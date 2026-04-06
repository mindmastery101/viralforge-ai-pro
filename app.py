

import streamlit as st
from openai import OpenAI

# Secure API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(page_title="ViralForge AI", page_icon="🔥")

st.title("🔥 ViralForge AI")
st.subheader("AI Viral Script Generator")

# User input
topic = st.text_input("Enter your video topic:")

style = st.selectbox(
    "Choose Style:",
    ["Roblox Rant (Viral)", "Dan Koe Deep", "Storytelling", "Educational"]
)

def generate_ai_script(topic, style):
    prompt = f"""
You are an expert viral content creator.

Create a HIGH-RETENTION short-form video script.

Topic: {topic}
Style: {style}

RULES:
- Hook in first 2 seconds
- No boring lines
- Fast pacing
- Emotional + relatable
- Keep it under 25 seconds

STRUCTURE:
Hook → Reaction → Exaggeration → Relatable payoff → CTA
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# Button
if st.button("Generate Script"):
    if topic:
        script = generate_ai_script(topic, style)
        st.text_area("🔥 Your Viral Script:", script, height=300)
    else:
        st.warning("Please enter a topic first.")