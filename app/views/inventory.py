from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

from core import api

class InventoryView(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.name_label = ttk.Label(self, text='Nombre', justify=LEFT)
        self.name_label.grid(column=0, row=0, pady=5, padx=5)
        self.code_label = ttk.Label(self, text='Código', justify=LEFT)
        self.code_label.grid(column=0, row=1, pady=5, padx=5)
        self.stock_label = ttk.Label(self, text='Stock', justify=LEFT)
        self.stock_label.grid(column=0, row=2, pady=5, padx=5)

        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(column=1, row=0, pady=5, padx=5)
        self.code_entry = ttk.Entry(self)
        self.code_entry.grid(column=1, row=1, pady=5, padx=5)
        self.stock_entry = ttk.Entry(self)
        self.stock_entry.grid(column=1, row=2, pady=5, padx=5)

        self.add_button = ttk.Button( self,
            text='Agregar',
            command=self.add_entry
        )
        self.add_button.grid(column=2, row=0, sticky=NSEW, pady=5, padx=5)
        self.edit_button = ttk.Button(
            self,
            text='Editar',
            command=self.add_entry,
            bootstyle='info'
        )
        self.edit_button.grid(column=2, row=1, sticky=NSEW, pady=5, padx=5)
        self.delete_button = ttk.Button(
            self,
            text='Eliminar',
            command=self.delete_item,
            bootstyle='danger'
        )
        self.delete_button.grid(column=2, row=2, sticky=NSEW, pady=5, padx=5)


        self.table = ttk.Treeview(self, columns=('id', 'code', 'name', 'quantity'), show='headings', height=30)
        self.table.bind('<ButtonRelease-1>', self.select_item)

        self.table.grid(column=0, row=3, columnspan=3, pady=5, padx=5, sticky=NSEW)
        self.table.heading('id', text='Identificador')
        self.table.heading('code', text='Código')
        self.table.heading('name', text='Nombre')
        self.table.heading('quantity', text='Cantidad')

        self.pack(fill=Y, expand=True, padx=160)
        self.load_data()

    def clear_entries(self):
        self.name_entry.delete(0, END)
        self.code_entry.delete(0, END)
        self.stock_entry.delete(0, END)

    def load_data(self):
        self.items = api.get_all_items()

        self.table.delete(*self.table.get_children())
        for item in self.items:
            self.table.insert('', END, values=(item['id'], item['code'], item['name'], item['stock']))

    def add_entry(self):
        name = self.name_entry.get()
        code = self.code_entry.get()

        try:
            api.create_item(name, code)
        except:
            messagebox.showerror('Error', 'Ha ocurrido un error al intentar crear el elemento.')
        self.load_data()
        self.clear_entries()

    def select_item(self, e):
        focused = self.table.focus()
        element = self.table.item(focused)
        code = element['values'][1]
        name = element['values'][2]
        stock = element['values'][3]
        self.clear_entries()
        self.name_entry.insert(0, name)
        self.code_entry.insert(0, code)
        self.stock_entry.insert(0, stock)

    def delete_item(self):
        focused = self.table.focus()
        element = self.table.item(focused)
        id = element['values'][0]
        api.delete_item_by_id(id)
        self.load_data()
        self.clear_entries()

