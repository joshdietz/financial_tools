import os
import sqlite3
import psycopg2
import dotenv

dotenv.load_dotenv()

def connect_db():
    if os.getenv('DB_DRIVER') == 'sqlite':
        return sqlite3.connect(
            os.getenv('DB_NAME')
        )
    elif os.getenv('DB_DRIVER') == 'postgres':
        return psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
        )