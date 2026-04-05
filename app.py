
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY_HERE")

st.set_page_config(page_title="ViralForge AI", page_icon="🔥")

st.title("🔥 ViralForge AI")
st.subheader("AI Viral Script Generator (Roblox + Dan Koe Style)")

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
- Use Roblox/gaming metaphors if needed
- Keep it under 25 seconds

STRUCTURE:
Hook → Reaction → Exaggeration → Metaphor → Relatable payoff → CTA
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if st.button("Generate Script"):
    if topic:
        script = generate_ai_script(topic, style)
        st.text_area("🔥 Your Viral Script:", script, height=300)
    else:
        st.warning("Enter a topic first.")