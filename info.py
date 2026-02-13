# This bot is developed by **RETOUCH**
import os
from dotenv import load_dotenv

load_dotenv()

# API Credentials
API_ID = int(os.getenv('API_ID', '0'))
API_HASH = os.getenv('API_HASH', '')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')

# Database & Logs
DATABASE_URI = os.getenv('DATABASE_URI', '')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'Retouch_Elite')
ADMINS = [int(x) for x in os.getenv('ADMINS', '').split()]
LOG_CHANNEL = int(os.getenv('LOG_CHANNEL', '0'))

# Branding & Technical UI
POWERED_BY = "**SYSTEM POWERED BY RETOUCH 🚀**"
TECH_BANNER = """
**╔════════════════════════╗
  SYSTEM: RETOUCH CORE v15.0
  STATUS: ULTRA-FAST ACTIVE
╚════════════════════════╝**
"""

# Technical Caption Elements
TECH_DESIGN = "△───────────────────△"
CIRC_DESIGN = "○───────────────────○"

# Settings
AUTO_DELETE_TIME = 1800 # 30 Mins
AD_ACCESS_TIME = 86400  # 24 Hours
