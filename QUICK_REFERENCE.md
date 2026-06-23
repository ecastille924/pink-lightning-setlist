# Pink Lightning Set List Generator - Quick Reference

## 🚀 Quick Start

### First Time Setup
```powershell
# Option 1: Use quick start script (recommended)
.\start.ps1

# Option 2: Manual setup
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python init_db.py
python app.py
```

### Subsequent Runs
```powershell
.\start.ps1
# OR
.\venv\Scripts\Activate.ps1
python app.py
```

## 🔐 Access

- **URL**: http://localhost:5000
- **Username**: `pinklightning`
- **Password**: `gottohave100`

## 🎵 Adding Songs

### Single Song
1. Click **"Add Songs" → "Add Single Song"**
2. Fill in required fields (Title, Artist)
3. Optional: Key, Genre, Era, Lead Vocals
4. Set **Frequency Weight** (0-100%, default 50%)
5. Check applicable options:
   - ☑ First Set Only
   - ☑ Second Set Only  
   - ☑ Potential Starting Song
   - ☑ Potential Final Song
6. Click **"Add Song"**

### Multiple Songs (Bulk Import)
1. Click **"Add Songs" → "Add Multiple Songs"**
2. Enter songs in format:
   ```
   Title | Artist | Key | Genre | Era | Lead Vocals | Frequency Weight
   ```
3. Example:
   ```
   Sweet Home Alabama | Lynyrd Skynyrd | D | Rock | 70s | John | 80
   Hotel California | Eagles | Bm | Rock | 70s | Sarah | 75
   Don't Stop Believin' | Journey | E | Rock | 80s | Mike | 90
   ```
4. Click **"Add Songs"**

## 🎸 Generating Setlists

1. Click **"Generate Setlist"** in navigation
2. Select number of sets:
   - ⭕ One Set
   - ⭕ Two Sets (default)
   - ⭕ Three Sets
3. Enter songs per set (e.g., 15 songs per set)
4. Click **"Generate Setlist"**
5. Review generated setlist
6. Click **"Print"** to print or **"Generate Another"** to try again

## 📊 Song Management

### View All Songs
- Click **"Songs"** in navigation
- Shows all songs with attributes
- Displays badges for special roles (Start, Final, Set-specific)

### Edit Song
1. Click **pencil icon** (✏️) next to song
2. Modify any fields
3. Click **"Save Changes"**

### Delete Song
1. Click **trash icon** (🗑️) next to song
2. Confirm deletion
3. Song removed from database

## 🎯 Frequency Weight Guide

- **90-100%**: Songs played every show (crowd favorites)
- **70-89%**: Frequently played songs
- **50-69%**: Regular rotation songs (default)
- **30-49%**: Occasional songs
- **10-29%**: Rare songs (special occasions)
- **1-9%**: Rarely played (deep cuts)

## 🎭 Set Placement Rules

### First Set Only
- Song will only appear in Set 1
- Good for: Warm-up songs, crowd pleasers

### Second Set Only
- Song will only appear in Set 2 or later
- Good for: High-energy closers, encores

### Potential Starting Song
- Can be selected as first song in any set
- Good for: Strong openers, attention grabbers

### Potential Final Song
- Can be selected as last song in any set
- Good for: Powerful closers, crowd sing-alongs

## ⚡ Tips & Best Practices

1. **Start with high-frequency songs** (70-100%) for your core setlist
2. **Mark 3-5 songs** as potential starting songs
3. **Mark 3-5 songs** as potential final songs
4. **Balance set constraints** - don't over-constrain or generation may fail
5. **Keep at least 2x songs** vs setlist length (e.g., 60 songs for 30-song setlist)
6. **Test generation** with different song counts to find optimal balance
7. **Update frequencies** after each show based on crowd response

## 🔧 Troubleshooting

### Not enough songs warning
- Add more songs to database
- Reduce songs per set
- Remove some set-specific constraints

### No starting/ending songs selected
- Algorithm will randomly select from available songs
- Mark some songs as starting/ending for better results

### Same songs appearing frequently
- Adjust frequency weights
- Add more songs with similar weights

### Can't login
- Check username: `pinklightning` (all lowercase)
- Check password: `gottohave100`
- Run `python init_db.py` if user doesn't exist

## 📝 File Locations

- **Database**: `C:\Scripts\pinklightning.db`
- **Virtual Environment**: `C:\Scripts\venv\`
- **Templates**: `C:\Scripts\templates\`
- **Styles**: `C:\Scripts\static\css\style.css`

## 🔄 Updating the App

```powershell
# Stop the server (CTRL+C)
# Pull latest changes (if using git)
git pull

# Activate venv and update dependencies
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt --upgrade

# Restart
python app.py
```

## 🆘 Getting Help

1. Check `README.md` for detailed documentation
2. Check `PROJECT_SUMMARY.md` for technical details
3. Review error messages in terminal
4. Check Flask debug page in browser (development mode)

---

**Quick Access**: Bookmark http://localhost:5000 for fast access! ⚡
