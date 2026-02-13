#!/bin/bash
# This bot is developed by **RETOUCH**

echo "🚀 INITIALIZING RETOUCH ELITE INSTALLATION..."
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv -y

echo "📦 SETTING UP VIRTUAL ENVIRONMENT..."
python3 -m venv venv
source venv/bin/activate

echo "⚡ INSTALLING DEPENDENCIES..."
pip install -r requirements.txt

echo "✅ SETUP COMPLETE. RUN 'python3 bot.py' TO START."
