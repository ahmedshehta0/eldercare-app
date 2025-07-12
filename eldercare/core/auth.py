# D:\ahmed\Elder care\trial 1\eldercare\core\auth.py

import bcrypt

class PasswordHelper:
    """Handles password hashing and verification using bcrypt."""
    @staticmethod
    def hash_password(plain_text_password):
        """Hashes a password for the first time."""
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    @staticmethod
    def check_password(plain_text_password, hashed_password):
        """Checks a plain text password against a stored hashed password."""
        return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password.encode('utf-8'))