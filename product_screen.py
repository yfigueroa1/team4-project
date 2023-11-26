from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class InventoryManagementApp(App):
    def build(self):
        Window.size = (320, 640)
        Window.borderless = True
        Window.clearcolor = (0.8, 0.8, 0.8, 1)

        layout = FloatLayout()

        app_label = Label(
            text="Inventory Management",
            font_size=24,
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        layout.add_widget(app_label)

        product_name_input = TextInput(
            hint_text="Product Name",
            font_size=18,
            size_hint=(None, None),
            size=(300, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        product_quantity_input = TextInput(
            hint_text="Quantity",
            input_type='number',
            font_size=18,
            size_hint=(None, None),
            size=(300, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        layout.add_widget(product_name_input)
        layout.add_widget(product_quantity_input)

        add_button = Button(
            text="Add to Inventory",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        add_button.bind(on_press=self.add_to_inventory)
        layout.add_widget(add_button)

        return layout

    def add_to_inventory(self, instance):
        product_name = self.root.children[2].text  
        quantity = self.root.children[3].text  

        print(f"Adding {quantity} units of {product_name} to inventory.")

if __name__ == "__main__":
    InventoryManagementApp().run()