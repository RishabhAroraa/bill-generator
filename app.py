# author: rishabharoraa.github.io
from tkinter import *
from tkinter import ttk

# basic configuration
window = Tk()
window.title("Bill generator")
window.geometry("480x640")


# labels and entries
product_ID = Label(window, text="Product ID: ").grid(column=0, row=0)
product_name = Label(window, text="Product Name: ").grid(column=0, row=1)
product_units = Label(window, text="Units: " ).grid(column=0, row=2)
product_price = Label(window, text="Amount: ").grid(column=0,row=3)

product_ID_entry = Entry(window).grid(column=1, row=0)
product_name_entry = Entry(window).grid(column=1, row=1)
product_units_entry = Entry(window).grid(column=1, row=2)
product_price_entry = Entry(window).grid(column=1, row=3)

# TODO :
# make a new Bill Object
# make a new Item Object when the button is clicked

add_item_button = ttk.Button(window, text="Add Item", command='add_item_button_clicked').grid(row=4,column=0)

window.mainloop()
