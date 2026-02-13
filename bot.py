# This bot is developed by **RETOUCH**
import asyncio
from hydrogram import Client
from info import BOT_TOKEN, API_ID, API_HASH
from web import web_server
from utils.logger import setup_logger, logger
from aiohttp import web as aio_web

setup_logger()

class RetouchBot(Client):
    def __init__(self):
        super().__init__(
            name="Retouch",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins")
        )

    async def start(self):
        await super().start()
        logger.info("--- RETOUCH CORE V15.0 ONLINE ---")
        
        # Start the "Stay Alive" Web Server for Render/Koyeb
        app = aio_web.AppRunner(await web_server())
        await app.setup()
        site = aio_web.TCPSite(app, "0.0.0.0", 8080)
        await site.start()
        logger.info("WEB_SERVER: RUNNING ON PORT 8080")

    async def stop(self, *args):
        await super().stop()
        logger.info("RETOUCH CORE SHUTTING DOWN...")

if __name__ == "__main__":
    RetouchBot().run()
