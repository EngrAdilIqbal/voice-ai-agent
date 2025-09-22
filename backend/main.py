# backend/main.py
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from typing import Dict

from services import supabase_client, retell_client, postprocess

load_dotenv()

app = FastAPI(title="AI Voice Agent Backend")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Voice Agent Backend is running"}

@app.get("/configs")
def get_configs():
    try:
        configs = supabase_client.get_all_configs()
        return configs
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Supabase fetch error: {str(e)}")

@app.post("/start_call")
def start_call(payload: Dict):
    """
    payload should contain:
    {
        "driver_name": "John",
        "driver_phone": "+10000000000",
        "load_number": "LOAD123",
        "config_id": "xxxx-xxxx"
    }
    """
    try:
        result = retell_client.start_call(payload)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Call failed: {str(e)}")
