# ui/dashboard.py
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class DashboardFrame(tk.Frame):
    """
    Main dashboard frame displaying summaries and charts.
    """
    def __init__(self, master, user, **kwargs):
        super().__init__(master, **kwargs)
        self.user = user
        self.build_dashboard()

    def build_dashboard(self):
        tk.Label(self, text=f"Welcome, {self.user['username']}", font=('Arial', 16)).pack(pady=10)
        
        # Create a frame for charts
        chart_frame = tk.Frame(self)
        chart_frame.pack(fill='both', expand=True)
        
        # Sample data for demonstration
        categories = ['Food', 'Rent', 'Entertainment']
        amounts = [250, 800, 150]

        fig, ax = plt.subplots(figsize=(4, 3))
        ax.pie(amounts, labels=categories, autopct='%1.1f%%')
        ax.set_title("Expense Breakdown")

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
