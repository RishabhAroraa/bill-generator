# author: rishabharoraa.github.io
from tkinter import *
from tkinter import ttk

# basic configuration
window = Tk()
window.title("Bill generator")
window.geometry("480x640")
#window.configure(background="gray")

product_ID = Label(window, text="Product ID: ").grid(column=0, row=0)
product_name = Label(window, text="Product Name: ").grid(column=0, row=1)
product_units = Label(window, text="Units: " ).grid(column=0, row=2)
product_price = Label(window, text="Amount: ").grid(column=0,row=3)

product_ID_entry = Entry(window).grid(column=1, row=0)
product_name_entry = Entry(window).grid(column=1, row=1)
product_units_entry = Entry(window).grid(column=1, row=2)
product_price_entry = Entry(window).grid(column=1, row=3)

add_item_button = ttk.Button(window, text="Add Item").grid(row=4,column=0)

window.mainloop()
