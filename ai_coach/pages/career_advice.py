# pages/career_advice.py
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
from prompts import generate_career_prompt

# Load environment variables from .env file
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=groq_api_key)

def run():
    st.title("🎯 Career Advice")
    name = st.text_input(" Full Name")
    degree = st.text_input(" Degree")
    skills = st.text_area(" Skills (comma-separated)")
    interests = st.text_area(" Interests (comma-separated)")
    personality = st.selectbox(" Personality Type", ["Introvert", "Extrovert", "Ambivert"])
    goal = st.text_input(" Career Goal (optional)")

    if st.button("🔍 Get Career Advice"):
        if not all([name, degree, skills, interests, personality]):
            st.warning("Please fill in all fields.")
        else:
            with st.spinner("Generating advice..."):
                try:
                    prompt = generate_career_prompt(name, degree, skills, interests, personality, goal)
                    response = client.chat.completions.create(
                        model="llama3-70b-8192",  # Stable working Groq model
                        messages=[
                            {"role": "system", "content": "You are a helpful career advisor."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7
                    )
                    st.subheader("🧠 Your AI-Powered Career Advice:")
                    st.write(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")

