from kivy.uix.screenmanager import Screen
from kivymd.uix.switch import MDSwitch

# Define a custom KivyMD Switch class to use in KV
# This allows the KV file to find and use `RightSwitch`
class RightSwitch(MDSwitch):
    pass

class SettingsScreen(Screen):
    pass