import tkinter as tk

class InventoryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management App")

        self.label = tk.Label(master, text="Welcome to Inventory Management", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button_new_item = tk.Button(master, text="New Item", command=self.open_new_item_window)
        self.button_new_item.pack(pady=10)

        self.button_view_inventory = tk.Button(master, text="View Inventory", command=self.open_view_inventory_window)
        self.button_view_inventory.pack(pady=10)

        self.button_exit = tk.Button(master, text="Exit", command=master.destroy)
        self.button_exit.pack(pady=20)

    def open_new_item_window(self):
        print("Opening New Item Window")

    def open_view_inventory_window(self):
        print("Opening View Inventory Window")

root = tk.Tk()
app = InventoryApp(root)
root.mainloop()
