# hash_password.py

from passlib.context import CryptContext

# List of passwords you want to hash
passwords = ['your_password']  # Replace with your actual password

# Create a password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Generate hashed passwords
hashed_passwords = [pwd_context.hash(pw) for pw in passwords]

# Print hashed password(s)
print(hashed_passwords)
