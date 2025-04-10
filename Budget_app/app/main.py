# app/main.py
import tkinter as tk
from tkinter import messagebox
from app.auth import AuthManager
from app.manager import BudgetManager
from ui.components import LoginForm
from ui.dashboard import DashboardFrame
from data.database import Database

def switch_theme(root, theme='light'):
    """
    Dynamically load theme settings from a CSS-like file and apply them.
    (Note: Tkinter does not support CSS natively so this is just a demonstration.)
    """
    try:
        with open(f'ui/styles/{theme}.css', 'r') as f:
            styles = f.read()
            # Parse styles if desired and apply to widgets.
            print(f"Applying theme: {theme}")
    except Exception as e:
        messagebox.showerror("Theme Error", f"Error loading theme: {e}")

class Application:
    """
    Main application class that initializes the Tkinter window and manages UI transitions.
    """
    def __init__(self):
        # Initialize the database (create tables if they don’t exist)
        Database.initialize_db()
        
        # Create the root window
        self.root = tk.Tk()
        self.root.title("Budget Management Application")
        self.root.geometry("1024x768")
        switch_theme(self.root, theme='light')

        # Initialize authentication manager
        self.auth_manager = AuthManager()

        # Start the login process
        self.load_login()

    def load_login(self):
        """
        Display the login form.
        """
        self.clear_window()
        login_form = LoginForm(self.root, on_success=self.on_login_success, auth_manager=self.auth_manager)
        login_form.pack(fill='both', expand=True)

    def on_login_success(self, user):
        """
        Callback after successful login. Launch the dashboard.
        """
        self.clear_window()
        dashboard_frame = DashboardFrame(self.root, user)
        dashboard_frame.pack(fill='both', expand=True)

    def clear_window(self):
        """
        Remove all widgets from the root window.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        """
        Run the Tkinter main loop.
        """
        self.root.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()
