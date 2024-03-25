
from tkinter import *
from tkinter import ttk
from .inventory import InventoryView
from .sale import SaleView

class MultiView(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)


        self.sidebar = ttk.Frame(self, bootstyle='primary')

        self.logo_label = ttk.Label(
            self.sidebar,
            text='INVENTOPY',
            bootstyle='primary-inverse',
            font=('TkDefaultFixed', 20)
        )
        self.go_to_new_sale_button = ttk.Button(
            self.sidebar,
            text='Caja',
            command=lambda: self.sale_view.tkraise()
        )
        self.go_to_inventory_button = ttk.Button(
            self.sidebar,
            text='Inventario',
            command=lambda: self.inventory_view.tkraise()
        )
        self.go_to_sales_button = ttk.Button(
            self.sidebar,
            text='Ventas',
            command=lambda: self.inventory_view.tkraise()
        )

        self.logo_label.pack(side=TOP, fill=X, padx=10, pady=10)
        self.go_to_new_sale_button.pack(side=TOP, fill=X, ipady=7)
        self.go_to_inventory_button.pack(side=TOP, fill=X, ipady=7)
        self.go_to_sales_button.pack(side=TOP, fill=X, ipady=7)

        self.inventory_view = InventoryView(self)
        #self.sale_view = SaleView(self)

        self.sidebar.pack(side=LEFT, fill=Y)
        self.inventory_view.pack(side=RIGHT, fill=Y, expand=True)
        #self.sale_view.pack(side=RIGHT, fill=Y, expand=True)


        self.pack()


