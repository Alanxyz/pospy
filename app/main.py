from tkinter import *
import ttkbootstrap as ttk

from views.multiple import MultiView

if __name__ == "__main__":
    root = ttk.Window(themename='flatly')
    root.title('Inventopy')
    root.resizable(True, True)
    MultiView(root).pack(side='top', fill='both', expand=True)
    root.mainloop()

