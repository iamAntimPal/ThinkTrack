# app/auth.py
import bcrypt
from data import database

def register_user(username: str, password: str, currency: str = 'USD'):
    """
    Registers a new user in the database with hashed password.
    """
    password_bytes = password.encode('utf-8')
    password_hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    try:
        database.create_user(username=username, password_hash=password_hash, currency=currency)
        return True
    except Exception as e:
        print(f"Registration error: {e}")
        return False

def login_user(username: str, password: str):
    """
    Validates user credentials.
    """
    user = database.get_user_by_username(username)
    if user:
        stored_hash = user['password_hash']
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            return user  # Return user info on success
    return None
