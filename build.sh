#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo "=== Creating staticfiles directory ==="
mkdir -p staticfiles

echo "=== Collecting static files ==="
python manage.py collectstatic --no-input --clear --verbosity 2

echo "=== Checking database connection ==="
python manage.py check --database default

echo "=== Running migrations ==="
python manage.py migrate --verbosity 2

echo "=== Listing migrations ==="
python manage.py showmigrations

echo "=== Build completed successfully! ==="
