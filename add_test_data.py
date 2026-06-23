"""Add test data - 80 popular rock and pop songs"""
from app import create_app
from extensions import db
from models import Song

app = create_app()

# Test data: 80 popular songs from 70s-2020s
test_songs = [
    # 1970s
    ("Bohemian Rhapsody", "Queen", "Bb", "Rock", "70s", "Freddie", 95, False, False, True, True),
    ("Hotel California", "Eagles", "Bm", "Rock", "70s", "Don", 90, False, False, True, False),
    ("Sweet Home Alabama", "Lynyrd Skynyrd", "D", "Rock", "70s", "Ronnie", 88, False, False, True, False),
    ("Dream On", "Aerosmith", "Fm", "Rock", "70s", "Steven", 75, False, False, False, False),
    ("Stairway to Heaven", "Led Zeppelin", "Am", "Rock", "70s", "Robert", 85, False, False, False, True),
    ("Go Your Own Way", "Fleetwood Mac", "F", "Rock", "70s", "Lindsey", 80, False, False, False, False),
    ("Born to Run", "Bruce Springsteen", "E", "Rock", "70s", "Bruce", 82, False, False, True, False),
    ("More Than a Feeling", "Boston", "D", "Rock", "70s", "Brad", 78, False, False, False, False),
    ("Free Bird", "Lynyrd Skynyrd", "G", "Rock", "70s", "Ronnie", 70, False, False, False, True),
    ("Layla", "Eric Clapton", "Dm", "Rock", "70s", "Eric", 72, False, False, False, False),

    # 1980s
    ("Don't Stop Believin'", "Journey", "E", "Rock", "80s", "Steve", 98, False, False, True, True),
    ("Livin' on a Prayer", "Bon Jovi", "Em", "Rock", "80s", "Jon", 95, False, False, True, True),
    ("Sweet Child O' Mine", "Guns N' Roses", "D", "Rock", "80s", "Axl", 92, False, False, True, False),
    ("Every Breath You Take", "The Police", "Ab", "Rock", "80s", "Sting", 85, False, False, False, False),
    ("I Love Rock 'n Roll", "Joan Jett", "E", "Rock", "80s", "Joan", 88, False, False, True, False),
    ("Pour Some Sugar on Me", "Def Leppard", "E", "Rock", "80s", "Joe", 83, False, False, False, False),
    ("You Give Love a Bad Name", "Bon Jovi", "Cm", "Rock", "80s", "Jon", 87, False, False, True, False),
    ("Jump", "Van Halen", "C", "Rock", "80s", "David", 90, False, False, True, False),
    ("Girls Just Want to Have Fun", "Cyndi Lauper", "G", "Pop", "80s", "Cyndi", 85, False, False, False, False),
    ("Jessie's Girl", "Rick Springfield", "D", "Rock", "80s", "Rick", 80, False, False, False, False),
    ("Come On Eileen", "Dexys Midnight Runners", "C", "Pop", "80s", "Kevin", 75, False, False, False, False),
    ("Take On Me", "a-ha", "A", "Pop", "80s", "Morten", 82, False, False, False, False),
    ("Here I Go Again", "Whitesnake", "G", "Rock", "80s", "David", 78, False, False, False, False),
    ("We're Not Gonna Take It", "Twisted Sister", "E", "Rock", "80s", "Dee", 77, False, False, True, False),
    ("Eye of the Tiger", "Survivor", "Cm", "Rock", "80s", "Dave", 88, False, False, True, False),

    # 1990s
    ("Smells Like Teen Spirit", "Nirvana", "F", "Rock", "90s", "Kurt", 94, False, False, True, False),
    ("Under the Bridge", "Red Hot Chili Peppers", "E", "Rock", "90s", "Anthony", 86, False, False, False, False),
    ("Black Hole Sun", "Soundgarden", "G", "Rock", "90s", "Chris", 75, False, False, False, False),
    ("Wonderwall", "Oasis", "Em", "Rock", "90s", "Liam", 92, False, False, False, False),
    ("Come as You Are", "Nirvana", "Em", "Rock", "90s", "Kurt", 85, False, False, False, False),
    ("No Rain", "Blind Melon", "E", "Rock", "90s", "Shannon", 70, False, False, False, False),
    ("Runaway Train", "Soul Asylum", "C", "Rock", "90s", "Dave", 72, False, False, False, False),
    ("Semi-Charmed Life", "Third Eye Blind", "G", "Rock", "90s", "Stephan", 88, False, False, True, False),
    ("All Star", "Smash Mouth", "F#", "Rock", "90s", "Steve", 83, False, False, True, False),
    ("Song 2", "Blur", "F#", "Rock", "90s", "Damon", 78, False, False, True, False),
    ("Closing Time", "Semisonic", "G", "Rock", "90s", "Dan", 80, False, False, False, True),
    ("Mr. Jones", "Counting Crows", "Am", "Rock", "90s", "Adam", 75, False, False, False, False),
    ("I Want You to Want Me", "Letters to Cleo", "A", "Rock", "90s", "Kay", 77, False, False, False, False),
    ("What I Got", "Sublime", "D", "Rock", "90s", "Bradley", 82, False, False, False, False),
    ("Sex and Candy", "Marcy Playground", "A", "Rock", "90s", "John", 73, False, False, False, False),

    # 2000s
    ("Mr. Brightside", "The Killers", "D", "Rock", "2000s", "Brandon", 96, False, False, True, False),
    ("How to Save a Life", "The Fray", "Bb", "Rock", "2000s", "Isaac", 84, False, False, False, False),
    ("I Will Wait", "Mumford & Sons", "Bm", "Rock", "2000s", "Marcus", 81, False, False, False, False),
    ("Use Somebody", "Kings of Leon", "C", "Rock", "2000s", "Caleb", 86, False, False, False, False),
    ("Are You Gonna Be My Girl", "Jet", "A", "Rock", "2000s", "Nic", 89, False, False, True, False),
    ("Seven Nation Army", "The White Stripes", "E", "Rock", "2000s", "Jack", 91, False, False, True, False),
    ("Last Resort", "Papa Roach", "Dm", "Rock", "2000s", "Jacoby", 79, False, False, False, False),
    ("Basket Case", "Green Day", "Eb", "Rock", "2000s", "Billie", 87, False, False, False, False),
    ("Boulevard of Broken Dreams", "Green Day", "Fm", "Rock", "2000s", "Billie", 88, False, False, False, False),
    ("In Too Deep", "Sum 41", "D", "Rock", "2000s", "Deryck", 76, False, False, False, False),
    ("Ocean Avenue", "Yellowcard", "C", "Rock", "2000s", "Ryan", 80, False, False, False, False),
    ("The Middle", "Jimmy Eat World", "C", "Rock", "2000s", "Jim", 85, False, False, True, False),
    ("Sugar, We're Goin Down", "Fall Out Boy", "D", "Rock", "2000s", "Patrick", 90, False, False, True, False),
    ("Pocket Full of Sunshine", "Natasha Bedingfield", "A", "Pop", "2000s", "Natasha", 74, False, False, False, False),
    ("Since U Been Gone", "Kelly Clarkson", "G", "Pop", "2000s", "Kelly", 86, False, False, True, False),

    # 2010s
    ("Shut Up and Dance", "Walk the Moon", "C", "Pop", "2010s", "Nicholas", 92, False, False, True, False),
    ("Pumped Up Kicks", "Foster the People", "F#m", "Pop", "2010s", "Mark", 88, False, False, False, False),
    ("Radioactive", "Imagine Dragons", "Bm", "Rock", "2010s", "Dan", 93, False, False, True, False),
    ("Ride", "Twenty One Pilots", "C#m", "Rock", "2010s", "Tyler", 85, False, False, False, False),
    ("Stressed Out", "Twenty One Pilots", "F", "Rock", "2010s", "Tyler", 89, False, False, False, False),
    ("Heathens", "Twenty One Pilots", "C#m", "Rock", "2010s", "Tyler", 84, False, False, False, False),
    ("Believer", "Imagine Dragons", "Bb", "Rock", "2010s", "Dan", 91, False, False, True, False),
    ("Thunder", "Imagine Dragons", "C", "Rock", "2010s", "Dan", 87, False, False, False, False),
    ("High Hopes", "Panic! at the Disco", "Bb", "Pop", "2010s", "Brendon", 90, False, False, True, False),
    ("Uptown Funk", "Bruno Mars", "Dm", "Pop", "2010s", "Bruno", 95, False, False, True, True),
    ("Counting Stars", "OneRepublic", "C#m", "Pop", "2010s", "Ryan", 88, False, False, False, False),
    ("Wake Me Up", "Avicii", "Bm", "Pop", "2010s", "Aloe", 86, False, False, False, False),
    ("Best Day of My Life", "American Authors", "G", "Pop", "2010s", "Zac", 82, False, False, True, False),
    ("Safe and Sound", "Capital Cities", "C", "Pop", "2010s", "Ryan", 79, False, False, False, False),
    ("Rude", "MAGIC!", "D", "Pop", "2010s", "Nasri", 81, False, False, False, False),
    ("Riptide", "Vance Joy", "Am", "Pop", "2010s", "Vance", 83, False, False, False, False),
    ("Ho Hey", "The Lumineers", "C", "Folk Rock", "2010s", "Wesley", 85, False, False, False, False),
    ("Little Talks", "Of Monsters and Men", "Am", "Folk Rock", "2010s", "Nanna", 80, False, False, False, False),
    ("My Songs Know What You Did", "Fall Out Boy", "C", "Rock", "2010s", "Patrick", 78, False, False, False, False),
    ("Centuries", "Fall Out Boy", "Cm", "Rock", "2010s", "Patrick", 84, False, False, True, False),

    # 2020s
    ("Blinding Lights", "The Weeknd", "Fm", "Pop", "2020s", "Abel", 97, False, False, True, False),
    ("Levitating", "Dua Lipa", "B", "Pop", "2020s", "Dua", 94, False, False, True, False),
    ("Heat Waves", "Glass Animals", "Bm", "Pop", "2020s", "Dave", 91, False, False, False, False),
    ("good 4 u", "Olivia Rodrigo", "Ab", "Pop Rock", "2020s", "Olivia", 93, False, False, True, False),
    ("drivers license", "Olivia Rodrigo", "Bb", "Pop", "2020s", "Olivia", 86, False, False, False, False),
]

with app.app_context():
    # Clear existing songs (optional - comment out if you want to keep existing data)
    # Song.query.delete()

    added_count = 0
    for song_data in test_songs:
        title, artist, key, genre, era, vocals, freq, first_set, second_set, starting, final = song_data

        # Check if song already exists
        existing = Song.query.filter_by(title=title, artist=artist).first()
        if existing:
            print(f"Skipping '{title}' - already exists")
            continue

        song = Song(
            title=title,
            artist=artist,
            key=key,
            genre=genre,
            era=era,
            lead_vocals=vocals,
            frequency_weight=freq,
            first_set_only=first_set,
            second_set_only=second_set,
            potential_starting_song=starting,
            potential_final_song=final
        )
        db.session.add(song)
        added_count += 1

    db.session.commit()
    print(f"\n✓ Successfully added {added_count} songs to the database!")
    print(f"Total songs in database: {Song.query.count()}")

    # Show some statistics
    starting_songs = Song.query.filter_by(potential_starting_song=True).count()
    final_songs = Song.query.filter_by(potential_final_song=True).count()

    print(f"\nStatistics:")
    print(f"  - Potential starting songs: {starting_songs}")
    print(f"  - Potential final songs: {final_songs}")
    print(f"  - Average frequency weight: {db.session.query(db.func.avg(Song.frequency_weight)).scalar():.1f}%")
