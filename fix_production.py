"""
Production Database Diagnostic and Fix Script
Run this on Render shell to diagnose and fix issues
"""
from app import create_app
from extensions import db
from models import User, Song, SavedSetlist, SetlistSong

app = create_app()

with app.app_context():
    print("\n" + "="*60)
    print("PINK LIGHTNING - PRODUCTION DIAGNOSTIC")
    print("="*60)

    # Check if tables exist
    print("\n1. Checking database tables...")
    try:
        user_count = User.query.count()
        print(f"   ✓ User table exists - {user_count} users")
    except Exception as e:
        print(f"   ✗ User table error: {e}")

    try:
        song_count = Song.query.count()
        print(f"   ✓ Song table exists - {song_count} songs")
    except Exception as e:
        print(f"   ✗ Song table error: {e}")

    try:
        setlist_count = SavedSetlist.query.count()
        print(f"   ✓ SavedSetlist table exists - {setlist_count} saved setlists")
    except Exception as e:
        print(f"   ✗ SavedSetlist table missing or error: {e}")
        print("   → Running db.create_all() to create missing tables...")
        db.create_all()
        print("   ✓ Tables created!")
        setlist_count = SavedSetlist.query.count()
        print(f"   ✓ SavedSetlist table now has {setlist_count} saved setlists")

    try:
        setlist_song_count = SetlistSong.query.count()
        print(f"   ✓ SetlistSong table exists - {setlist_song_count} entries")
    except Exception as e:
        print(f"   ✗ SetlistSong table missing or error: {e}")
        print("   → Running db.create_all() to create missing tables...")
        db.create_all()
        print("   ✓ Tables created!")
        setlist_song_count = SetlistSong.query.count()
        print(f"   ✓ SetlistSong table now has {setlist_song_count} entries")

    # Check environment variables
    print("\n2. Checking environment variables...")
    import os
    skip_starter = os.environ.get('SKIP_STARTER_DATA', 'NOT SET')
    print(f"   SKIP_STARTER_DATA = {skip_starter}")
    if skip_starter == 'NOT SET' or skip_starter.lower() != 'true':
        print("   ⚠ WARNING: SKIP_STARTER_DATA should be 'true' to preserve edits!")
    else:
        print("   ✓ SKIP_STARTER_DATA is correctly set")

    database_url = os.environ.get('DATABASE_URL', 'NOT SET')
    if database_url != 'NOT SET':
        # Mask password in URL for security
        if '@' in database_url:
            parts = database_url.split('@')
            masked = parts[0].split(':')
            if len(masked) > 2:
                masked[2] = '****'
            print(f"   DATABASE_URL = {':'.join(masked)}@{parts[1]}")
        else:
            print(f"   DATABASE_URL = {database_url}")
    else:
        print("   DATABASE_URL = NOT SET (using SQLite)")

    # Sample some songs to check data integrity
    print("\n3. Checking sample songs...")
    sample_songs = Song.query.limit(5).all()
    for song in sample_songs:
        print(f"   • {song.title} by {song.artist}")
        print(f"     Key: {song.key or 'None'}, Vocals: {song.lead_vocals or 'None'}, Freq: {song.frequency_weight}")

    # Check for specific song (ABCDEFU) to verify edit persistence
    print("\n4. Checking for edit persistence test (ABCDEFU)...")
    abcd_song = Song.query.filter_by(title="ABCDEFU", artist="Gayle").first()
    if abcd_song:
        print(f"   Found: ABCDEFU by Gayle")
        print(f"   Current key: {abcd_song.key}")
        print(f"   (If you changed this to 'E' and it shows 'G', edits are NOT persisting)")
    else:
        print("   ABCDEFU not found in database")

    print("\n" + "="*60)
    print("DIAGNOSTIC COMPLETE")
    print("="*60)
    print("\nIf SavedSetlist or SetlistSong tables were missing, they have been created.")
    print("Try saving a setlist again through the web interface.")
    print("\nIf song edits are not persisting:")
    print("1. Set SKIP_STARTER_DATA=true in Render environment variables")
    print("2. Save and redeploy")
    print("="*60 + "\n")
