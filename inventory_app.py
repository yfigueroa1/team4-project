from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

# Dummy data for demonstration purposes
users = []

class LoginPage(Screen):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)
        layout = FloatLayout()

        app_label = Label(
            text="Login",
            font_size=24,
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        layout.add_widget(app_label)

        username_input = TextInput(
            hint_text="Username",
            font_size=18,
            size_hint=(None, None),
            size=(200, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        password_input = TextInput(
            hint_text="Password",
            password=True,
            font_size=18,
            size_hint=(None, None),
            size=(200, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        layout.add_widget(username_input)
        layout.add_widget(password_input)

        login_button = Button(
            text="Login",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )

        register_button = Button(
            text="Create Account",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.3}
        )

        login_button.bind(on_press=self.login)
        register_button.bind(on_press=self.go_to_create_account_page)

        layout.add_widget(login_button)
        layout.add_widget(register_button)

        self.add_widget(layout)

    def login(self, instance):
        email_input = None
        password_input = None
        for child in self.children:
            if isinstance(child, FloatLayout):
                for widget in child.children:
                    if isinstance(widget, TextInput) and widget.hint_text == "Username":
                        email_input = widget
                    elif isinstance(widget, TextInput) and widget.hint_text == "Password":
                        password_input = widget

        if email_input is not None and password_input is not None:
            email = email_input.text
            password = password_input.text

            if self.authenticate(email, password):
                self.manager.current = 'home'
            else:
                error_popup = Popup(title='Error', content=Label(text='Invalid email or password.'),
                                    size_hint=(None, None), size=(200, 100))
                error_popup.open()
        else:
            print("Error: TextInput widgets not found.")

    def go_to_create_account_page(self, instance):
        self.manager.current = 'create_account'

    def register(self, email, password):
        users.append(User(email, password))
        print(f"User with email: {email} registered successfully.")

    def authenticate(self, email, password):
        for user in users:
            if user.email == email and user.password == password:
                return True
        return False

class CreateAccountPage(Screen):
    def __init__(self, **kwargs):
        super(CreateAccountPage, self).__init__(**kwargs)

        layout = AnchorLayout(anchor_x='center', anchor_y='center', pos_hint={'center_y': 0.7})

        app_label = Label(
            text="Create Account",
            font_size=24,
            size_hint_y=None,
            height=dp(40)
        )

        email_input = TextInput(
            hint_text="Email",
            font_size=18,
            size_hint_y=None,
            height=dp(30),
            multiline=False
        )
        password_input = TextInput(
            hint_text="Password",
            password=True,
            font_size=18,
            size_hint_y=None,
            height=dp(30),
            multiline=False
        )
        confirm_password_input = TextInput(
            hint_text="Confirm Password",
            password=True,
            font_size=18,
            size_hint_y=None,
            height=dp(30),
            multiline=False
        )

        create_account_button = Button(
            text="Create Account",
            font_size=20,
            size_hint_y=None,
            height=dp(40)
        )
        create_account_button.bind(on_press=lambda instance: self.create_account(email_input.text, password_input.text, confirm_password_input.text))

        box_layout = BoxLayout(orientation='vertical', spacing=dp(10), size_hint=(None, None), size=(dp(200), dp(400)))

        box_layout.add_widget(app_label)
        box_layout.add_widget(email_input)
        box_layout.add_widget(password_input)
        box_layout.add_widget(confirm_password_input)
        box_layout.add_widget(create_account_button)

        layout.add_widget(box_layout)
        self.add_widget(layout)

    def create_account(self, email, password, confirm_password):
        if not email or not password or not confirm_password:
            error_popup = Popup(title='Error', content=Label(text='Please enter both email and password.'),
                                size_hint=(None, None), size=(300, 100))
            error_popup.open()
            return

        if password == confirm_password:
            if not any(user.email == email for user in users):
                login_page = self.manager.get_screen('login')
                login_page.register(email, password)
                self.manager.current = 'login'
            else:
                error_popup = Popup(title='Error', content=Label(text='Email already in use.'),
                                    size_hint=(None, None), size=(200, 100))
                error_popup.open()
        else:
            error_popup = Popup(title='Error', content=Label(text='Passwords do not match.'),
                                size_hint=(None, None), size=(200, 100))
            error_popup.open()


class HomePage(Screen):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)

        layout = FloatLayout()

        app_label = Label(
            text="Home",
            font_size=24,
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        layout.add_widget(app_label)

        barcode_button = Button(
            text="Manage Inventory",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        barcode_button.bind(on_press=self.go_to_barcode_page)
        layout.add_widget(barcode_button)

        quantity_button = Button(
            text="Available Stock",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        quantity_button.bind(on_press=self.go_to_quantity_page)
        layout.add_widget(quantity_button)

        self.add_widget(layout)

    def go_to_quantity_page(self, instance):
        self.manager.current = 'quantity'

    def go_to_barcode_page(self, instance):
        self.manager.current = 'barcode'

class QuantityPage(Screen):
    def __init__(self, **kwargs):
        super(QuantityPage, self).__init__(**kwargs)
        layout = FloatLayout()

        self.icon1 = Image(source='home.png', size_hint=(None, None), size=(40, 40), pos=(80, 5))
        self.icon1.bind(on_touch_down=self.on_icon1_touch)

        self.icon2 = Image(source='manage.png', size_hint=(None, None), size=(40, 40), pos=(200, 5))
        self.icon2.bind(on_touch_down=self.on_icon2_touch)

        layout.add_widget(self.icon1)
        layout.add_widget(self.icon2)

        app_label = Label(
            text="Available Stock",
            font_size=24,
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        layout.add_widget(app_label)

        product_lookup_input = TextInput(
            hint_text="Enter Product Number",
            font_size=18,
            size_hint=(None, None),
            size=(200, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        layout.add_widget(product_lookup_input)

        lookup_button = Button(
            text="Lookup Quantity",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        lookup_button.bind(on_press=self.lookup_quantity)
        layout.add_widget(lookup_button)

        quantity_label = Label(
            text="Quantity: ",
            font_size=18,
            size_hint=(None, None),
            size=(200, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        layout.add_widget(quantity_label)
        
        with layout.canvas.before:
            Color(1, 1, 1, 1)  
            Rectangle(pos=(0, 0), size=(Window.width, 50))

        self.add_widget(layout)

    def lookup_quantity(self, instance):
        product_lookup_input = None
        quantity_label = None
        
        for widget in self.walk():
            if isinstance(widget, TextInput) and widget.hint_text == "Enter Product Number":
                product_lookup_input = widget
            elif isinstance(widget, Label) and widget.text.startswith("Quantity: "):
                quantity_label = widget

        if product_lookup_input is not None and quantity_label is not None:
            product_number = product_lookup_input.text
            quantity = self.get_quantity_from_inventory(product_number)

            if quantity is not None:
                quantity_label.text = f"Quantity: {quantity}"
            else:
                quantity_label.text = "Product not found in inventory."

    def on_icon1_touch(self, instance, touch):
        if self.icon1.collide_point(*touch.pos):
            self.go_to_home_page()

    def on_icon2_touch(self, instance, touch):
        if self.icon2.collide_point(*touch.pos):
            self.go_to_barcode_page(self)

    def go_back(self, instance):
        self.manager.current = 'home'

    def go_to_home_page(self):        
        self.manager.current = 'home'

    def go_to_barcode_page(self, instance):
        self.manager.current = 'barcode'

    def get_quantity_from_inventory(self, product_number):
        if product_number in BarcodePage.inventory_data:
            return BarcodePage.inventory_data[product_number]
        else:
            return None

    def on_icon1_touch(self, instance, touch):
        if self.icon1.collide_point(*touch.pos):
            self.go_to_home_page()

    def on_icon2_touch(self, instance, touch):
        if self.icon2.collide_point(*touch.pos):
            self.go_to_barcode_page(self)


class QuantityPopup(Popup):
    def __init__(self, barcode, **kwargs):
        super(QuantityPopup, self).__init__(**kwargs)
        self.title = 'Enter Quantity'
        self.barcode = barcode
        self.quantity_input = TextInput(multiline=False, size_hint=(None, None), size=(200, 30),
                                        pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.quantity_input.bind(on_text_validate=self.on_enter)
        self.content = self.quantity_input
        self.size_hint = (None, None)
        self.size = (200, 30)
        self.auto_dismiss = False
        self.result = None  

    def on_enter(self, instance):
        quantity = self.quantity_input.text
        if quantity.isdigit():
            self.result = int(quantity)  
        else:
            self.result = None  
            error_popup = Popup(title='Error', content=Label(text='Please enter a valid quantity.'),
                                size_hint=(None, None), size=(200, 30))
            error_popup.open()
        self.dismiss()


class BarcodePage(Screen):
    inventory_data = {}  

    def __init__(self, inventory_page, **kwargs):
        super(BarcodePage, self).__init__(**kwargs)
        self.inventory_page = inventory_page  
        layout = FloatLayout()

        self.icon1 = Image(source='home.png', size_hint=(None, None), size=(40, 40), pos=(80, 5))
        self.icon1.bind(on_touch_down=self.on_icon1_touch)

        self.icon2 = Image(source='stock.png', size_hint=(None, None), size=(40, 40), pos=(200, 5))
        self.icon2.bind(on_touch_down=self.on_icon2_touch)

        layout.add_widget(self.icon1)
        layout.add_widget(self.icon2)

        app_label = Label(
            text="Manage Inventory",
            font_size=24,
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        layout.add_widget(app_label)

        barcode_input = TextInput(
            hint_text="Enter Product Number",
            font_size=18,
            size_hint=(None, None),
            size=(200, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        layout.add_widget(barcode_input)

        add_button = Button(
            text="Add Item",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        add_button.bind(on_press=lambda instance: self.add_to_inventory(barcode_input.text))
        layout.add_widget(add_button)

        remove_button = Button(
            text="Remove Item",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        remove_button.bind(on_press=lambda instance: self.remove_from_inventory(barcode_input.text))
        layout.add_widget(remove_button)

        view_inventory_button = Button(
            text="View Inventory",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.3}
        )
        view_inventory_button.bind(on_press=self.view_inventory)
        layout.add_widget(view_inventory_button)
      
        with layout.canvas.before:
            Color(1, 1, 1, 1) 
            Rectangle(pos=(0, 0), size=(Window.width, 50))

        self.add_widget(layout)

    def add_to_inventory(self, barcode):        
        quantity_popup = QuantityPopup(barcode)
        quantity_popup.bind(on_dismiss=lambda instance: self.on_quantity_popup_dismiss(instance, barcode))
        quantity_popup.open()

    def remove_from_inventory(self, barcode):
        if barcode in BarcodePage.inventory_data:            
            quantity_popup = QuantityPopup(barcode)
            quantity_popup.title = 'Enter Quantity to Remove'
            quantity_popup.quantity_input.hint_text = 'Enter Quantity to Remove'
            quantity_popup.bind(on_dismiss=lambda instance: self.on_remove_quantity_popup_dismiss(instance, barcode))
            quantity_popup.open()
        else:
            error_popup = Popup(title='Error', content=Label(text=f'Item with barcode {barcode} not found.'),
                                size_hint=(None, None), size=(200, 30))
            error_popup.open()

    def view_inventory(self, instance):
        self.manager.current = 'inventory'

    def on_icon1_touch(self, instance, touch):
        if self.icon1.collide_point(*touch.pos):
            self.go_to_home_page()

    def on_icon2_touch(self, instance, touch):
        if self.icon2.collide_point(*touch.pos):
            self.go_to_quantity_page(self)

    def go_to_home_page(self):
        self.manager.current = 'home'

    def go_to_quantity_page(self, instance):
        self.manager.current = 'quantity'

    def on_quantity_popup_dismiss(self, instance, barcode):        
        if instance.result is not None:            
            quantity = instance.result
            print(f"Adding item with barcode {barcode} and quantity {quantity} to inventory.")
            
            BarcodePage.inventory_data[barcode] = quantity
            self.inventory_page.update_inventory_text()

    def on_remove_quantity_popup_dismiss(self, instance, barcode):       
        if instance.result is not None:            
            quantity_to_remove = instance.result
            current_quantity = BarcodePage.inventory_data[barcode]

            if quantity_to_remove <= current_quantity:                
                BarcodePage.inventory_data[barcode] -= quantity_to_remove
                print(f"Removing {quantity_to_remove} items with barcode {barcode} from inventory.")
                
                self.inventory_page.update_inventory_text()
            else:
                error_popup = Popup(title='Error', content=Label(text='Quantity to remove exceeds current quantity.'),
                                    size_hint=(None, None), size=(200, 30))
                error_popup.open()
        else:            
            print(f"Removal canceled for item with barcode {barcode}.")


class InventoryPage(Screen):
    def __init__(self, **kwargs):
        super(InventoryPage, self).__init__(**kwargs)
        layout = FloatLayout()

        self.app_label = Label(
            text="Inventory",
            font_size=24,
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.9}
        )
        layout.add_widget(self.app_label)
        
        self.inventory_label = Label(
            text=self.get_inventory_text(),
            font_size=18,
            size_hint=(None, None),
            size=(300, 400),
            pos_hint={'center_x': 0.5, 'center_y': 0.8}
        )
        layout.add_widget(self.inventory_label)

        back_button = Button(
            text="Go Back",
            font_size=18,
            size_hint=(None, None),
            size=(80, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.1}
        )
        back_button.bind(on_press=self.go_to_barcode_page)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def get_inventory_text(self):        
        inventory_text = ""
        for product, quantity in BarcodePage.inventory_data.items():
            inventory_text += f"{product}: {quantity}\n"
        return inventory_text

    def update_inventory_text(self):        
        self.inventory_label.text = self.get_inventory_text()

    def go_to_barcode_page(self, instance):
        self.manager.current = 'barcode'


class InventoryManagementApp(App):
    def build(self):
        Window.size = (320, 640)
        sm = ScreenManager()

        login_page = LoginPage(name='login')
        home_page = HomePage(name='home')
        quantity_page = QuantityPage(name='quantity')
        inventory_page = InventoryPage(name='inventory')
        barcode_page = BarcodePage(inventory_page, name='barcode')
        create_account_page = CreateAccountPage(name='create_account')

        sm.add_widget(login_page)
        sm.add_widget(home_page)
        sm.add_widget(quantity_page)
        sm.add_widget(inventory_page)
        sm.add_widget(barcode_page)
        sm.add_widget(create_account_page)

        return sm

if __name__ == "__main__":
    InventoryManagementApp().run()