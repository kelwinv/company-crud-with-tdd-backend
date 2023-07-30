"""env config"""
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME", "your_database_name")
DATABASE_USER = os.getenv("DATABASE_USER", "your_username")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "your_password")
DATABASE_HOST = os.getenv("DATABASE_HOST", "your_host")
DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
DATABASE_SCHEMA = os.getenv("DATABASE_SCHEMA", "public")

PORT = os.getenv("PORT", "3333")
HOST = os.getenv("HOST", "0.0.0.0")

DATABASE_CONFIG = {
    "database": DATABASE_NAME,
    "user": DATABASE_USER,
    "password": DATABASE_PASSWORD,
    "host": DATABASE_HOST,
    "port": DATABASE_PORT,
    "schema": DATABASE_SCHEMA,
}

SERVER_CONFIG = {
    'port': PORT,
    'host': HOST
}
