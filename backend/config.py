import os
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client, Client

current_file = Path(__file__).resolve()
root_dir = current_file.parent.parent 
env_path = root_dir / '.env'

# 'override=True' forces Python to re-read the file even if it thinks it already did
load_dotenv(dotenv_path=env_path, override=True)

class Config:
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
    SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print(f"--- Environment Check ---")
print(f"Reading from: {env_path}")
# This will show us if the key is actually empty or just not found
print(f"GROQ_API_KEY: {'✅ Found' if Config.GROQ_API_KEY else '❌ MISSING'}")
print(f"SUPABASE_URL: {'✅ Found' if Config.SUPABASE_URL else '❌ MISSING'}")
print(f"-------------------------\n")

supabase = None
supabase_admin = None

if Config.SUPABASE_URL and Config.SUPABASE_ANON_KEY:
    supabase = create_client(Config.SUPABASE_URL, Config.SUPABASE_ANON_KEY)
if Config.SUPABASE_URL and Config.SUPABASE_SERVICE_ROLE_KEY:
    supabase_admin = create_client(Config.SUPABASE_URL, Config.SUPABASE_SERVICE_ROLE_KEY)