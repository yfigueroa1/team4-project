from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class HomePage(App):
    def build(self):
        Window.size = (320, 640)
        Window.borderless = True
        Window.clearcolor = (0.8, 0.8, 0.8, 1)

        layout = FloatLayout()

        app_label = Label(
            text="Home Page",
            font_size=24,
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        layout.add_widget(app_label)

        new_item_button = Button(
            text="New Item",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}  # Adjusted position
        )

        view_inventory_button = Button(
            text="View Inventory Button",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.3}  # Adjusted position
        )

        layout.add_widget(view_inventory_button)
        layout.add_widget(new_item_button)
        return layout

if __name__ == "__main__":
    HomePage().run()
