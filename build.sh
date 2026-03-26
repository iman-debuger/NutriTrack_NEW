#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo "=== Creating staticfiles directory ==="
mkdir -p staticfiles

echo "=== Collecting static files ==="
python manage.py collectstatic --no-input --clear --verbosity 2

echo "=== Waiting for database to be ready ==="
sleep 5

echo "=== Running migrations (attempt 1) ==="
python manage.py migrate --verbosity 2 || {
    echo "Migration failed, waiting 10 seconds and retrying..."
    sleep 10
    echo "=== Running migrations (attempt 2) ==="
    python manage.py migrate --verbosity 2
}

echo "=== Listing applied migrations ==="
python manage.py showmigrations

echo "=== Build completed successfully! ==="
