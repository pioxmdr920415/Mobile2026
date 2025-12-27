import asyncio
import os
import asyncpg
from pathlib import Path
from dotenv import load_dotenv

# Load env variables
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

async def list_users():
    database_url = os.environ.get('DATABASE_URL')
    try:
        conn = await asyncpg.connect(database_url)
        users = await conn.fetch('SELECT id, email, full_name, created_at FROM users')
        print(f"Found {len(users)} users:")
        for u in users:
            print(f"- {u['email']} ({u['full_name']})")
        await conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(list_users())
