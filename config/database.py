import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from colorama import Fore, Style, init

load_dotenv() # Cargamos variables de entorno

MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DATABASE_NAME")

client = AsyncIOMotorClient(MONGO_URI)
database  = client[DB_NAME]


async def ping_database():
    try:
        await client.admin.command('ping')
        print(Fore.GREEN + "✅ Successfully connected to MongoDB Atlas!")
    except Exception as e:
        print(Fore.RED + f"❌ Failed to connect to MongoDB: {e}")

materials_collection = database.materials
trucks_collection = database.trucks
drivers_collection = database.drivers
landfills_collection = database.landfills
users_collection = database.users
routes_collection = database.routes

sparetruckinfos_collection = database.sparetruckinfo
downtimes_collection = database.downtime
loads_collection = database.load
notes_collection = database.notes

coversheets_collection = database.coversheets
