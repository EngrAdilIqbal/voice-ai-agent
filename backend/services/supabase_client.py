# backend/services/supabase_client.py
import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_all_configs():
    try:
        # Make sure to use your correct table name (agent_configs)
        response = supabase.table("agent_configs").select("*").execute()
        if response.data is None:
            return []
        return response.data
    except Exception as e:
        raise Exception(f"Supabase fetch error: {str(e)}")
