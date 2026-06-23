from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from models import Song, SavedSetlist, SetlistSong
from extensions import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    """Home page - redirect to songs list"""
    return redirect(url_for('main.list_songs'))

@main_bp.route('/songs')
@login_required
def list_songs():
    """List all songs"""
    songs = Song.query.order_by(Song.title).all()
    return render_template('songs.html', songs=songs)

@main_bp.route('/songs/add', methods=['GET', 'POST'])
@login_required
def add_song():
    """Add a new song"""
    if request.method == 'POST':
        try:
            song = Song(
                title=request.form.get('title'),
                artist=request.form.get('artist'),
                key=request.form.get('key'),
                genre=request.form.get('genre'),
                era=request.form.get('era'),
                lead_vocals=request.form.get('lead_vocals') or 'Lauren',  # Default to Lauren
                first_set_only=bool(request.form.get('first_set_only')),
                second_set_only=bool(request.form.get('second_set_only')),
                potential_starting_song=bool(request.form.get('potential_starting_song')),
                potential_final_song=bool(request.form.get('potential_final_song')),
                frequency_weight=float(request.form.get('frequency_weight', 50.0))
            )
            db.session.add(song)
            db.session.commit()
            flash(f'Song "{song.title}" added successfully!', 'success')
            return redirect(url_for('main.list_songs'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding song: {str(e)}', 'danger')

    return render_template('add_song.html')

@main_bp.route('/songs/add-multiple', methods=['GET', 'POST'])
@login_required
def add_multiple_songs():
    """Add multiple songs at once"""
    if request.method == 'POST':
        try:
            song_count = int(request.form.get('song_count', 0))
            added_count = 0

            for i in range(1, song_count + 1):
                # Check if this song has required fields
                title = request.form.get(f'title_{i}')
                artist = request.form.get(f'artist_{i}')

                if not title or not artist:
                    continue

                # Create song with all fields
                song = Song(
                    title=title,
                    artist=artist,
                    key=request.form.get(f'key_{i}', ''),
                    genre=request.form.get(f'genre_{i}', ''),
                    era=request.form.get(f'era_{i}', ''),
                    lead_vocals=request.form.get(f'lead_vocals_{i}', '') or 'Lauren',  # Default to Lauren
                    first_set_only=bool(request.form.get(f'first_set_only_{i}')),
                    second_set_only=bool(request.form.get(f'second_set_only_{i}')),
                    potential_starting_song=bool(request.form.get(f'potential_starting_song_{i}')),
                    potential_final_song=bool(request.form.get(f'potential_final_song_{i}')),
                    frequency_weight=float(request.form.get(f'frequency_weight_{i}', 50.0))
                )
                db.session.add(song)
                added_count += 1

            db.session.commit()
            flash(f'{added_count} song(s) added successfully!', 'success')
            return redirect(url_for('main.list_songs'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding songs: {str(e)}', 'danger')

    return render_template('add_multiple_songs.html')

@main_bp.route('/songs/edit/<int:song_id>', methods=['GET', 'POST'])
@login_required
def edit_song(song_id):
    """Edit an existing song"""
    song = Song.query.get_or_404(song_id)

    if request.method == 'POST':
        try:
            song.title = request.form.get('title')
            song.artist = request.form.get('artist')
            song.key = request.form.get('key')
            song.genre = request.form.get('genre')
            song.era = request.form.get('era')
            song.lead_vocals = request.form.get('lead_vocals') or 'Lauren'  # Default to Lauren
            song.first_set_only = bool(request.form.get('first_set_only'))
            song.second_set_only = bool(request.form.get('second_set_only'))
            song.potential_starting_song = bool(request.form.get('potential_starting_song'))
            song.potential_final_song = bool(request.form.get('potential_final_song'))
            song.frequency_weight = float(request.form.get('frequency_weight', 50.0))

            db.session.commit()
            flash(f'Song "{song.title}" updated successfully!', 'success')
            return redirect(url_for('main.list_songs'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating song: {str(e)}', 'danger')

    return render_template('edit_song.html', song=song)

@main_bp.route('/songs/delete/<int:song_id>', methods=['POST'])
@login_required
def delete_song(song_id):
    """Delete a song"""
    song = Song.query.get_or_404(song_id)
    try:
        title = song.title
        db.session.delete(song)
        db.session.commit()
        flash(f'Song "{title}" deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting song: {str(e)}', 'danger')

    return redirect(url_for('main.list_songs'))

@main_bp.route('/generate')
@login_required
def generate_setlist():
    """Setlist generation page"""
    total_songs = Song.query.count()
    return render_template('generate.html', total_songs=total_songs)

@main_bp.route('/generate/create', methods=['POST'])
@login_required
def create_setlist():
    """Generate a setlist based on user parameters"""
    from setlist_generator import generate_setlist as gen_setlist

    try:
        num_sets = int(request.form.get('num_sets', 2))
        songs_per_set = []

        for i in range(1, num_sets + 1):
            count = int(request.form.get(f'songs_set_{i}', 0))
            songs_per_set.append(count)

        # Generate the setlist
        setlists, warnings = gen_setlist(num_sets, songs_per_set)

        # Display warnings if any
        for warning in warnings:
            flash(warning, 'warning')

        return render_template('setlist_result.html', setlists=setlists, num_sets=num_sets)

    except ValueError as e:
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('main.generate_setlist'))
    except Exception as e:
        flash(f'Unexpected error: {str(e)}', 'danger')
        return redirect(url_for('main.generate_setlist'))

# API endpoints for setlist editing
@main_bp.route('/api/songs')
@login_required
def api_get_songs():
    """API endpoint to get all songs as JSON"""
    songs = Song.query.order_by(Song.title).all()
    return jsonify([song.to_dict() for song in songs])

@main_bp.route('/api/songs/<int:song_id>')
@login_required
def api_get_song(song_id):
    """API endpoint to get a single song as JSON"""
    song = Song.query.get_or_404(song_id)
    return jsonify(song.to_dict())

# Saved setlists routes
@main_bp.route('/setlists/save', methods=['POST'])
@login_required
def save_setlist():
    """Save a generated setlist"""
    try:
        import json

        # Get form data
        setlist_name = request.form.get('setlist_name', '').strip()
        notes = request.form.get('notes', '').strip()
        setlist_data = request.form.get('setlist_data')

        if not setlist_name:
            flash('Please provide a name for the setlist', 'warning')
            return redirect(request.referrer or url_for('main.generate_setlist'))

        if not setlist_data:
            flash('No setlist data provided', 'danger')
            return redirect(request.referrer or url_for('main.generate_setlist'))

        # Parse the setlist JSON data
        setlist = json.loads(setlist_data)

        # Create saved setlist
        saved_setlist = SavedSetlist(
            name=setlist_name,
            notes=notes
        )
        db.session.add(saved_setlist)
        db.session.flush()  # Get the ID without committing

        # Add songs to setlist
        position = 0
        for set_num, songs in enumerate(setlist, start=1):
            for song_id in songs:
                setlist_song = SetlistSong(
                    setlist_id=saved_setlist.id,
                    song_id=song_id,
                    set_number=set_num,
                    position=position
                )
                db.session.add(setlist_song)
                position += 1

        db.session.commit()
        flash(f'Setlist "{setlist_name}" saved successfully!', 'success')
        return redirect(url_for('main.view_saved_setlist', setlist_id=saved_setlist.id))

    except Exception as e:
        db.session.rollback()
        flash(f'Error saving setlist: {str(e)}', 'danger')
        return redirect(request.referrer or url_for('main.generate_setlist'))

@main_bp.route('/setlists')
@login_required
def list_saved_setlists():
    """List all saved setlists"""
    setlists = SavedSetlist.query.order_by(SavedSetlist.created_at.desc()).all()
    return render_template('saved_setlists.html', setlists=setlists)

@main_bp.route('/setlists/<int:setlist_id>')
@login_required
def view_saved_setlist(setlist_id):
    """View a specific saved setlist"""
    setlist = SavedSetlist.query.get_or_404(setlist_id)

    # Organize songs by set number
    sets = {}
    for setlist_song in setlist.songs:
        set_num = setlist_song.set_number
        if set_num not in sets:
            sets[set_num] = []
        sets[set_num].append(setlist_song.song)

    # Convert to ordered list
    organized_setlist = [sets.get(i, []) for i in range(1, max(sets.keys()) + 1)]

    return render_template('view_saved_setlist.html', setlist=setlist, sets=organized_setlist)

@main_bp.route('/setlists/<int:setlist_id>/delete', methods=['POST'])
@login_required
def delete_saved_setlist(setlist_id):
    """Delete a saved setlist"""
    try:
        setlist = SavedSetlist.query.get_or_404(setlist_id)
        setlist_name = setlist.name

        db.session.delete(setlist)
        db.session.commit()

        flash(f'Setlist "{setlist_name}" deleted successfully', 'success')
        return redirect(url_for('main.list_saved_setlists'))

    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting setlist: {str(e)}', 'danger')
        return redirect(url_for('main.list_saved_setlists'))
