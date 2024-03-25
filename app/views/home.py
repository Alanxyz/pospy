from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class HomeView(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.user_label = ttk.Label(self, text='Usuario', width=10, justify=LEFT)
        self.user_label.grid(column=0, row=1)

        self.user_entry = ttk.Entry(self)
        self.user_entry.grid(column=1, row=1, pady=5)

        self.user_label = ttk.Label(self, text='Contraseña', width=10, justify=LEFT)
        self.user_label.grid(column=0, row=2)

        self.password_entry = ttk.Entry(self, show='*')
        self.password_entry.grid(column=1, row=2, pady=5)

        self.convert_button = ttk.Button(
            self,
            command=self.try_login,
            text='Iniciar sesión'
        )
        self.convert_button.grid(column=1, row=3, sticky=NSEW, pady=5)

        self.grid(padx=40, pady=40, sticky=NSEW)

    def try_login(self):
        user = self.user_entry.get()
        password = self.password_entry.get()

        if user == 'Alan' and password == 'c':
            messagebox.showinfo('Información', 'Bienvenido')
        else:
            self.user_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
            messagebox.showerror('Error', 'Verifica el usuario y la contraseña.')

