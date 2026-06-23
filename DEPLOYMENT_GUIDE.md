# Pink Lightning Deployment Guide

## Protecting Your Production Data

### The Problem
When you make manual changes to songs on the live site (changing keys, adding singers, etc.), you need to ensure those changes aren't lost when you redeploy the app with code updates.

### The Solution
The app uses an environment variable `SKIP_STARTER_DATA` to control whether starter songs are loaded.

## Steps for Production

### 1. Initial Deploy (First Time Only)
- Deploy the app to Render
- The app will automatically load 72 starter songs
- Login and verify the songs are there

### 2. After Making Manual Changes
Once you've edited songs on the live site, protect your changes:

**In Render Dashboard:**
1. Go to your web service
2. Click "Environment" in the left sidebar
3. Click "Add Environment Variable"
4. Add:
   - **Key:** `SKIP_STARTER_DATA`
   - **Value:** `true`
5. Click "Save Changes"

This tells the app: "Don't reload starter data, even if the database is empty"

### 3. Future Code Updates
Now when you push code changes to GitHub:
- Render will redeploy automatically
- Your database and manual song edits are preserved
- Starter data won't reload

## Important Notes

### Database Persistence
- **Render Free Tier:** PostgreSQL database persists across deploys ✅
- **Manual Changes:** Safe as long as database isn't deleted ✅
- **Code Changes:** Won't affect database ✅

### When Data Could Be Lost
- If you delete and recreate the Render service
- If Render's PostgreSQL database is deleted
- If you manually clear the database

### Emergency: Reloading Starter Data
If you need to reload the starter songs:

1. In Render, remove or set `SKIP_STARTER_DATA` to `false`
2. **Delete all songs** via the app UI or manually clear the songs table
3. Redeploy or restart the service
4. Starter songs will reload
5. **Remember to set `SKIP_STARTER_DATA=true` again** to protect future changes

## Database Backups

Render provides **daily automatic backups** for PostgreSQL:
- Go to your database in Render dashboard
- Click "Backups" tab
- Can restore from any daily backup

### Manual Backup (Recommended)
Periodically export your songs:
1. Use the song library view
2. Copy data to a spreadsheet
3. Or add a CSV export feature to the app

## Workflow Summary

```
Initial Deploy
	↓
Songs Load Automatically (72 songs)
	↓
Login & Make Manual Changes (keys, singers, etc.)
	↓
Set SKIP_STARTER_DATA=true in Render
	↓
Push Code Updates Anytime
	↓
Manual Changes Preserved ✅
```

## Questions?

- **Will my songs be lost when I update code?** No, if you set `SKIP_STARTER_DATA=true`
- **Can I add new songs via the UI?** Yes! All UI changes persist
- **What if I delete a song accidentally?** Use Render's daily backup to restore
- **Can I edit the starter data?** Yes, but changes only apply to fresh installs

---

**Current Status:** The app is now configured to respect the `SKIP_STARTER_DATA` environment variable. Set it to `true` in Render after your first successful deploy.
