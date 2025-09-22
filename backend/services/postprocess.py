# backend/services/postprocess.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(transcript: str) -> str:
    """
    Generate AI-driven summary of the call transcript using OpenAI LLM (new API)
    """
    if not transcript:
        return "No transcript available."

    prompt = f"""
    You are an AI assistant. Summarize the following call transcript concisely:
    {transcript}
    Provide key points and any important status updates.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )

    summary = response.choices[0].message.content.strip()
    return summary
