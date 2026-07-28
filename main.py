from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from widgets import *

Window.size = (360, 640)
new=True

class Auth(Screen): #authentication selection page
    pass

class AuthRegister(Screen):
    def register_data(self):
        name_text = self.ids.name_input_reg.text
        email_text = self.ids.email_input_reg.text
        pass_text = self.ids.pass_input_reg.text
        conpass_text = self.ids.conpass_input_reg.text

        print(f"name: {name_text}, email: {email_text}, pass: {pass_text}, conpass: {conpass_text}")

        #User input name, email, pass and confirmed pass, save data to file here

class AuthLogin(Screen):
    def login_data(self):
        email_text = self.ids.email_input_login.text
        pass_text = self.ids.pass_input_login.text

        print(f"email: {email_text}, pass: {pass_text}")

        #User input email and pass, save data to file here

class WindowManager(ScreenManager):
    pass

class RiderApp(App):
    def build(self):
        rider = Builder.load_file('rider.kv')

        if new:
            rider.current = "auth"

        return rider

if __name__ == '__main__':
    RiderApp().run()