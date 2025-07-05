import tkinter as tk
from tkinter import scrolledtext

def load_logs(log_file):
    try:
        with open(log_file, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Log file not found."

class ProxyGUI:
    def __init__(self, root):
        root.title("Proxy Logs and Alerts")
        root.geometry("800x600")

        self.tabs = tk.ttk.Notebook(root)

        self.logs_tab = tk.Frame(self.tabs)
        self.alerts_tab = tk.Frame(self.tabs)

        self.tabs.add(self.logs_tab, text="Logs")
        self.tabs.add(self.alerts_tab, text="Alerts")
        self.tabs.pack(expand=1, fill="both")

        self.logs_text = scrolledtext.ScrolledText(self.logs_tab, wrap=tk.WORD)
        self.logs_text.pack(expand=True, fill='both')

        self.alerts_text = scrolledtext.ScrolledText(self.alerts_tab, wrap=tk.WORD)
        self.alerts_text.pack(expand=True, fill='both')

        self.refresh()

    def refresh(self):
        self.logs_text.delete(1.0, tk.END)
        self.alerts_text.delete(1.0, tk.END)
        self.logs_text.insert(tk.END, load_logs("logs.json"))
        self.alerts_text.insert(tk.END, load_logs("alerts.log"))
