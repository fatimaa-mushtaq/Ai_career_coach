# auth_config.py

import yaml
import os
import streamlit_authenticator as stauth

CONFIG_PATH = "config.yaml"

def hash_password(password):
    return stauth.Hasher([password]).generate()[0]

def save_user(username, name, email, password):
    hashed_pw = hash_password(password)
    
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as file:
            config = yaml.safe_load(file)
    else:
        config = {
            "credentials": {
                "usernames": {}
            },
            "cookie": {
                "name": "ai_app_cookie",
                "key": "random_key",
                "expiry_days": 1
            },
            "preauthorized": {
                "emails": []
            }
        }

    if username in config["credentials"]["usernames"]:
        return False, "Username already exists"

    config["credentials"]["usernames"][username] = {
        "name": name,
        "email": email,
        "password": hashed_pw
    }

    config["preauthorized"]["emails"].append(email)

    with open(CONFIG_PATH, "w") as file:
        yaml.dump(config, file)

    return True, "User registered successfully"
