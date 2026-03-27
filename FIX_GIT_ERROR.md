# Quick Fix for Git Merge Error

## ❌ Error You're Seeing:

```
error: The following untracked working tree files would be overwritten by merge:
  .gitignore
  tracker/templates/tracker/sw.js
Please move or remove them before you merge.
Aborting
```

## ✅ Quick Fix (Choose One):

### Option 1: Safe Method (Recommended)

Run these commands one by one:

```bash
# Step 1: Backup your files (if you have local changes)
copy .gitignore .gitignore.backup
copy tracker\templates\tracker\sw.js tracker\templates\tracker\sw.js.backup

# Step 2: Remove the conflicting files
del .gitignore
del tracker\templates\tracker\sw.js

# Step 3: Pull the latest code
git pull origin main
```

### Option 2: Force Update (If you don't care about local changes)

```bash
git fetch origin
git reset --hard origin/main
```

### Option 3: Stash and Pull

```bash
git stash
git pull origin main
```

---

## 🔍 Why This Happens:

You have local files (`.gitignore` and `sw.js`) that aren't tracked by git, but the repository now has these files. Git won't overwrite your local files automatically.

---

## ✅ After Fixing:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Start server:
```bash
python manage.py runserver
```

---

## 📝 To Prevent This in Future:

Always pull before making changes:
```bash
git pull origin main
```

---

That's it! Your code should now be up to date. 🎉
