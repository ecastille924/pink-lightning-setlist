"""
Add keys to songs where we have confident information about the original recordings.
"""

from app import create_app
from extensions import db
from models import Song

def add_song_keys():
    app = create_app()

    with app.app_context():
        # Dictionary of songs with their commonly known keys
        # Only including songs where the key is well-documented and commonly known
        song_keys = {
            ("The Warrior", "Scandal"): "Em",
            ("The Sign", "Ace of Base"): "F#m",
            ("One Way or Another", "Blondie"): "D",
            ("Oh! Darling", "The Beatles"): "A",
            ("I Wanna Be Your Lover", "Prince"): "C#m",
            ("Straight On", "Heart"): "Em",
            ("Edge of Glory", "Lady Gaga"): "Am",
            ("Cherry Bomb", "The Runaways"): "A",
            ("You Oughta Know", "Alanis Morissette"): "F#m",
            ("Another One Bites the Dust", "Queen"): "Em",
            ("Lovefool", "The Cardigans"): "Am",
            ("Piece of My Heart", "Janis Joplin"): "E",
            ("All My Life", "Foo Fighters"): "G",
            ("I Love Rock and Roll", "Joan Jett"): "E",
            ("Valerie", "Amy Winehouse"): "Eb",
            ("Don't Speak", "No Doubt"): "Cm",
            ("Barracuda", "Heart"): "E",
            ("Baby, One More Time", "Britney Spears"): "Cm",
            ("Back in Black", "AC/DC"): "E",
            ("Heartbreaker", "Pat Benatar"): "A",
            ("Shallow", "Lady Gaga"): "G",
            ("Immigrant Song", "Led Zeppelin"): "F#m",
            ("Respect", "Aretha Franklin"): "C",
            ("Cannonball", "The Breeders"): "E",
            ("I Kissed a Girl", "Katy Perry"): "C#",
            ("I Want You to Want Me", "Letters to Cleo"): "A",
            ("I'm So Excited", "The Pointer Sisters"): "F",
            ("Your Love", "The Outfield"): "A",
            ("Since U Been Gone", "Kelly Clarkson"): "G",
            ("I Hate Myself for Loving You", "Joan Jett"): "A",
            ("Just a Girl", "No Doubt"): "D",
            ("Any Way You Want It", "Journey"): "D",
            ("Rolling in the Deep", "Adele"): "Cm",
            ("Smells Like Teen Spirit", "Nirvana"): "F",
            ("Proud Mary", "Tina Turner"): "D",
            ("Go Your Own Way", "Fleetwood Mac"): "F",
            ("Knock on Wood", "Amii Stewart"): "Am",
            ("Dangerous Woman", "Ariana Grande"): "E",
            ("Halo", "Beyonce"): "Ab",
            ("Hash Pipe", "Weezer"): "G#",
            ("You're No Good", "Linda Ronstadt"): "Am",
            ("good 4 u", "Olivia Rodrigo"): "Ab",
            ("Fat Lip", "Sum 41"): "F",
            ("The Middle", "Jimmy Eat World"): "C",
            ("Zombie", "The Cranberries"): "Em",
            ("ABCDEFU", "Gayle"): "G",
            ("The Best", "Tina Turner"): "C",
            ("Man! I Feel Like a Woman", "Shania Twain"): "Eb",
            ("I Believe in a Thing Called Love", "The Darkness"): "E",
            ("Sk8er Boi", "Avril Lavigne"): "D",
            ("Self Esteem", "The Offspring"): "F#",
            ("Party in the USA", "Miley Cyrus"): "Bb",
            ("More Than a Feeling", "Boston"): "D",
            ("The Anthem", "Good Charlotte"): "E",
            ("I Wanna Dance with Somebody", "Whitney Houston"): "F",
            ("My Own Worst Enemy", "Lit"): "Eb",
            ("What's Up", "4 Non Blondes"): "A",
            ("Flowers", "Miley Cyrus"): "G",
            ("Killing in the Name", "Rage Against the Machine"): "Dm",
            ("All the Small Things", "blink-182"): "C",
            ("Vampire", "Olivia Rodrigo"): "Bb",
            ("Crazy", "Aerosmith"): "A",
            ("You Belong with Me", "Taylor Swift"): "G",
            ("Give It Away", "Red Hot Chili Peppers"): "A",
            ("Whenever, Wherever", "Shakira"): "C#m",
            ("Everlong", "Foo Fighters"): "D",
            ("Love Shack", "The B-52's"): "D",
            ("Better Man", "Pearl Jam"): "D",
            ("Basket Case", "Green Day"): "Eb",
        }

        print("Adding keys to songs...")
        updated_count = 0
        not_found = []

        for (title, artist), key in song_keys.items():
            song = Song.query.filter_by(title=title, artist=artist).first()

            if song:
                song.key = key
                updated_count += 1
                print(f"  ✓ {title} by {artist} → {key}")
            else:
                not_found.append((title, artist))
                print(f"  ✗ Not found: {title} by {artist}")

        db.session.commit()

        print(f"\n✓ Successfully added keys to {updated_count} songs!")

        # Show songs without keys
        songs_without_keys = Song.query.filter(
            (Song.key == None) | (Song.key == '')
        ).all()

        if songs_without_keys:
            print(f"\n⚠ {len(songs_without_keys)} songs still need keys:")
            for song in songs_without_keys:
                print(f"  - {song.title} by {song.artist}")

        # Statistics
        songs_with_keys = Song.query.filter(
            (Song.key != None) & (Song.key != '')
        ).count()
        total_songs = Song.query.count()

        print(f"\nDatabase Statistics:")
        print(f"  Total songs: {total_songs}")
        print(f"  Songs with keys: {songs_with_keys}")
        print(f"  Songs without keys: {total_songs - songs_with_keys}")

if __name__ == "__main__":
    add_song_keys()
