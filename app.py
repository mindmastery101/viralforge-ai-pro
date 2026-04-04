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