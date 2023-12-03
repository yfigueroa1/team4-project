from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

class LoginPage(Screen):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)
        layout = FloatLayout()

        app_label = Label(
            text="InventoTrack",
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
        pass
        self.manager.current = 'home'

    def go_to_create_account_page(self, instance):
        self.manager.current = 'create_account'

    def register(self, instance):
        print("Register button pressed")

    def authenticate(self, username, password):
        username = "admin"
        password = "password"

        
class CreateAccountPage(Screen):
    def __init__(self, **kwargs):
        super(CreateAccountPage, self).__init__(**kwargs)
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None, height=300)

        app_label = Label(
            text="Create Account",
            font_size=24,
            size_hint_y=None,
            height=40
        )

        email_input = TextInput(
            hint_text="Email",
            font_size=18,
            size_hint_y=None,
            height=30
        )
        password_input = TextInput(
            hint_text="Password",
            password=True,
            font_size=18,
            size_hint_y=None,
            height=30
        )
        confirm_password_input = TextInput(
            hint_text="Confirm Password",
            password=True,
            font_size=18,
            size_hint_y=None,
            height=30
        )

        create_account_button = Button(
            text="Create Account",
            font_size=20,
            size_hint_y=None,
            height=40
        )
        create_account_button.bind(on_press=self.create_account)

        layout.add_widget(app_label)
        layout.add_widget(email_input)
        layout.add_widget(password_input)
        layout.add_widget(confirm_password_input)
        layout.add_widget(create_account_button)

        self.add_widget(layout)

    def create_account(self, instance):
        email = self.children[0].children[1].text
        password = self.children[0].children[2].text
        confirm_password = self.children[0].children[3].text

        if password == confirm_password:
            print(f"Creating account with email: {email} and password: {password}")
            self.manager.current = 'login'
        else:
            error_popup = Popup(title='Error', content=Label(text='Passwords do not match.'), size_hint=(None, None), size=(400, 200))
            error_popup.open()
    
class HomePage(Screen):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        
        layout = FloatLayout()
        app_label = Label(
            text="Home Page",
            font_size=24,
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        layout.add_widget(app_label)

        quantity_button = Button(
            text="Quantity",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.6} 
        )
        
        view_inventory_button = Button(
            text="View Inventory",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}  
        )
        
        barcode_button = Button(
            text="Barcode",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}  
        )
        
        view_inventory_button.bind(on_press=self.go_to_product_page) 
        layout.add_widget(view_inventory_button)
        
        quantity_button.bind(on_press=self.go_to_quantity_page)  
        layout.add_widget(quantity_button)
        
        barcode_button.bind(on_press=self.go_to_barcode_page) 
        layout.add_widget(barcode_button)
        
        self.add_widget(layout)

    def go_to_product_page(self, instance):
        self.manager.current = 'product'

    def go_to_quantity_page(self, instance):
        self.manager.current = 'quantity'

    def go_to_barcode_page(self, instance):
        self.manager.current = 'barcode'
               
class ProductPage(Screen):
    def __init__(self, **kw):
        super(ProductPage, self).__init__(**kw)
        layout = FloatLayout()

        app_label = Label(
            text="Product Detail Page",
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
            size=(200, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        product_quantity_input = TextInput(
            hint_text="Quantity",
            input_type='number',
            font_size=18,
            size_hint=(None, None),
            size=(200, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        layout.add_widget(product_name_input)
        layout.add_widget(product_quantity_input)

        add_button = Button(
            text="Add Item",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        add_button.bind(on_press=self.add_to_inventory)
        layout.add_widget(add_button)
        
        back_button = Button(
            text="Back",
            font_size=20,
            size_hint=(None, None),
            size=(100, 40),
            pos_hint={'center_x': 0.3, 'center_y': 0.1}
        )
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)
        self.add_widget(layout)
        
    def go_back(self, instance):
        self.manager.current = 'home'

        
    def add_to_inventory(self, instance):
        product_name = self.children[0].children[2].text  
        quantity = self.children[0].children[3].text  

        print(f"Adding {quantity} units of {product_name} to inventory.")
          
class QuantityPage(Screen):
    def __init__(self, **kw):
        super(QuantityPage, self).__init__(**kw)
        layout = FloatLayout()

        app_label = Label(
            text="Quantity Page",
            font_size=24,
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        layout.add_widget(app_label)

        product_lookup_input = TextInput(
            hint_text="Product Name",
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
        layout.add_widget(lookup_button)

        quantity_label = Label(
            text="Quantity: ",
            font_size=18,
            size_hint=(None, None),
            size=(200, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        layout.add_widget(quantity_label)

        new_quantity_input = TextInput(
            hint_text="New Quantity",
            input_type='number',
            font_size=18,
            size_hint=(None, None),
            size=(200, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.3}
        )
        layout.add_widget(new_quantity_input)

        change_quantity_button = Button(
            text="Change Quantity",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.2}
        )
        layout.add_widget(change_quantity_button)
        
        back_button = Button(
            text="Back",
            font_size=20,
            size_hint=(None, None),
            size=(100, 40),
            pos_hint={'center_x': 0.3, 'center_y': 0.1}
        )
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)
        
    def go_back(self, instance):
        self.manager.current = 'home'

    def get_quantity_from_inventory(self, product_name):
        inventory_data = {
            'Product1': 10,
            'Product2': 20,
            'Product3': 15,
        }

        return inventory_data.get(product_name, 0)

                
class BarcodePage(Screen):
    def __init__(self, **kwargs):
        super(BarcodePage, self).__init__(**kwargs)
        layout = FloatLayout()

        app_label = Label(
            text="Barcode Page",
            font_size=24,
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        layout.add_widget(app_label)

        barcode_input = TextInput(
            hint_text="Enter Barcode",
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
        add_button.bind(on_press=self.add_to_inventory)
        layout.add_widget(add_button)

        remove_button = Button(
            text="Remove Item",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}  
        )
        layout.add_widget(remove_button)

        show_inventory_button = Button(
            text="Show Inventory",
            font_size=20,
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.3}  
        )
        layout.add_widget(show_inventory_button)
        
        back_button = Button(
            text="Back",
            font_size=20,
            size_hint=(None, None),
            size=(100, 40),
            pos_hint={'center_x': 0.3, 'center_y': 0.1}
        )
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)
        
    def go_back(self, instance):
        self.manager.current = 'home'

    def add_to_inventory(self, instance):
        barcode = self.children[0].children[2].text  
        print(f"Adding item with barcode {barcode} to inventory.")

class InventoryManagementApp(App):
    def build(self):
        Window.size=(320,640)
        sm = ScreenManager()

        login_page = LoginPage(name='login')
        home_page = HomePage(name='home')
        product_page = ProductPage(name='product')
        quantity_page = QuantityPage(name='quantity')
        barcode_page = BarcodePage(name='barcode')
        create_account_page = CreateAccountPage(name='create_account')

        sm.add_widget(login_page)
        sm.add_widget(home_page)
        sm.add_widget(product_page)
        sm.add_widget(quantity_page)
        sm.add_widget(barcode_page)
        sm.add_widget(create_account_page)
        return sm
    
if __name__ == "__main__":
    InventoryManagementApp().run()
