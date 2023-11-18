import tkinter as tk
from tkinter import messagebox

def login():
    valid_credentials = {"admin": "password123"} 

    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if valid_credentials.get(entered_username) == entered_password:
        messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()
root.title("Login Page")

tk.Label(root, text="Username:").pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack(pady=10)

tk.Label(root, text="Password:").pack(pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

tk.Button(root, text="Login", command=login).pack(pady=20)
root.mainloop()