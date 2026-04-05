

import streamlit as st
from openai import OpenAI


# app.py - ViralForge-AI

from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # optional if you plan to use OpenAI later

def generate_script(topic: str) -> str:
    """
    Generate a viral script placeholder.
    Later, you can integrate with OpenAI API for real AI output.
    """
    return (
        f"🔥 Viral Script for '{topic}' 🔥\n\n"
        "1️⃣ Hook your audience in the first 3 seconds.\n"
        "2️⃣ Deliver the main content fast and entertaining.\n"
        "3️⃣ Include a call-to-action at the end.\n"
        "4️⃣ Make it short, shareable, and viral-ready!\n"
    )

def main():
    print("\n🔥 Welcome to ViralForge-AI 🔥\n")
    topic = input("Enter your video topic: ")
    script = generate_script(topic)
    print("\n" + script + "\n")

if __name__ == "__main__":
    main()


import os
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_viral_script(topic):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert content creator for short viral videos."},
            {"role": "user", "content": f"Generate a 60-second viral video script for TikTok about: {topic}"}
        ],
        max_tokens=250
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("🔥 ViralForge-AI: Generate Viral Short Video Scripts 🔥")
    topic = input("Enter your video topic: ")
    script = generate_viral_script(topic)
    print("\n--- Viral Script ---\n")
    print(script)


