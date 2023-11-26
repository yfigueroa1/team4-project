from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class BarcodePage(App):
    def build(self):
        # Set the Window size to emulate a mobile screen 
        Window.size = (320, 640)  # Width x Height
        Window.borderless = True  # Remove the window border
        Window.clearcolor = (0.8, 0.8, 0.8, 1)  # Set background color to light gray

        # Create a FloatLayout
        layout = FloatLayout()

        # Add a label for the title ("Barcode Page") and center it both vertically and horizontally
        title_label = Label(
            text="Barcode Page",
            font_size=16,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.62}  # Adjust the vertical position
        )
        layout.add_widget(title_label)

        # Remove the label for barcode and set hint text to "Enter Barcode Number" and center it
        barcode_input = TextInput(
            hint_text="Enter Barcode",
            font_size=18,
            size_hint=(None, None),
            size=(200, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.52}  # Adjust the vertical position
        )

        layout.add_widget(barcode_input)

        # Create a BoxLayout for buttons (centered horizontally) and adjust vertical positioning
        button_layout = BoxLayout(
            orientation='vertical',
            spacing=10,
            size_hint=(None, None),
            size=(200, 80),  # Increase the height to accommodate buttons
            pos_hint={'center_x': 0.5, 'center_y': 0.42}  # Adjust the vertical position
        )

        add_item_button = Button(text="Add Item")
        add_item_button.bind(on_press=self.add_item)
        remove_item_button = Button(text="Remove Item")
        remove_item_button.bind(on_press=self.remove_item)

        button_layout.add_widget(add_item_button)
        button_layout.add_widget(remove_item_button)

        layout.add_widget(button_layout)

        return layout

    def add_item(self, instance):
        # Add code to add an item (replace with your logic)
        barcode = self.barcode_input.text
        self.show_popup("Add Item", f"Adding item with Barcode {barcode}")

    def remove_item(self, instance):
        # Add code to remove an item (replace with your logic)
        barcode = self.barcode_input.text
        self.show_popup("Remove Item", f"Removing item with Barcode {barcode}")

    def show_popup(self, title, content):
        # Create a popup to display messages
        popup_layout = GridLayout(cols=1, padding=10)
        popup_layout.add_widget(Label(text=content))
        close_button = Button(text="Close")
        popup_layout.add_widget(close_button)

        popup = Popup(title=title, content=popup_layout, size_hint=(None, None), size=(300, 150))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == "__main__":
    BarcodePage().run()