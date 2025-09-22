# backend/services/retell_client.py
import os
from openai import OpenAI
from dotenv import load_dotenv
from . import postprocess

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def start_call(payload: dict):
    """
    Simulate a call using AI-driven transcript and generate summary.
    """
    # Simple dummy response for testing; in real project, integrate Retell API
    driver_name = payload.get("driver_name", "Unknown")
    load_number = payload.get("load_number", "N/A")

    # Generate a dummy transcript
    transcript = f"Hello {driver_name}, this is a check-in call for load {load_number}. Driver reports all is fine."
    
    # Generate AI summary
    summary = postprocess.generate_summary(transcript)
    
    return {
        "status": "success",
        "transcript": transcript,
        "summary": summary
    }
