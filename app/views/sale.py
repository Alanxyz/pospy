from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

from core import api

class SaleView(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.items_in_cart = []

        self.cart = ttk.Frame(self)
        self.search = ttk.Frame(self)

        self.search_entry = ttk.Entry(self.search)
        self.search_entry.pack(side=TOP, fill=X)

        self.cart_list = ttk.Treeview(self.cart, columns=('name', 'quantity', 'price'), show='headings')
        self.cart_list.heading('name', text='Nombre')
        self.cart_list.heading('quantity', text='Cantidad')
        self.cart_list.heading('price', text='Precio')

        self.total_label = ttk.Label(self.cart, text='Total: $434', font=('TkDefaultFixed', 15))
        self.register_button = ttk.Button(self.cart, text='Registrar', bootstyle='success')

        self.items_list = ttk.Treeview(self.search, columns=('name', 'stock'), show='headings')
        self.items_list.heading('name', text='Nombre')
        self.items_list.heading('stock', text='Stock')

        self.search.grid(column=0, row=0)
        self.items_list.pack(side=TOP)

        self.cart.grid(column=1, row=0)
        self.cart_list.pack(side=TOP)
        self.cart_list.pack(side=TOP)
        self.register_button.pack(side=BOTTOM, fill=X, pady=10)
        self.total_label.pack(side=BOTTOM, fill=X, pady=10)

        self.pack(side=LEFT, fill=Y, expand=True, padx=30)
        self.load_data()

    def load_data(self):
        self.items = api.get_all_items()
        self.items_list.delete(*self.items_list.get_children())
        for item in self.items:
            self.items_list.insert('', END, values=(item['name'], item['stock']))

