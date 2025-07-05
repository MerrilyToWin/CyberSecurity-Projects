import tkinter as tk
import tkinter.ttk as ttk
from gui_viewer import ProxyGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = ProxyGUI(root)
    root.mainloop()
