from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class LoginPage(App):
    def build(self):
        # Set the Window size to emulate a mobile screen 
        Window.size = (320, 640)  # Width x Height
        Window.borderless = True  # Remove the window border
        Window.clearcolor = (0.8, 0.8, 0.8, 1)  # Set background color to light gray

        # Create a FloatLayout
        layout = FloatLayout()

        # Add a label for the app name and center it both vertically and horizontally
        app_label = Label(
            text="Inventory Management",
            font_size=24,
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        layout.add_widget(app_label)

        # Add text inputs for username and password and center them
        username_input = TextInput(
            hint_text="Username",
            font_size=18,
            size_hint=(None, None),
            size=(300, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        password_input = TextInput(
            hint_text="Password",
            password=True,
            font_size=18,
            size_hint=(None, None),
            size=(300, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        layout.add_widget(username_input)
        layout.add_widget(password_input)

        # Add a login button and center it
        login_button = Button(
            text="Login",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)

        return layout

    def login(self, instance):
        pass

if __name__ == "__main__":
    LoginPage().run()