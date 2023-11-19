import tkinter as tk
from tkinter import ttk, messagebox

class InventoryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management App")
        self.inventory = {'item1': {'name': 'Item 1', 'quantity': 10}, 'item2': {'name': 'Item 2', 'quantity': 5}, 'item3': {'name': 'Item 3', 'quantity': 15}}

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.master, text="Inventory Management App", font=("Helvetica", 16)).pack(pady=10)

        columns = ('Item ID', 'Item Name', 'Quantity')
        self.tree = ttk.Treeview(self.master, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10)

        ttk.Label(self.master, text="Enter new quantity:").pack()
        self.quantity_entry = ttk.Entry(self.master)
        self.quantity_entry.pack()

        ttk.Button(self.master, text="Update Quantity", command=self.update_quantity).pack(pady=10)

        for item_id, details in self.inventory.items():
            self.tree.insert('', 'end', values=(item_id, details['name'], details['quantity']))

    def update_quantity(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item from the inventory.")
            return

        item_id = self.tree.item(selected_item, 'values')[0]
        new_quantity = self.quantity_entry.get()

        try:
            new_quantity = int(new_quantity)
            if new_quantity < 0:
                raise ValueError("Quantity cannot be negative.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid quantity: {e}")
            return

        self.inventory[item_id]['quantity'] = new_quantity
        self.tree.item(selected_item, values=(item_id, self.inventory[item_id]['name'], new_quantity))
        self.quantity_entry.delete(0, 'end')

        messagebox.showinfo("Success", "Quantity updated successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
