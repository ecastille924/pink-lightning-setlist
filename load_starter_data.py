"""
Load Pink Lightning starter songs into the database.
This script clears existing songs and loads the actual band setlist.
"""

from app import create_app
from extensions import db
from models import Song

def load_starter_songs():
    app = create_app()

    with app.app_context():
        # Clear existing songs
        print("Clearing existing songs...")
        Song.query.delete()
        db.session.commit()
        print("✓ All existing songs removed")

        # Define the actual Pink Lightning setlist
        starter_songs = [
            {"title": "The Warrior", "artist": "Scandal", "era": "80s", "genre": "Rock"},
            {"title": "The Sign", "artist": "Ace of Base", "era": "90s", "genre": "Pop"},
            {"title": "One Way or Another", "artist": "Blondie", "era": "70s", "genre": "Rock"},
            {"title": "I'm So in Love with You", "artist": "Pink Lightning", "era": "2020s", "genre": "Rock"},
            {"title": "Oh! Darling", "artist": "The Beatles", "era": "60s", "genre": "Rock"},
            {"title": "I Wanna Be Your Lover", "artist": "Prince", "era": "80s", "genre": "Pop"},
            {"title": "Straight On", "artist": "Heart", "era": "70s", "genre": "Rock"},
            {"title": "Edge of Glory", "artist": "Lady Gaga", "era": "2010s", "genre": "Pop"},
            {"title": "Never Bow", "artist": "Pink Lightning", "era": "2020s", "genre": "Rock"},
            {"title": "Cherry Bomb", "artist": "The Runaways", "era": "70s", "genre": "Rock"},
            {"title": "You Oughta Know", "artist": "Alanis Morissette", "era": "90s", "genre": "Rock"},
            {"title": "Another One Bites the Dust", "artist": "Queen", "era": "80s", "genre": "Rock"},
            {"title": "Lovefool", "artist": "The Cardigans", "era": "90s", "genre": "Pop"},
            {"title": "Piece of My Heart", "artist": "Janis Joplin", "era": "60s", "genre": "Rock"},
            {"title": "All My Life", "artist": "Foo Fighters", "era": "90s", "genre": "Rock"},
            {"title": "I Love Rock and Roll", "artist": "Joan Jett", "era": "80s", "genre": "Rock"},
            {"title": "Valerie", "artist": "Amy Winehouse", "era": "2000s", "genre": "Pop"},
            {"title": "Don't Speak", "artist": "No Doubt", "era": "90s", "genre": "Rock"},
            {"title": "Barracuda", "artist": "Heart", "era": "70s", "genre": "Rock"},
            {"title": "Baby, One More Time", "artist": "Britney Spears", "era": "90s", "genre": "Pop"},
            {"title": "Back in Black", "artist": "AC/DC", "era": "80s", "genre": "Rock"},
            {"title": "Heartbreaker", "artist": "Pat Benatar", "era": "80s", "genre": "Rock"},
            {"title": "Shallow", "artist": "Lady Gaga", "era": "2010s", "genre": "Pop"},
            {"title": "Rock and Roll", "artist": "Joan Jett", "era": "80s", "genre": "Rock"},
            {"title": "Immigrant Song", "artist": "Led Zeppelin", "era": "70s", "genre": "Rock"},
            {"title": "Respect", "artist": "Aretha Franklin", "era": "60s", "genre": "Rock"},
            {"title": "Cannonball", "artist": "The Breeders", "era": "90s", "genre": "Rock"},
            {"title": "I Kissed a Girl", "artist": "Katy Perry", "era": "2000s", "genre": "Pop"},
            {"title": "I Want You to Want Me", "artist": "Letters to Cleo", "era": "90s", "genre": "Rock"},
            {"title": "I'm So Excited", "artist": "The Pointer Sisters", "era": "80s", "genre": "Pop"},
            {"title": "Your Love", "artist": "The Outfield", "era": "80s", "genre": "Rock"},
            {"title": "Since U Been Gone", "artist": "Kelly Clarkson", "era": "2000s", "genre": "Pop"},
            {"title": "I Hate Myself for Loving You", "artist": "Joan Jett", "era": "80s", "genre": "Rock"},
            {"title": "Just a Girl", "artist": "No Doubt", "era": "90s", "genre": "Rock"},
            {"title": "Any Way You Want It", "artist": "Journey", "era": "80s", "genre": "Rock"},
            {"title": "Rolling in the Deep", "artist": "Adele", "era": "2010s", "genre": "Pop"},
            {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "era": "90s", "genre": "Rock"},
            {"title": "Proud Mary", "artist": "Tina Turner", "era": "70s", "genre": "Rock"},
            {"title": "Go Your Own Way", "artist": "Fleetwood Mac", "era": "70s", "genre": "Rock"},
            {"title": "Knock on Wood", "artist": "Amii Stewart", "era": "70s", "genre": "Pop"},
            {"title": "Dangerous Woman", "artist": "Ariana Grande", "era": "2010s", "genre": "Pop"},
            {"title": "Halo", "artist": "Beyonce", "era": "2000s", "genre": "Pop"},
            {"title": "Hash Pipe", "artist": "Weezer", "era": "2000s", "genre": "Rock"},
            {"title": "You're No Good", "artist": "Linda Ronstadt", "era": "70s", "genre": "Rock"},
            {"title": "good 4 u", "artist": "Olivia Rodrigo", "era": "2020s", "genre": "Pop"},
            {"title": "Fat Lip", "artist": "Sum 41", "era": "2000s", "genre": "Rock"},
            {"title": "The Middle", "artist": "Jimmy Eat World", "era": "2000s", "genre": "Rock"},
            {"title": "Zombie", "artist": "The Cranberries", "era": "90s", "genre": "Rock"},
            {"title": "ABCDEFU", "artist": "Gayle", "era": "2020s", "genre": "Pop"},
            {"title": "The Best", "artist": "Tina Turner", "era": "80s", "genre": "Rock"},
            {"title": "Man! I Feel Like a Woman", "artist": "Shania Twain", "era": "90s", "genre": "Pop"},
            {"title": "I Believe in a Thing Called Love", "artist": "The Darkness", "era": "2000s", "genre": "Rock"},
            {"title": "Sk8er Boi", "artist": "Avril Lavigne", "era": "2000s", "genre": "Rock"},
            {"title": "Self Esteem", "artist": "The Offspring", "era": "90s", "genre": "Rock"},
            {"title": "Party in the USA", "artist": "Miley Cyrus", "era": "2000s", "genre": "Pop"},
            {"title": "More Than a Feeling", "artist": "Boston", "era": "70s", "genre": "Rock"},
            {"title": "The Anthem", "artist": "Good Charlotte", "era": "2000s", "genre": "Rock"},
            {"title": "I Wanna Dance with Somebody", "artist": "Whitney Houston", "era": "80s", "genre": "Pop"},
            {"title": "My Own Worst Enemy", "artist": "Lit", "era": "90s", "genre": "Rock"},
            {"title": "What's Up", "artist": "4 Non Blondes", "era": "90s", "genre": "Rock"},
            {"title": "Flowers", "artist": "Miley Cyrus", "era": "2020s", "genre": "Pop"},
            {"title": "Killing in the Name", "artist": "Rage Against the Machine", "era": "90s", "genre": "Rock"},
            {"title": "All the Small Things", "artist": "blink-182", "era": "90s", "genre": "Rock"},
            {"title": "Vampire", "artist": "Olivia Rodrigo", "era": "2020s", "genre": "Pop"},
            {"title": "Crazy", "artist": "Aerosmith", "era": "90s", "genre": "Rock"},
            {"title": "You Belong with Me", "artist": "Taylor Swift", "era": "2000s", "genre": "Pop"},
            {"title": "Give It Away", "artist": "Red Hot Chili Peppers", "era": "90s", "genre": "Rock"},
            {"title": "Whenever, Wherever", "artist": "Shakira", "era": "2000s", "genre": "Pop"},
            {"title": "Everlong", "artist": "Foo Fighters", "era": "90s", "genre": "Rock"},
            {"title": "Love Shack", "artist": "The B-52's", "era": "80s", "genre": "Pop"},
            {"title": "Better Man", "artist": "Pearl Jam", "era": "90s", "genre": "Rock"},
            {"title": "Basket Case", "artist": "Green Day", "era": "90s", "genre": "Rock"},
        ]

        print(f"\nAdding {len(starter_songs)} Pink Lightning songs...")

        added_count = 0
        for song_data in starter_songs:
            # Set default values
            song = Song(
                title=song_data["title"],
                artist=song_data["artist"],
                genre=song_data.get("genre", "Rock"),
                era=song_data.get("era", ""),
                frequency_weight=50.0,  # Default 50% for all songs
                first_set_only=False,
                second_set_only=False,
                potential_starting_song=False,
                potential_final_song=False,
                lead_vocals=None,  # Can be set later
                key=None  # Can be set later
            )

            db.session.add(song)
            added_count += 1

            if added_count % 10 == 0:
                print(f"  Added {added_count} songs...")

        db.session.commit()

        print(f"\n✓ Successfully added {added_count} songs to the database!")

        # Print statistics
        total_songs = Song.query.count()
        print(f"\nDatabase Statistics:")
        print(f"  Total songs: {total_songs}")
        print(f"  Rock songs: {Song.query.filter_by(genre='Rock').count()}")
        print(f"  Pop songs: {Song.query.filter_by(genre='Pop').count()}")
        print(f"  60s: {Song.query.filter_by(era='60s').count()}")
        print(f"  70s: {Song.query.filter_by(era='70s').count()}")
        print(f"  80s: {Song.query.filter_by(era='80s').count()}")
        print(f"  90s: {Song.query.filter_by(era='90s').count()}")
        print(f"  2000s: {Song.query.filter_by(era='2000s').count()}")
        print(f"  2010s: {Song.query.filter_by(era='2010s').count()}")
        print(f"  2020s: {Song.query.filter_by(era='2020s').count()}")

if __name__ == "__main__":
    load_starter_songs()
