"""
Set all songs without a lead vocalist to Lauren (default).
Run this once to update existing songs.
"""

from app import create_app
from extensions import db
from models import Song

def set_default_vocalists():
    app = create_app()

    with app.app_context():
        # Find all songs without a lead vocalist
        songs_without_vocals = Song.query.filter(
            (Song.lead_vocals == None) | (Song.lead_vocals == '')
        ).all()

        if not songs_without_vocals:
            print("✓ All songs already have a lead vocalist assigned!")
            return

        print(f"Found {len(songs_without_vocals)} songs without lead vocals")
        print("Setting default to 'Lauren'...\n")

        updated_count = 0
        for song in songs_without_vocals:
            print(f"  • {song.title} by {song.artist}")
            song.lead_vocals = 'Lauren'
            updated_count += 1

        db.session.commit()

        print(f"\n✓ Successfully updated {updated_count} songs to Lauren as lead vocalist!")

        # Verify
        remaining = Song.query.filter(
            (Song.lead_vocals == None) | (Song.lead_vocals == '')
        ).count()

        if remaining == 0:
            print("✓ All songs now have a lead vocalist assigned")
        else:
            print(f"⚠ Warning: {remaining} songs still without vocalist")

if __name__ == "__main__":
    set_default_vocalists()
