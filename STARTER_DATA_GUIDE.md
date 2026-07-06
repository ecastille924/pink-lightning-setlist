# Starter Data Management Guide

## How It Works Now

**Default Behavior (No Environment Variable):**
- App starts up
- Creates database tables if needed
- Uses whatever songs are already in the database
- **Does NOT load or reload starter data**

**Emergency Recovery (Set LOAD_STARTER_DATA=true):**
- App checks for missing starter songs (by title + artist)
- Only adds songs that don't already exist
- Never overwrites existing songs (preserves your edits)
- Useful if database is lost or corrupted

---

## Initial Deploy to Production (With Empty Database)

### Step 1: Deploy with Starter Data Flag
1. In Render dashboard → Environment
2. Add variable:
   - Key: `LOAD_STARTER_DATA`
   - Value: `true`
3. Save and let it deploy
4. Starter songs will be loaded into the database

### Step 2: Remove the Flag
1. After deployment finishes and songs are visible on site
2. Go back to Environment
3. **Delete** the `LOAD_STARTER_DATA` variable
4. Save (Render will redeploy)
5. Songs remain in database, flag is gone

### Step 3: Normal Operation
- All future deploys will use existing database songs
- Starter data code remains as backup but is ignored
- Your edits/additions/deletions persist forever

---

## Future Deploys (Normal Operation)

**Just push code as usual:**
```bash
git add .
git commit -m "Your changes"
git push
```

- NO environment variables needed
- Songs/setlists remain unchanged
- Only code updates

---

## Emergency: Database Lost or Corrupted

If you ever need to reload starter data:

1. **Temporarily set flag:**
   - Render → Environment
   - Add: `LOAD_STARTER_DATA=true`
   - Save

2. **Wait for deploy**
   - Songs will reload
   - Existing songs won't be overwritten

3. **Remove flag:**
   - Delete `LOAD_STARTER_DATA`
   - Save

---

## What's Protected

✅ Song edits (keys, frequencies, vocals, etc.)  
✅ Song additions (new songs you add)  
✅ Song deletions (removed songs stay removed)  
✅ Saved setlists  
✅ All database data persists across code deploys  

---

## Old Environment Variable

`SKIP_STARTER_DATA` is **no longer used**.  
You can delete it if it still exists in Render Environment.

The new approach is "opt-in" instead of "opt-out":
- Old: Data loads by default, set flag to skip
- New: Data never loads, set flag to load

---

## Starter Data Location

The 71 starter songs remain in `app.py` lines 67-138 as a backup reference.
They are dormant code that only runs when explicitly requested.
