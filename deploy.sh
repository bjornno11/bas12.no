#!/bin/bash
# Deploy script for BAS12

APP_DIR=/srv/bas12
VENV_DIR=$APP_DIR/venv
SERVICE=bas12

echo "🚀 Starter deploy for BAS12..."

cd $APP_DIR || exit

# Aktiver venv
source $VENV_DIR/bin/activate

# Oppdater dependencies (hvis du bruker requirements.txt)
if [ -f requirements.txt ]; then
    echo "📦 Oppdaterer dependencies..."
    pip install -r requirements.txt
fi

# Kjør migrasjoner
echo "🗄️ Kjører migrasjoner..."
python manage.py migrate --noinput

# Rydd opp og samle static
echo "🎨 Rydder staticfiles og samler på nytt..."
rm -rf $APP_DIR/staticfiles/*
python manage.py collectstatic --noinput

# Restart Gunicorn-service
echo "🔄 Restarter Gunicorn..."
sudo systemctl daemon-reload
sudo systemctl restart $SERVICE

# Status
echo "📊 Status på Gunicorn:"
sudo systemctl status $SERVICE --no-pager -l
