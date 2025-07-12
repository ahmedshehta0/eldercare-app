# D:\ahmed\Elder care\trial 1\main.py

import os
from kivy.utils import platform

# This part is crucial for Android to know where to save Kivy's config files
# without needing root access.
if platform == "android":
    from android.storage import app_storage_path
    # Define a writable path for Kivy's home directory
    kivy_home = os.path.join(app_storage_path(), ".kivy")
    if not os.path.exists(kivy_home):
        os.makedirs(kivy_home)
    os.environ["KIVY_HOME"] = kivy_home
    print(f"KIVY_HOME set to: {os.environ['KIVY_HOME']}")

# Import the main App class from our package and run it.
from eldercare.app import ElderCareApp

if __name__ == "__main__":
    print("Starting ElderCare AI Application...")
    ElderCareApp().run()