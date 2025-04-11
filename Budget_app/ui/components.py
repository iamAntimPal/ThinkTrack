# ui/components.py
import tkinter as tk
from tkinter import messagebox
from app.auth import AuthManager

class BaseFrame(tk.Frame):
    """
    Base frame with common padding.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(padx=10, pady=10)

class LoginForm(BaseFrame):
    """
    Login form for user authentication.
    """
    def __init__(self, master, on_success, auth_manager: AuthManager, **kwargs):
        super().__init__(master, **kwargs)
        self.on_success = on_success
        self.auth_manager = auth_manager
        self.build_form()

    def build_form(self):
        tk.Label(self, text="Login", font=("Arial", 20)).pack(pady=10)
        self.username_entry = tk.Entry(self)
        self.username_entry.insert(0, "Username")
        self.username_entry.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.insert(0, "Password")
        self.password_entry.pack(pady=5)
        tk.Button(self, text="Login", command=self.authenticate).pack(pady=10)
        tk.Button(self, text="Register", command=self.register).pack(pady=5)

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.auth_manager.login_user(username, password)
        if user:
            messagebox.showinfo("Success", "Login successful!")
            self.on_success(user)
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.auth_manager.register_user(username, password):
            messagebox.showinfo("Success", "Registration successful!")
        else:
            messagebox.showerror("Error", "Registration failed. Username may already exist.")

class MainMenu(BaseFrame):
    """
    Main menu with navigation options and a dark/light theme toggle button.
    """
    def __init__(self, master, user, on_nav, on_toggle, **kwargs):
        super().__init__(master, **kwargs)
        self.user = user
        self.on_nav = on_nav
        self.on_toggle = on_toggle
        self.build_menu()

    def build_menu(self):
        welcome = f"Welcome, {self.user['username']}"
        tk.Label(self, text=welcome, font=("Arial", 18)).pack(pady=10)
        
        # Navigation buttons
        options = ["Dashboard", "Add Entry", "Reports", "Logout"]
        for option in options:
            tk.Button(self, text=option, width=20, command=lambda opt=option: self.on_nav(opt)).pack(pady=5)
        
        # Theme toggle button
        tk.Button(self, text="Toggle Theme", width=20, command=self.on_toggle).pack(pady=15)
