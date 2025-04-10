# app/auth.py
import bcrypt
from data.database import Database

class AuthManager:
    """
    Handles user authentication and registration.
    """
    def __init__(self):
        self.db = Database

    def register_user(self, username: str, password: str, currency: str = 'USD') -> bool:
        """
        Registers a new user with a hashed password.
        """
        try:
            password_bytes = password.encode('utf-8')
            password_hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            self.db.create_user(username=username, password_hash=password_hash, currency=currency)
            return True
        except Exception as e:
            print(f"Registration error: {e}")
            return False

    def login_user(self, username: str, password: str):
        """
        Validates user credentials.
        """
        user = self.db.get_user_by_username(username)
        if user:
            stored_hash = user['password_hash']
            if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
                return user  # Login successful
        return None
