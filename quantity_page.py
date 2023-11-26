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
            size=(400, 40),
            pos_hint={'center_x': 0.5, 'top': 1}
        )
        layout.add_widget(app_label)

        product_lookup_input = TextInput(
            hint_text="Product Name",
            font_size=18,
            size_hint=(None, None),
            size=(300, 30),
            pos_hint={'center_x': 0.5, 'top': 0.9}
        )
        layout.add_widget(product_lookup_input)

        lookup_button = Button(
            text="Lookup Quantity",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'top': 0.8}
        )
        lookup_button.bind(on_press=self.lookup_quantity)
        layout.add_widget(lookup_button)

        quantity_label = Label(
            text="Quantity: ",
            font_size=18,
            size_hint=(None, None),
            size=(300, 30),
            pos_hint={'center_x': 0.5, 'top': 0.7}
        )
        layout.add_widget(quantity_label)

        new_quantity_input = TextInput(
            hint_text="New Quantity",
            input_type='number',
            font_size=18,
            size_hint=(None, None),
            size=(300, 30),
            pos_hint={'center_x': 0.5, 'top': 0.6}
        )
        layout.add_widget(new_quantity_input)

        change_quantity_button = Button(
            text="Change Quantity",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'top': 0.5}
        )
        change_quantity_button.bind(on_press=self.change_quantity)
        layout.add_widget(change_quantity_button)

        return layout

    def lookup_quantity(self, instance):
        product_name = self.root.children[2].text  
        quantity = self.get_quantity_from_inventory(product_name)
        quantity_label = self.root.children[4]  
        quantity_label.text = f"Quantity: {quantity}"

    def change_quantity(self, instance):
        product_name = self.root.children[2].text  
        new_quantity = self.root.children[5].text  

        print(f"Changing quantity of {product_name} to {new_quantity}.")

    def get_quantity_from_inventory(self, product_name):
        inventory_data = {
            'Product1': 10,
            'Product2': 20,
            'Product3': 15,
        }

        return inventory_data.get(product_name, 0)

if __name__ == "__main__":
    InventoryManagementApp().run()