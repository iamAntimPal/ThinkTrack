# ui/reports.py
import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
from fpdf import FPDF

class ReportsFrame(tk.Frame):
    """
    Reporting interface that exports data to PDF or Excel.
    """
    def __init__(self, master, user, **kwargs):
        super().__init__(master, **kwargs)
        self.user = user
        self.build_ui()

    def build_ui(self):
        tk.Label(self, text="Reports", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="Export as PDF", command=self.export_pdf).pack(pady=5)
        tk.Button(self, text="Export as Excel", command=self.export_excel).pack(pady=5)

    def export_pdf(self):
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Budget Report", ln=True, align="C")
            file_path = filedialog.asksaveasfilename(defaultextension=".pdf")
            pdf.output(file_path)
            tk.messagebox.showinfo("Success", "Report exported to PDF successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error exporting PDF: {e}")

    def export_excel(self):
        try:
            data = {"Category": ["Food", "Rent", "Entertainment"], "Amount": [250, 800, 150]}
            df = pd.DataFrame(data)
            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
            df.to_excel(file_path, index=False)
            tk.messagebox.showinfo("Success", "Report exported to Excel successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error exporting Excel: {e}")
