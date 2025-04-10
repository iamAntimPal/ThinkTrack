# app/main.py
import tkinter as tk
from tkinter import messagebox
from app import auth, manager
from ui import components, dashboard, forms, reports
from data import database

def switch_theme(root, theme='light'):
    """
    Switch themes dynamically by reading the corresponding css file.
    (Note: Tkinter does not support CSS directly. This is a placeholder
    demonstrating that you can load theme parameters.)
    """
    try:
        with open(f'ui/styles/{theme}.css', 'r') as f:
            styles = f.read()
            # Process styles if needed and apply to widgets
            print(f"Applying {theme} theme settings...")
    except Exception as e:
        messagebox.showerror("Theme Error", f"Could not load theme: {e}")

def on_login_success(user):
    """
    Callback function once the login is successful. Initializes the main dashboard.
    """
    # Destroy login frame and start dashboard
    for widget in root.winfo_children():
        widget.destroy()
    dashboard_frame = dashboard.DashboardFrame(root, user)
    dashboard_frame.pack(fill='both', expand=True)

if __name__ == "__main__":
    # Initialize the database (create tables if they don’t exist)
    database.initialize_db()

    root = tk.Tk()
    root.title("Budget Management Application")
    root.geometry("1024x768")

    # Set initial theme
    switch_theme(root, theme='light')

    # Start with the Login Form from our reusable UI components
    login_frame = components.LoginForm(root, on_success=on_login_success)
    login_frame.pack(fill='both', expand=True)

    root.mainloop()
