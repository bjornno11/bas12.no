#!/bin/bash
set -e

echo "🚀 Starter deploy for BAS12..."

# 1. Sjekk kode og templates
echo "🧪 Kjører checks..."
source venv/bin/activate
python manage.py check --deploy
python manage.py validate_templates

# 2. Migrasjoner
echo "🗄️ Kjører migrasjoner..."
python manage.py migrate --noinput

# 3. Collect static
echo "🎨 Samler static files..."
python manage.py collectstatic --noinput

# 4. Restart Gunicorn
echo "🔄 Restarter Gunicorn..."
sudo systemctl restart bas12.service

echo "✅ Deploy fullført!"
