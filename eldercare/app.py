# D:\ahmed\Elder care\trial 1\eldercare\app.py

import logging
import threading
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.spinner import MDSpinner

# Import our custom modules
from .core.database import DatabaseHelper
from .services.ad_manager import AdManager

# Import screens so Kivy can recognize them
from .ui.screens.login_screen import LoginScreen
from .ui.screens.main_screen import MainScreen
from .ui.screens.home_screen import HomeScreen
from .ui.screens.meds_screen import MedsScreen
# ... import other screens

class ElderCareApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logging.basicConfig(level=logging.INFO)
        self.db_helper = DatabaseHelper()
        self.ad_manager = AdManager(self)
        self.current_user = None

    def build(self):
        # Load the main KV file which includes all others
        return Builder.load_file('eldercare/ui/kv/main.kv')

    def login(self, username, password):
        # ... (Login logic from Singularity file, but now it's cleaner)
        if not username or not password:
            self.show_snackbar("Username and password are required.")
            return
        
        spinner = MDSpinner(size_hint=(None, None), size=("46dp", "46dp"), pos_hint={'center_x': .5, 'center_y': .5})
        self.root.get_screen('login').add_widget(spinner)

        def do_login_thread():
            user_data, message = self.db_helper.login_user(username, password)
            Clock.schedule_once(lambda dt: self.on_login_result(user_data, message, spinner))

        threading.Thread(target=do_login_thread, daemon=True).start()

    def on_login_result(self, user_data, message, spinner):
        if spinner.parent:
            spinner.parent.remove_widget(spinner)
        self.show_snackbar(message)
        if user_data:
            self.current_user = self.root.get_screen('login').ids.username.text
            self.root.current = 'main'
            self.root.get_screen('main').ids.nav_drawer_username.text = f"Welcome, {self.current_user}"

    def logout(self):
        self.current_user = None
        self.root.current = 'login'
    
    def change_screen(self, screen_name, title):
        main_screen = self.root.get_screen('main')
        main_screen.ids.main_screen_manager.current = screen_name
        main_screen.ids.top_bar.title = title
        main_screen.ids.nav_drawer.set_state("close")
        
    def save_medication(self, dialog_content, dialog_instance):
        name = dialog_content.ids.med_name.text
        if name:
            self.show_snackbar(f"Saved medication: {name}")
            # Future: self.db_helper.save_med(...)
            self.ad_manager.request_and_show_interstitial()
            dialog_instance.dismiss()
        else:
            self.show_snackbar("Medication name is required.")

    def get_screen(self, screen_name):
        # A helper function to easily get a screen instance
        return self.root.get_screen('main').ids.main_screen_manager.get_screen(screen_name)

    def show_snackbar(self, text):
        Snackbar(text=text).open()