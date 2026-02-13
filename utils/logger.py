# This bot is developed by **RETOUCH**
import logging
import logging.handlers

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s - %(levelname)s] RETOUCH_SYSTEM: %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.StreamHandler(),
            logging.handlers.RotatingFileHandler("retouch.log", maxBytes=5000000, backupCount=5)
        ]
    )
    # Disable noisy logs from other libraries
    logging.getLogger("pyrogram").setLevel(logging.WARNING)
    logging.getLogger("imdbpy").setLevel(logging.WARNING)

logger = logging.getLogger("RETOUCH")
