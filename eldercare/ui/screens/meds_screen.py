# هذا الملف كامل كما هو في الرد السابق، لا تغييرات.
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.pickers import MDTimePicker
from kivy.lang import Builder
from kivy.app import App
from functools import partial

MED_DIALOG_KV = '''
<MedDialogContent@MDBoxLayout>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "300dp"
    MDTextField:
        id: med_name
        hint_text: "Medication Name"
    MDTextField:
        id: med_dosage
        hint_text: "Dosage (e.g., 50mg)"
    MDBoxLayout:
        adaptive_height: True
        MDTextField:
            id: med_time_display
            hint_text: "Reminder Time (HH:MM)"
            readonly: True
        MDIconButton:
            icon: 'clock-plus-outline'
            on_release: app.get_screen('meds_screen').show_time_picker(root)
'''

class MedsScreen(Screen):
    dialog = None
    def show_med_dialog(self, med_data=None):
        if not self.dialog:
            dialog_content = Builder.load_string(MED_DIALOG_KV)
            self.dialog = MDDialog(
                title="Add Medication",
                type="custom",
                content_cls=dialog_content,
                buttons=[
                    MDFlatButton(text="CANCEL", on_release=lambda x: self.dialog.dismiss()),
                    MDRaisedButton(text="SAVE", on_release=lambda x: App.get_running_app().save_medication(self.dialog.content_cls, self.dialog)),
                ]
            )
        self.dialog.open()
        
    def show_time_picker(self, dialog_content_instance):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=partial(self.set_time, dialog_content_instance))
        time_dialog.open()
        
    def set_time(self, dialog_content_instance, instance, time):
        if dialog_content_instance:
            dialog_content_instance.ids.med_time_display.text = time.strftime('%H:%M')