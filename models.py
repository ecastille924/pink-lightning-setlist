from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    """User model for authentication"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        """Hash and set password"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if provided password matches hash"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Song(db.Model):
    """Song model with all attributes for setlist generation"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    artist = db.Column(db.String(200), nullable=False)
    key = db.Column(db.String(20))
    genre = db.Column(db.String(100))
    era = db.Column(db.String(50))
    lead_vocals = db.Column(db.String(100))

    # Checkboxes for set placement rules
    first_set_only = db.Column(db.Boolean, default=False)
    second_set_only = db.Column(db.Boolean, default=False)
    potential_starting_song = db.Column(db.Boolean, default=False)
    potential_final_song = db.Column(db.Boolean, default=False)

    # Frequency weight (0-100%)
    frequency_weight = db.Column(db.Float, default=50.0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Song {self.title} by {self.artist}>'

    def to_dict(self):
        """Convert song to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'key': self.key,
            'genre': self.genre,
            'era': self.era,
            'lead_vocals': self.lead_vocals,
            'first_set_only': self.first_set_only,
            'second_set_only': self.second_set_only,
            'potential_starting_song': self.potential_starting_song,
            'potential_final_song': self.potential_final_song,
            'frequency_weight': self.frequency_weight
        }

class SavedSetlist(db.Model):
    """Saved setlist model for storing generated setlists"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)

    # Relationship to songs through association table
    songs = db.relationship('SetlistSong', back_populates='setlist', cascade='all, delete-orphan', order_by='SetlistSong.position')

    def __repr__(self):
        return f'<SavedSetlist {self.name}>'

class SetlistSong(db.Model):
    """Association table for saved setlists and songs with ordering"""
    id = db.Column(db.Integer, primary_key=True)
    setlist_id = db.Column(db.Integer, db.ForeignKey('saved_setlist.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    set_number = db.Column(db.Integer, nullable=False)  # 1, 2, or 3
    position = db.Column(db.Integer, nullable=False)  # Order within the entire setlist

    # Relationships
    setlist = db.relationship('SavedSetlist', back_populates='songs')
    song = db.relationship('Song')

    def __repr__(self):
        return f'<SetlistSong setlist={self.setlist_id} song={self.song_id} pos={self.position}>'
