class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_item(self, barcode, quantity=1):
        if barcode in self.inventory:
            self.inventory[barcode] += quantity
        else:
            self.inventory[barcode] = quantity
        print(f"Added {quantity} item(s) with barcode {barcode}.")

    def remove_item(self, barcode, quantity=1):
        if barcode in self.inventory:
            if self.inventory[barcode] >= quantity:
                self.inventory[barcode] -= quantity
                print(f"Removed {quantity} item(s) with barcode {barcode}.")
                if self.inventory[barcode] == 0:
                    del self.inventory[barcode]
            else:
                print(f"Cannot remove {quantity} items. Only {self.inventory[barcode]} items in inventory.")
        else:
            print(f"No items with barcode {barcode} found in inventory.")

    def show_inventory(self):
        if self.inventory:
            print("Current Inventory:")
            for barcode, count in self.inventory.items():
                print(f"Barcode: {barcode}, Count: {count}")
        else:
            print("Inventory is empty.")

    def add_item_interactively(self):
        barcode = input("Enter the barcode: ")
        quantity = input("Enter the quantity: ")
        try:
            quantity = int(quantity)
            self.add_item(barcode, quantity)
        except ValueError:
            print("Invalid quantity. Please enter a number.")
