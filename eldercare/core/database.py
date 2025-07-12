import firebase_admin
from firebase_admin import credentials, db
import logging
from .auth import PasswordHelper

class DatabaseHelper:
    """
    Manages all interactions with the Firebase Realtime Database
    using the official firebase-admin SDK.
    """
    _app_initialized = False

    def __init__(self):
        if not DatabaseHelper._app_initialized:
            try:
                # !!! IMPORTANT !!!
                # 1. Download your serviceAccountKey.json from Firebase Project Settings.
                # 2. Place it in the root of your project (next to main.py).
                # 3. Replace 'path/to/your/serviceAccountKey.json' with the actual filename.
                cred = credentials.Certificate("serviceAccountKey.json")

                # !!! IMPORTANT !!!
                # Replace 'https://your-project-id.firebaseio.com/' with your Firebase Realtime Database URL.
                firebase_admin.initialize_app(cred, {
                    'databaseURL': 'hhttps://org-shehta-ahmed-eldercare.firebaseio.com/'
                })
                
                DatabaseHelper._app_initialized = True
                logging.info("Successfully connected to Firebase.")
            except Exception as e:
                logging.error(f"Could not connect to Firebase. Check your service account key and database URL. Error: {e}")
                # You might want to handle this more gracefully, e.g., by disabling database features.
                self.db_root = None
                return

        # Get a reference to the root of your database.
        self.db_root = db.reference()

    def login_user(self, username, password):
        """Verifies user credentials against Firebase."""
        if not self.db_root:
            return None, "Database connection failed"
        
        try:
            # Get user data from the 'users' node
            user_node = self.db_root.child('users').child(username)
            user_data = user_node.get()
            
            if user_data and 'password_hash' in user_data:
                # Check the password
                if PasswordHelper.check_password(password, user_data['password_hash']):
                    logging.info(f"User '{username}' authenticated successfully.")
                    return user_data, "Login successful"
            
            logging.warning(f"Authentication failed for user '{username}'.")
            return None, "Invalid username or password"
        except Exception as e:
            logging.error(f"Error during login process: {e}")
            return None, "An error occurred during login."

    def create_user(self, username, password):
        """Creates a new user with a hashed password."""
        if not self.db_root:
            return False, "Database connection failed"
        
        try:
            hashed_pw = PasswordHelper.hash_password(password)
            user_data = {'password_hash': hashed_pw, 'role': 'admin'}
            
            # Set the user data in the 'users' node
            self.db_root.child('users').child(username).set(user_data)
            
            logging.info(f"User '{username}' created successfully.")
            return True, "User created"
        except Exception as e:
            logging.error(f"Failed to create user '{username}': {e}")
            return False, "Failed to create user"