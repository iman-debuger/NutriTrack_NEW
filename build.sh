#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Create staticfiles directory
mkdir -p staticfiles

# Collect static files with verbose output
echo "Collecting static files..."
python manage.py collectstatic --no-input --clear --verbosity 2

# Run migrations
echo "Running migrations..."
python manage.py migrate

echo "Build completed successfully!"
