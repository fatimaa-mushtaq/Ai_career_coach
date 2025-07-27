# pages/interview_coach.py
import streamlit as st
from dotenv import load_dotenv
import os
from groq import Groq

# Load API key from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=groq_api_key)

def run():
    st.title("🎤 Interview Coach")

    role = st.text_input("💼 Desired Role or Job Title (e.g., Data Analyst, UX Designer)")
    if st.button("🧠 Generate Top 5 Interview Questions"):
        if not role:
            st.warning("Please enter a job title.")
        else:
            with st.spinner("Generating interview questions..."):
                try:
                    prompt = f"Generate the top 5 most relevant interview questions for a {role} position. Keep them concise and realistic."

                    response = client.chat.completions.create(
                        model="llama3-70b-8192",  # Valid and stable Groq model
                        messages=[
                            {"role": "system", "content": "You are an expert interview coach."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.6
                    )

                    st.subheader("📝 Interview Questions:")
                    st.markdown(response.choices[0].message.content)

                except Exception as e:
                    st.error(f"Error: {e}")

