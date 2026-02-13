# This bot is developed by **RETOUCH**
import time
from motor.motor_asyncio import AsyncIOMotorClient
from info import DATABASE_URI, DATABASE_NAME

class Database:
    def __init__(self, uri, name):
        self._client = AsyncIOMotorClient(uri)
        self.db = self._client[name]
        self.users = self.db.users
        self.settings = self.db.settings

    async def get_user(self, user_id):
        user = await self.users.find_one({'id': int(user_id)})
        return user or {}

    async def grant_access(self, user_id):
        expiry = time.time() + 86400
        await self.users.update_one({'id': int(user_id)}, {'$set': {'expiry': expiry}}, upsert=True)

    async def has_access(self, user_id):
        user = await self.get_user(user_id)
        return user.get('expiry', 0) > time.time()

    async def set_config(self, key, value):
        await self.settings.update_one({'key': key}, {'$set': {'value': value}}, upsert=True)

    async def get_config(self, key):
        config = await self.settings.find_one({'key': key})
        return config['value'] if config else None

db = Database(DATABASE_URI, DATABASE_NAME)
