# 🎸 Pink Lightning Set List Generator

A web-based application for managing and generating intelligent setlists for the Pink Lightning cover band. Built with Flask and designed for deployment on Render.com's free tier.

## ✨ Features

- **Song Management**: Add, edit, and delete songs with detailed attributes
- **Bulk Import**: Add multiple songs at once using a simple pipe-delimited format
- **Smart Setlist Generation**: 
  - Generate 1-3 sets with custom song counts per set
  - Respects set-specific constraints (First Set Only, Second Set Only)
  - Intelligently selects starting and ending songs
  - Uses frequency weights to control song rotation
- **User Authentication**: Secure login system
- **Beautiful UI**: Eye-friendly pink and black theme
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Print-Friendly**: Generated setlists can be printed for performances

## 🎵 Song Attributes

Each song includes:
- **Basic Info**: Title, Artist, Key, Genre, Era, Lead Vocals
- **Set Placement Rules**:
  - First Set Only
  - Second Set Only
  - Potential Starting Song
  - Potential Final Song
- **Frequency Weight**: 0-100% (controls how often song appears in setlists)

## 🚀 Local Development Setup

### Prerequisites
- Python 3.11+
- pip

### Installation

1. **Clone or download the repository**

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
	 ```bash
	 venv\Scripts\activate
	 ```
   - Mac/Linux:
	 ```bash
	 source venv/bin/activate
	 ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

7. **Login with default credentials**:
   - Username: `pinklightning`
   - Password: `gottohave100`

## 🌐 Deploying to Render.com (Free)

### Option 1: Using render.yaml (Recommended)

1. **Push your code to GitHub**

2. **Go to [Render.com](https://render.com)** and sign up/login

3. **Click "New +" → "Blueprint"**

4. **Connect your GitHub repository**

5. **Render will automatically detect `render.yaml`** and create:
   - Web Service (Flask app)
   - PostgreSQL Database
   - Environment variables

6. **Click "Apply"** and wait for deployment

7. **Your app will be live** at: `https://pink-lightning-setlist.onrender.com`

### Option 2: Manual Setup

1. **Create PostgreSQL Database**:
   - Go to Render Dashboard
   - Click "New +" → "PostgreSQL"
   - Choose Free plan
   - Note the connection string

2. **Create Web Service**:
   - Click "New +" → "Web Service"
   - Connect your repository
   - Settings:
	 - Name: `pink-lightning-setlist`
	 - Runtime: `Python 3`
	 - Build Command: `pip install -r requirements.txt`
	 - Start Command: `gunicorn app:app`
	 - Plan: `Free`

3. **Add Environment Variables**:
   - `SECRET_KEY`: Generate a random string
   - `DATABASE_URL`: Paste PostgreSQL connection string from step 1

4. **Deploy** and wait for build to complete

### Important Notes for Free Tier

- **Spin-down**: The app will sleep after 15 minutes of inactivity
- **First load**: May take 30-60 seconds after sleeping
- **Database**: PostgreSQL free tier expires after 90 days (you'll need to create a new one)

## 📖 How to Use

### Adding Songs

**Single Song**:
1. Click "Add Songs" → "Add Single Song"
2. Fill in the song details
3. Set frequency weight (higher % = more likely to appear)
4. Check any applicable set placement rules
5. Click "Add Song"

**Multiple Songs**:
1. Click "Add Songs" → "Add Multiple Songs"
2. Enter songs in format: `Title | Artist | Key | Genre | Era | Lead Vocals | Frequency`
3. Example:
   ```
   Sweet Home Alabama | Lynyrd Skynyrd | D | Rock | 70s | John | 80
   Hotel California | Eagles | Bm | Rock | 70s | Sarah | 75
   ```
4. Click "Add Songs"

### Generating Setlists

1. Click "Generate Setlist"
2. Select number of sets (1, 2, or 3)
3. Enter desired songs per set
4. Click "Generate Setlist"
5. Review the generated setlist
6. Print or regenerate as needed

### Managing Songs

- **View All Songs**: Click "Songs" in navigation
- **Edit Song**: Click pencil icon next to song
- **Delete Song**: Click trash icon (confirms before deleting)

## 🎨 Customization

### Changing Colors

Edit `static/css/style.css` and modify the CSS variables:
```css
:root {
	--primary-pink: #ff69b4;
	--light-pink: #ffb6d9;
	--dark-pink: #ff1493;
	--primary-black: #1a1a1a;
	--soft-black: #2d2d2d;
}
```

### Changing Default User

Edit `app.py` in the `create_app()` function:
```python
default_user = User(username='yournewusername')
default_user.set_password('yournewpassword')
```

## 🔧 Tech Stack

- **Backend**: Flask 3.0
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: Flask-Login
- **ORM**: SQLAlchemy
- **Frontend**: Bootstrap 5, Jinja2 templates
- **Deployment**: Gunicorn, Render.com
- **Architecture**: Application factory pattern with blueprints

## 📝 Database Schema

### User Table
- id (Primary Key)
- username (Unique)
- password_hash
- created_at

### Song Table
- id (Primary Key)
- title
- artist
- key
- genre
- era
- lead_vocals
- first_set_only (Boolean)
- second_set_only (Boolean)
- potential_starting_song (Boolean)
- potential_final_song (Boolean)
- frequency_weight (Float, 0-100)
- created_at
- updated_at

## 🎯 Algorithm Details

The setlist generator:

1. **Validates** song count availability
2. **Filters** songs based on set constraints
3. **Selects** starting songs from designated candidates
4. **Selects** ending songs from designated candidates
5. **Fills** middle positions using weighted random selection
6. **Avoids** repetition across sets
7. **Provides warnings** if constraints can't be met

## 🤝 Contributing

Feel free to fork, modify, and customize this application for your band's needs!

## 📄 License

This project is open source and available for personal use.

## 🎤 About Pink Lightning

Pink Lightning is a cover band that rocks the stage with 3-hour performances. This tool helps them craft the perfect setlist every time! ⚡

---

**Made with 💗 and ⚡ for Pink Lightning**
