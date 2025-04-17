# app/main.py
import tkinter as tk
from tkinter import messagebox
from app.auth import AuthManager
from ui.components import LoginForm, MainMenu
from data.database import Database

def apply_theme(root, theme):
    """
    Applies the chosen theme by setting background colors.
    (This function reads from a dummy CSS file and then applies colors to the root widget.)
    """
    if theme == "dark":
        bg_color = "#2e2e2e"
        fg_color = "#ffffff"
    else:
        bg_color = "#ffffff"
        fg_color = "#000000"
    root.configure(bg=bg_color)
    # In a full implementation you could iterate over widgets.
    print(f"Applied {theme} theme.")

class Application:
    """
    Main application class.
    """
    def __init__(self):
        # Initialize CSV files if missing
        Database.initialize_csv_files()
        
        # Create the root window
        self.root = tk.Tk()
        self.root.title("Budget Management Application")
        self.root.geometry("1024x768")
        
        # Default theme (light)
        self.theme = "light"
        apply_theme(self.root, self.theme)
        
        self.auth_manager = AuthManager()
        self.user = None

        # Start with login
        self.load_login()

    def load_login(self):
        """
        Displays the login form.
        """
        self.clear_window()
        login_form = LoginForm(self.root, on_success=self.on_login_success, auth_manager=self.auth_manager)
        login_form.pack(fill="both", expand=True)

    def on_login_success(self, user):
        """
        Called on successful login; load the main menu.
        """
        self.user = user
        self.load_main_menu()

    def load_main_menu(self):
        """
        Displays the main menu containing navigation options and theme toggle.
        """
        self.clear_window()
        main_menu = MainMenu(self.root, self.user, on_nav=self.navigate, on_toggle=self.toggle_theme)
        main_menu.pack(fill="both", expand=True)

    def navigate(self, option):
        """
        Navigation function to load different screens based on the selected option.
        """
        self.clear_window()
        if option == "Dashboard":
            # Load Dashboard screen
            from ui.dashboard import DashboardFrame
            frame = DashboardFrame(self.root, self.user)
            frame.pack(fill="both", expand=True)
        elif option == "Add Entry":
            # Load Entry Form screen
            from ui.forms import EntryForm
            frame = EntryForm(self.root, self.user, on_submit=self.load_main_menu)
            frame.pack(fill="both", expand=True)
        elif option == "Reports":
            # Load Reports screen
            from ui.reports import ReportsFrame
            frame = ReportsFrame(self.root, self.user)
            frame.pack(fill="both", expand=True)
        elif option == "Logout":
            # Go back to login screen
            self.user = None
            self.load_login()
        else:
            messagebox.showerror("Error", "Option not implemented.")

    def toggle_theme(self):
        """
        Toggle between dark and light themes.
        """
        self.theme = "dark" if self.theme == "light" else "light"
        apply_theme(self.root, self.theme)
        # Refresh the current screen by reloading the main menu
        self.load_main_menu()

    def clear_window(self):
        """
        Clears all widgets from the root window.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()
