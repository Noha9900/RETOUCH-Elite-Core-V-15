# This bot is developed by **RETOUCH**
import os
from aiohttp import web
from utils.logger import logger

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("RETOUCH_SYSTEM_STATUS: ONLINE_200")

async def web_server():
    server = web.Application()
    server.add_routes(routes)
    return server

# GLOBAL PORT LOGIC
# 1. Checks if the platform assigned a 'PORT' environment variable.
# 2. Defaults to 8080 for VPS or Local deployment.
PORT = int(os.environ.get("PORT", 8080))
