# ui/components.py
import tkinter as tk
from tkinter import messagebox
from app.auth import AuthManager

class BaseFrame(tk.Frame):
    """
    A base frame for common styling.
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
        tk.Label(self, text="Login", font=('Arial', 20)).pack(pady=10)
        
        self.username_entry = tk.Entry(self)
        self.username_entry.insert(0, "Username")
        self.username_entry.pack(pady=5)
        
        self.password_entry = tk.Entry(self, show='*')
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

"""
class RegisterForm(BaseFrame):
    """
    Registration form for new users.
    """
    def __init__(self, master, on_success, auth_manager: AuthManager, **kwargs):
        super().__init__(master, **kwargs)
        self.on_success = on_success
        self.auth_manager = auth_manager
        self.build_form()

    def build_form(self):
        tk.Label(self, text="Register", font=('Arial', 20)).pack(pady=10)
        
        self.username_entry = tk.Entry(self)
        self.username_entry.insert(0, "Username")
        self.username_entry.pack(pady=5)
"""      