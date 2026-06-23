# Production Vocalist Update Guide

## What Changed

### New Features:
1. **"Both" option added** for duets (Lauren + Erick together)
2. **Default vocalist is now "Lauren"** for all new songs
3. **All existing songs** without a vocalist are set to "Lauren"

### UI Changes:
- Add/Edit song forms now have three options:
  - Lauren
  - Erick  
  - Both (Duet)
- Song library displays "Both" as **L** **E** badges side-by-side
- "Lauren" is pre-selected when adding new songs

## Updating Production Database

Your **local database** has been updated - all 72 songs now have Lauren as the lead vocalist.

### For the Live Site (Render):

Since your production database was created before this update, you need to run the migration script once:

#### Option 1: Via Render Shell (Recommended)
1. Go to your Render dashboard
2. Select your web service
3. Click **Shell** in the top menu
4. Run:
   ```bash
   python set_default_vocalists.py
   ```
5. You should see output confirming all songs were updated to Lauren

#### Option 2: Manual Update
- Login to your live site
- Edit each song individually and set the vocalist

#### Option 3: Wait for Natural Update
- The code now defaults to "Lauren" for all new songs
- Future starter data loads will include "Lauren" as default
- Existing songs will remain without vocalist until manually edited

## Verification

After running the migration:
- Visit your song library
- All songs should show a pink **L** badge in the Lead Vocals column
- No songs should show "-" (none)

## Future Behavior

From now on:
- ✅ New songs default to "Lauren"
- ✅ "Both" option available for duets
- ✅ Starter songs load with "Lauren" as default
- ✅ Forms pre-select "Lauren" for convenience

---

**Note:** The production migration only needs to run **once**. After that, the default vocalist handling is automatic.
