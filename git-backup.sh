#!/bin/bash
# Git backup script for BAS12

APP_DIR=/srv/bas12
cd $APP_DIR || exit

echo "💾 Starter git-backup for BAS12..."

# Legg til alle endringer
git add -A

# Lag commit med timestamp
git commit -m "Backup: $(date '+%Y-%m-%d %H:%M:%S')"

# Hvis remote finnes, pushe til den
if git remote | grep -q origin; then
    echo "🌐 Pusher til origin..."
    git push origin main || git push origin master
else
    echo "⚠️ Ingen remote satt. Endringer er kun lagret lokalt."
fi

echo "✅ Git-backup ferdig!"
