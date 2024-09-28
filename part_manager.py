import tkinter as tk
from tkinter import END, messagebox
from db import Database

db = Database('store.db')


def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    if part_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields!')
        return
    db.insert(part_text.get(), customer_text.get(),
              retailer_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), customer_text.get(),
                            retailer_text.get(), price_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    global selected_item
    index = parts_list.curselection()[0]
    selected_item = parts_list.get(index)

    part_entry.delete(0, END)
    part_entry.insert(END, selected_item[1])
    customer_entry.delete(0, END)
    customer_entry.insert(END, selected_item[2])
    retailer_entry.delete(0, END)
    retailer_entry.insert(END, selected_item[3])
    price_entry.delete(0, END)
    price_entry.insert(END, selected_item[4])


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], part_text.get(), customer_text.get(),
              retailer_text.get(), price_text.get())
    populate_list()


def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)


# tk._test()
# Create Window Object
app = tk.Tk()


# Part
part_text = tk.StringVar()
part_label = tk.Label(app, text='Part Name', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0)
part_entry = tk.Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1, sticky='W')

# Customer
customer_text = tk.StringVar()
customer_label = tk.Label(app, text='Customer', font=('bold', 14))
customer_label.grid(row=0, column=2)
customer_entry = tk.Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3, sticky='W')

# Retailer
retailer_text = tk.StringVar()
retailer_label = tk.Label(app, text='Retailer Name', font=('bold', 14))
retailer_label.grid(row=1, column=0)
retailer_entry = tk.Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1, sticky='W')

# Price
price_text = tk.StringVar()
price_label = tk.Label(app, text='Price', font=('bold', 14))
price_label.grid(row=1, column=2)
price_entry = tk.Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3, sticky='W')

# Parts List (ListBox)
parts_list = tk.Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3,
                rowspan=6, pady=20, padx=20, sticky='E')

# Create scrollbar
scrollbar = tk.Scrollbar(app)
scrollbar.grid(row=3, column=3, rowspan=6, pady=20, sticky='WNS')

# Set scrollbar to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = tk.Button(app, text='Add Part', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = tk.Button(app, text='Remove Part', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = tk.Button(app, text='Update Part', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = tk.Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)


app. geometry('700x350')
app.title("Simple App")

populate_list()
# populate_list()
# populate_list()

# Start Program
app.mainloop()
