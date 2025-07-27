# signup.py
import streamlit as st
import bcrypt

st.title("📝 Signup")

username = st.text_input("Choose a username")
email = st.text_input("Your Email")
name = st.text_input("Full Name")
password = st.text_input("Choose a password", type="password")

if st.button("Generate Signup Data"):
    if username and email and name and password:
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        st.code(f"""
{username}:
  email: {email}
  name: {name}
  password: {hashed_pw}
""", language='yaml')
        st.success("✅ Copy this YAML and add it to auth_config.yaml under `credentials.usernames`")
    else:
        st.warning("Fill all fields.")
