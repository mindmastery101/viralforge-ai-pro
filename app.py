import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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
