# 🚀 RETOUCH ELITE ENGINE v15.0

**The most advanced, command-less Auto-Filter Bot on Telegram (2026 Edition).**
Designed for ultra-fast performance, intelligent search, and seamless monetization.

---

## 💎 Elite Features

* **⚡ Zero-Command Search:** Users simply type the movie name. No commands required.
* **🧠 AI Spelling Engine:** Automatically detects and corrects typos using advanced spell-check logic.
* **🎬 IMDb Integration:** Fetches real-time metadata, years, ratings, and posters.
* **🛡️ Ad-Gate System:** Built-in 30-second timer to monetize your traffic before file delivery.
* **🗑️ Auto-Vanish:** Files and messages automatically delete after 30 minutes for security and storage optimization.
* **🌐 Universal Deployment:** Optimized for VPS, Render, Koyeb, Heroku, and DigitalOcean.
* **🛡️ Security Suite:** Includes Anti-Spam, Link Protection, and Maintenance Mode.

---

## 🏗️ Technical Architecture & Bot Design

The **RETOUCH CORE** is built on a modular "Plugin" architecture to ensure zero latency and high scalability.



### **Folder Structure**
```text
retouch-elite-bot/
├── bot.py                # Main Entry Point (Initializes Web & Client)
├── info.py               # Config, Branding, & UI Design
├── database.py           # MongoDB Connection & 24h Pass Logic
├── web.py                # Health Check Server (Koyeb/Render Support)
├── LICENSE               # MIT Legal Protection
├── utils/                
│   ├── parser.py         # AI Spelling & IMDb Metadata Engine
│   └── logger.py         # Technical Terminal Logging
└── plugins/              
    ├── start.py          # Welcome & Branding
    ├── auto_filter.py    # The Core Search & Ad-Gate Logic
    ├── maintenance.py    # Admin Global Lock
    ├── security.py       # Group Anti-Spam & Link Protector
    └── broadcast.py      # Admin Mass Messaging Engine



    🔄 How It Works
👤 For the User
Direct Search: The user types Avangers (misspelled).

AI Correction: The bot corrects it to Avengers and shows all available versions (IMDb results).

Selection: User clicks on the specific movie version.

Ad-Gate: If the user doesn't have a 24-hour pass, they must wait 30 seconds (Progress bar UI).

Secure Delivery: The file is delivered with a professional technical caption.

Self-Destruct: The file message vanishes in 30 minutes to protect the bot.

👨‍💻 For the Admin
Analytics: Monitor all searches and errors in the LOG_CHANNEL.

Monetization: Force users to join your channel via FSUB_CHANNEL to increase members.

Maintenance: Lock the bot via /maintenance during database updates.

Broadcast: Send an ad or update to thousands of users instantly using /broadcast.

Security: Add the bot to your groups to automatically delete links and ban spammers.

🛠️ Deployment Guide
1. Environment Variables
Create a .env file and fill in your details:

API_ID / API_HASH: From my.telegram.org

BOT_TOKEN: From @BotFather

DATABASE_URI: Your MongoDB connection string

ADMINS: Your Telegram User ID

LOG_CHANNEL: Your private channel ID for logs

2. Launch Commands (VPS)
Bash
pip3 install -r requirements.txt
python3 bot.py
3. Cloud Platforms (Koyeb/Render)
Set the PORT environment variable to 8080 (or 10000 for Render) and set the Health Check Path to /.
