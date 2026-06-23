import os
from flask import Flask
from extensions import db, login_manager

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

    # Database configuration - PostgreSQL for production, SQLite for development
    database_url = os.environ.get('DATABASE_URL')
    if database_url and database_url.startswith('postgres://'):
        # Render.com provides postgres:// but SQLAlchemy needs postgresql://
        database_url = database_url.replace('postgres://', 'postgresql://', 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'sqlite:///pinklightning.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'

    # Import models before blueprints
    from models import User, Song

    # Register user_loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import and register blueprints
    from auth import auth_bp
    from routes import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    # Create database tables and default user
    with app.app_context():
        db.create_all()
        print("Database tables created!")

        # Create default user if it doesn't exist
        existing_user = User.query.filter_by(username='pinklightning').first()
        if not existing_user:
            default_user = User(username='pinklightning')
            default_user.set_password('gottohave100')
            db.session.add(default_user)
            db.session.commit()
            print("✓ Default user created: pinklightning / gottohave100")
        else:
            print("✓ Default user already exists")

        # Load starter songs if database is empty
        # Set SKIP_STARTER_DATA=true in Render environment variables to prevent reloading
        song_count = Song.query.count()
        skip_starter = os.environ.get('SKIP_STARTER_DATA', 'false').lower() == 'true'

        if song_count == 0 and not skip_starter:
            print("\n🎵 Loading Pink Lightning starter songs...")
            print("   (Set SKIP_STARTER_DATA=true to prevent this in future deploys)")

            # Starter songs data with keys
            starter_songs = [
        {"title": "The Warrior", "artist": "Scandal", "era": "80s", "genre": "Rock", "key": "Em"},
        {"title": "The Sign", "artist": "Ace of Base", "era": "90s", "genre": "Pop", "key": "F#m"},
        {"title": "One Way or Another", "artist": "Blondie", "era": "70s", "genre": "Rock", "key": "D"},
        {"title": "I'm So in Love with You", "artist": "Pink Lightning", "era": "2020s", "genre": "Rock"},
        {"title": "Oh! Darling", "artist": "The Beatles", "era": "60s", "genre": "Rock", "key": "A"},
        {"title": "I Wanna Be Your Lover", "artist": "Prince", "era": "80s", "genre": "Pop", "key": "C#m"},
        {"title": "Straight On", "artist": "Heart", "era": "70s", "genre": "Rock", "key": "Em"},
        {"title": "Edge of Glory", "artist": "Lady Gaga", "era": "2010s", "genre": "Pop", "key": "Am"},
        {"title": "Never Bow", "artist": "Pink Lightning", "era": "2020s", "genre": "Rock"},
        {"title": "Cherry Bomb", "artist": "The Runaways", "era": "70s", "genre": "Rock", "key": "A"},
        {"title": "You Oughta Know", "artist": "Alanis Morissette", "era": "90s", "genre": "Rock", "key": "F#m"},
        {"title": "Another One Bites the Dust", "artist": "Queen", "era": "80s", "genre": "Rock", "key": "Em"},
        {"title": "Lovefool", "artist": "The Cardigans", "era": "90s", "genre": "Pop", "key": "Am"},
        {"title": "Piece of My Heart", "artist": "Janis Joplin", "era": "60s", "genre": "Rock", "key": "E"},
        {"title": "All My Life", "artist": "Foo Fighters", "era": "90s", "genre": "Rock", "key": "G"},
        {"title": "I Love Rock and Roll", "artist": "Joan Jett", "era": "80s", "genre": "Rock", "key": "E"},
        {"title": "Valerie", "artist": "Amy Winehouse", "era": "2000s", "genre": "Pop", "key": "Eb"},
        {"title": "Don't Speak", "artist": "No Doubt", "era": "90s", "genre": "Rock", "key": "Cm"},
        {"title": "Barracuda", "artist": "Heart", "era": "70s", "genre": "Rock", "key": "E"},
        {"title": "Baby, One More Time", "artist": "Britney Spears", "era": "90s", "genre": "Pop", "key": "Cm"},
        {"title": "Back in Black", "artist": "AC/DC", "era": "80s", "genre": "Rock", "key": "E"},
        {"title": "Heartbreaker", "artist": "Pat Benatar", "era": "80s", "genre": "Rock", "key": "A"},
        {"title": "Shallow", "artist": "Lady Gaga", "era": "2010s", "genre": "Pop", "key": "G"},
        {"title": "Rock and Roll", "artist": "Joan Jett", "era": "80s", "genre": "Rock"},
        {"title": "Immigrant Song", "artist": "Led Zeppelin", "era": "70s", "genre": "Rock", "key": "F#m"},
        {"title": "Respect", "artist": "Aretha Franklin", "era": "60s", "genre": "Rock", "key": "C"},
        {"title": "Cannonball", "artist": "The Breeders", "era": "90s", "genre": "Rock", "key": "E"},
        {"title": "I Kissed a Girl", "artist": "Katy Perry", "era": "2000s", "genre": "Pop", "key": "C#"},
        {"title": "I Want You to Want Me", "artist": "Letters to Cleo", "era": "90s", "genre": "Rock", "key": "A"},
        {"title": "I'm So Excited", "artist": "The Pointer Sisters", "era": "80s", "genre": "Pop", "key": "F"},
        {"title": "Your Love", "artist": "The Outfield", "era": "80s", "genre": "Rock", "key": "A"},
        {"title": "Since U Been Gone", "artist": "Kelly Clarkson", "era": "2000s", "genre": "Pop", "key": "G"},
        {"title": "I Hate Myself for Loving You", "artist": "Joan Jett", "era": "80s", "genre": "Rock", "key": "A"},
        {"title": "Just a Girl", "artist": "No Doubt", "era": "90s", "genre": "Rock", "key": "D"},
        {"title": "Any Way You Want It", "artist": "Journey", "era": "80s", "genre": "Rock", "key": "D"},
        {"title": "Rolling in the Deep", "artist": "Adele", "era": "2010s", "genre": "Pop", "key": "Cm"},
        {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "era": "90s", "genre": "Rock", "key": "F"},
        {"title": "Proud Mary", "artist": "Tina Turner", "era": "70s", "genre": "Rock", "key": "D"},
        {"title": "Go Your Own Way", "artist": "Fleetwood Mac", "era": "70s", "genre": "Rock", "key": "F"},
        {"title": "Knock on Wood", "artist": "Amii Stewart", "era": "70s", "genre": "Pop", "key": "Am"},
        {"title": "Dangerous Woman", "artist": "Ariana Grande", "era": "2010s", "genre": "Pop", "key": "E"},
        {"title": "Halo", "artist": "Beyonce", "era": "2000s", "genre": "Pop", "key": "Ab"},
        {"title": "Hash Pipe", "artist": "Weezer", "era": "2000s", "genre": "Rock", "key": "G#"},
        {"title": "You're No Good", "artist": "Linda Ronstadt", "era": "70s", "genre": "Rock", "key": "Am"},
        {"title": "good 4 u", "artist": "Olivia Rodrigo", "era": "2020s", "genre": "Pop", "key": "Ab"},
        {"title": "Fat Lip", "artist": "Sum 41", "era": "2000s", "genre": "Rock", "key": "F"},
        {"title": "The Middle", "artist": "Jimmy Eat World", "era": "2000s", "genre": "Rock", "key": "C"},
        {"title": "Zombie", "artist": "The Cranberries", "era": "90s", "genre": "Rock", "key": "Em"},
        {"title": "ABCDEFU", "artist": "Gayle", "era": "2020s", "genre": "Pop", "key": "G"},
        {"title": "The Best", "artist": "Tina Turner", "era": "80s", "genre": "Rock", "key": "C"},
        {"title": "Man! I Feel Like a Woman", "artist": "Shania Twain", "era": "90s", "genre": "Pop", "key": "Eb"},
        {"title": "I Believe in a Thing Called Love", "artist": "The Darkness", "era": "2000s", "genre": "Rock", "key": "E"},
        {"title": "Sk8er Boi", "artist": "Avril Lavigne", "era": "2000s", "genre": "Rock", "key": "D"},
        {"title": "Self Esteem", "artist": "The Offspring", "era": "90s", "genre": "Rock", "key": "F#"},
        {"title": "Party in the USA", "artist": "Miley Cyrus", "era": "2000s", "genre": "Pop", "key": "Bb"},
        {"title": "More Than a Feeling", "artist": "Boston", "era": "70s", "genre": "Rock", "key": "D"},
        {"title": "The Anthem", "artist": "Good Charlotte", "era": "2000s", "genre": "Rock", "key": "E"},
        {"title": "I Wanna Dance with Somebody", "artist": "Whitney Houston", "era": "80s", "genre": "Pop", "key": "F"},
        {"title": "My Own Worst Enemy", "artist": "Lit", "era": "90s", "genre": "Rock", "key": "Eb"},
        {"title": "What's Up", "artist": "4 Non Blondes", "era": "90s", "genre": "Rock", "key": "A"},
        {"title": "Flowers", "artist": "Miley Cyrus", "era": "2020s", "genre": "Pop", "key": "G"},
        {"title": "Killing in the Name", "artist": "Rage Against the Machine", "era": "90s", "genre": "Rock", "key": "Dm"},
        {"title": "All the Small Things", "artist": "blink-182", "era": "90s", "genre": "Rock", "key": "C"},
        {"title": "Vampire", "artist": "Olivia Rodrigo", "era": "2020s", "genre": "Pop", "key": "Bb"},
        {"title": "Crazy", "artist": "Aerosmith", "era": "90s", "genre": "Rock", "key": "A"},
        {"title": "You Belong with Me", "artist": "Taylor Swift", "era": "2000s", "genre": "Pop", "key": "G"},
        {"title": "Give It Away", "artist": "Red Hot Chili Peppers", "era": "90s", "genre": "Rock", "key": "A"},
        {"title": "Whenever, Wherever", "artist": "Shakira", "era": "2000s", "genre": "Pop", "key": "C#m"},
        {"title": "Everlong", "artist": "Foo Fighters", "era": "90s", "genre": "Rock", "key": "D"},
        {"title": "Love Shack", "artist": "The B-52's", "era": "80s", "genre": "Pop", "key": "D"},
        {"title": "Better Man", "artist": "Pearl Jam", "era": "90s", "genre": "Rock", "key": "D"},
        {"title": "Basket Case", "artist": "Green Day", "era": "90s", "genre": "Rock", "key": "Eb"},
    ]

            for song_data in starter_songs:
                song = Song(
                    title=song_data["title"],
                    artist=song_data["artist"],
                    genre=song_data["genre"],
                    era=song_data["era"],
                    key=song_data.get("key"),  # Some songs don't have keys yet
                    frequency_weight=50.0,
                    first_set_only=False,
                    second_set_only=False,
                    potential_starting_song=False,
                    potential_final_song=False,
                    lead_vocals='Lauren'  # Default to Lauren
                )
                db.session.add(song)

            db.session.commit()
            print("✓ Starter songs loaded successfully!")
            print("   TIP: After editing songs, set SKIP_STARTER_DATA=true in Render to preserve changes")
        elif skip_starter and song_count == 0:
            print("⚠ Database is empty but SKIP_STARTER_DATA is set - no songs loaded")
        else:
            print(f"✓ Database has {song_count} songs")

    return app

# Create app instance for Gunicorn
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
