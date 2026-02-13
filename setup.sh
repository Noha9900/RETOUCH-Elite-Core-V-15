#!/bin/bash
# This bot is developed by **RETOUCH**

echo "🚀 INITIALIZING RETOUCH ELITE DEPLOYMENT..."

# Update System
sudo apt-get update && sudo apt-get upgrade -y

# Install Docker if not present
if ! [ -x "$(command -v docker)" ]; then
  echo "📦 Installing Docker..."
  curl -fsSL https://get.docker.com -o get-docker.sh
  sh get-docker.sh
fi

# Build and Run
echo "⚡ Building RETOUCH Containers..."
sudo docker build -t retouch-bot .
sudo docker run -d --name retouch-engine --restart always retouch-bot

echo "✅ SYSTEM ACTIVE. CHECK LOGS WITH: sudo docker logs -f retouch-engine"
