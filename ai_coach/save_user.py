# save_user.py
import yaml
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader
import os

CONFIG_PATH = "config.yaml"

def save_user(username, name, email, password):
    if not all([username, name, email, password]):
        return False, "Please fill in all fields."

    # Load existing config
    if not os.path.exists(CONFIG_PATH):
        return False, "Configuration file not found."

    with open(CONFIG_PATH, "r") as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Check if username already exists
    if username in config['credentials']['usernames']:
        return False, "Username already exists."

    # Hash password
    hashed_pw = stauth.Hasher([password]).generate()[0]

    # Add new user
    config['credentials']['usernames'][username] = {
        'email': email,
        'name': name,
        'password': hashed_pw
    }

    # Save updated config
    with open(CONFIG_PATH, "w") as file:
        yaml.dump(config, file)

    return True, "Registered successfully! You can now login."
