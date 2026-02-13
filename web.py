# This bot is developed by **RETOUCH**
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("RETOUCH_CORE_V15_ACTIVE")

async def web_server():
    server = web.Application()
    server.add_routes(routes)
    return server
