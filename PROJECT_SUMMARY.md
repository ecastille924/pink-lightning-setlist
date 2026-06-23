# Pink Lightning Set List Generator - Project Summary

## 🎯 Project Overview

A complete web application for managing and generating intelligent setlists for the Pink Lightning cover band. The app helps create optimized 3-hour performance setlists using rule-based algorithms and frequency weighting.

## 📁 Project Structure

```
C:\Scripts\
├── app.py                      # Flask application factory
├── extensions.py               # SQLAlchemy and Flask-Login initialization
├── models.py                   # User and Song database models
├── auth.py                     # Authentication blueprint (login/logout)
├── routes.py                   # Main routes (songs, setlist generation)
├── setlist_generator.py        # Setlist generation algorithm
├── init_db.py                  # Database initialization script
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version for deployment
├── Procfile                    # Process configuration for deployment
├── render.yaml                 # Render.com deployment config
├── .gitignore                  # Git ignore rules
├── start.bat                   # Windows quick start script
├── start.ps1                   # PowerShell quick start script
├── README.md                   # Full documentation
├── templates/                  # Jinja2 HTML templates
│   ├── base.html              # Base template with navigation
│   ├── login.html             # Login page
│   ├── songs.html             # Song list page
│   ├── add_song.html          # Single song form
│   ├── add_multiple_songs.html # Bulk import form
│   ├── edit_song.html         # Edit song form
│   ├── generate.html          # Setlist generation form
│   └── setlist_result.html    # Generated setlist display
├── static/
│   └── css/
│       └── style.css          # Pink/black custom theme
└── venv/                      # Virtual environment (generated)
```

## 🎨 Design Patterns Used

1. **Application Factory Pattern** - `create_app()` for flexible configuration
2. **Blueprint Pattern** - Separate blueprints for auth and main routes
3. **Extension Pattern** - Centralized extension initialization in `extensions.py`
4. **Template Inheritance** - Base template with blocks for content
5. **Repository Pattern** - SQLAlchemy models as data access layer

## 🔧 Technology Stack

### Backend
- **Flask 3.0** - Web framework
- **Flask-SQLAlchemy** - ORM
- **Flask-Login** - User session management
- **Werkzeug** - Password hashing
- **psycopg2-binary** - PostgreSQL adapter
- **Gunicorn** - Production WSGI server

### Frontend
- **Bootstrap 5** - Responsive framework
- **Bootstrap Icons** - Icon library
- **Jinja2** - Template engine
- **Custom CSS** - Pink/black theme

### Database
- **SQLite** - Development database
- **PostgreSQL** - Production database (Render.com)

## 📊 Database Schema

### User Model
```python
- id (Integer, Primary Key)
- username (String, Unique, Not Null)
- password_hash (String, Not Null)
- created_at (DateTime)
```

### Song Model
```python
- id (Integer, Primary Key)
- title (String, Not Null)
- artist (String, Not Null)
- key (String)
- genre (String)
- era (String)
- lead_vocals (String)
- first_set_only (Boolean)
- second_set_only (Boolean)
- potential_starting_song (Boolean)
- potential_final_song (Boolean)
- frequency_weight (Float, 0-100)
- created_at (DateTime)
- updated_at (DateTime)
```

## 🎵 Setlist Generation Algorithm

The algorithm in `setlist_generator.py` follows these steps:

1. **Validation**: Check if enough songs exist for requested setlist
2. **Filtering**: Apply set-specific constraints (first/second set only)
3. **Starting Song Selection**: Choose from designated starting songs using weighted random
4. **Ending Song Selection**: Choose from designated ending songs using weighted random
5. **Middle Songs**: Fill remaining slots with weighted random selection
6. **Frequency Weighting**: Higher % = more likely to be selected
7. **No Repetition**: Each song appears only once across all sets
8. **Warnings**: Provide feedback if constraints can't be met

## 🔐 Security Features

- Password hashing using Werkzeug's `generate_password_hash`
- Session-based authentication via Flask-Login
- CSRF protection via Flask's built-in features
- Login required decorators on protected routes
- Secure secret key configuration

## 🚀 Deployment Options

### Local Development
```bash
python start.ps1   # PowerShell
start.bat          # Command Prompt
```

### Render.com (Free Tier)
1. Push to GitHub
2. Connect repository in Render.com
3. Deploy using `render.yaml` (auto-configured)
4. PostgreSQL database included
5. Auto-deployment on git push

## 🎯 Key Features Implemented

✅ User authentication with default user  
✅ Song CRUD operations (Create, Read, Update, Delete)  
✅ Bulk song import via pipe-delimited format  
✅ Song attributes: Title, Artist, Key, Genre, Era, Lead Vocals  
✅ Set placement rules (checkboxes)  
✅ Frequency weight system (0-100%)  
✅ Intelligent setlist generation (1-3 sets)  
✅ Configurable songs per set  
✅ Validation warnings  
✅ Print-friendly setlist output  
✅ Responsive pink/black theme  
✅ Flash messages for user feedback  

## 📝 Configuration

### Environment Variables
- `SECRET_KEY` - Flask secret key (auto-generated on Render)
- `DATABASE_URL` - Database connection string
- `PORT` - Server port (default: 5000)

### Default Credentials
- **Username**: `pinklightning`
- **Password**: `gottohave100`

## 🔄 Typical Workflow

1. **Start App** → Run `start.ps1` or `python app.py`
2. **Login** → Use default credentials
3. **Add Songs** → Single or bulk import
4. **Set Attributes** → Configure frequency, set rules
5. **Generate Setlist** → Choose sets and song counts
6. **Review** → Check generated setlist
7. **Print/Export** → Use browser print function

## 🐛 Common Issues & Solutions

### Issue: Python not found
**Solution**: Install Python 3.11+ and restart terminal

### Issue: Module not found
**Solution**: Run `pip install -r requirements.txt` in venv

### Issue: Database not initialized
**Solution**: Run `python init_db.py`

### Issue: Port 5000 in use
**Solution**: Set `PORT` environment variable or kill existing process

## 📈 Future Enhancement Ideas

- Export setlists to PDF/Excel
- Song duration tracking and automatic set length calculation
- BPM (tempo) tracking and flow optimization
- Mood/energy level tracking
- Multiple user accounts with band member roles
- Setlist history and favorites
- Statistics and analytics
- Integration with Spotify/Apple Music
- Mobile app version
- Collaborative editing

## 👥 Credits

Built for **Pink Lightning** cover band  
Powered by Flask, SQLAlchemy, and Bootstrap  
Deployed on Render.com

---

**Made with 💗 and ⚡ for Pink Lightning**
