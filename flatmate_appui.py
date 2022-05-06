import tkinter as tk
from tkinter import ttk
import Flatmate_Billing

root = tk.Tk()
root.geometry("300x200")
flatmate_name_gl = "Upcoming tk obj"
flatmate_days_gl = "Upcoming tk obj"
category_name_gl = "Upcoming tk obj"
category_amount_gl = "Upcoming tk obj"

flatmate_counter = 0
category_counter = 0


def add_flatmate():
    global flatmate_counter
    Flatmate_Billing.Flatmate(flatmate_name_gl.get(1.0, "end-1c"), flatmate_days_gl.get(1.0, "end-1c"))
    print("Added flatmate successfully {} {}".format(Flatmate_Billing.Flatmate.flatmates[flatmate_counter].name, Flatmate_Billing.Flatmate.flatmates[0].days_in_house))
    flatmate_counter = flatmate_counter + 1
    return


def add_category():
    global category_counter
    Flatmate_Billing.Category(category_name_gl.get(1.0, "end-1c"), category_amount_gl.get(1.0, "end-1c"))
    print("Added Category successfully {} {}".format(Flatmate_Billing.Category.all_categories[category_counter].name, Flatmate_Billing.Category.all_categories[0].category_amount))
    category_counter = category_counter + 1
    return


def calculate_bill():
    global root
    Flatmate_Billing.Bill.new_calculate_bill()
    Flatmate_Billing.PDFReport.create_pdf(Flatmate_Billing.Flatmate.flatmates, Flatmate_Billing.Category.all_categories)
    tk.Label(root, text="This is confirmation of bill generated")


# create fun for adding flatmate
def add_flatmate_ui():
    global flatmate_name_gl, flatmate_days_gl
    flatmate_addition = tk.Tk()
    name_lbl = tk.Label(flatmate_addition, text="Flatmate Name:")
    flatmate_name = tk.Text(flatmate_addition, width=20, height=2)
    flatmate_name_gl = flatmate_name
    days_lbl = tk.Label(flatmate_addition, text="Days in house:")
    flatmate_days = tk.Text(flatmate_addition, width=20, height=2)
    flatmate_days_gl = flatmate_days
    name_lbl.pack()
    flatmate_name.pack()
    days_lbl.pack()
    flatmate_days.pack()


    add_button = ttk.Button(flatmate_addition, text="Add Flatmate",
                            command=add_flatmate)
    add_button.pack()
    ttk.Button(flatmate_addition, text="Close this", command=flatmate_addition.destroy).pack()


def add_category_ui():
    global category_name_gl, category_amount_gl
    category_addition = tk.Tk()

    category_name_lbl = tk.Label(category_addition, text="Category Name:")
    cat_name_txt = tk.Text(category_addition, width=20, height=2)
    category_name_gl = cat_name_txt

    category_amount_lbl = tk.Label(category_addition, text="Amount Spent:")
    category_amount_txt = tk.Text(category_addition, width=20, height=2)
    category_amount_gl = category_amount_txt

    category_name_lbl.pack()
    cat_name_txt.pack()
    category_amount_lbl.pack()
    category_amount_txt.pack()

    add_button = ttk.Button(category_addition, text="Add Category",
                            command=add_category)
    add_button.pack()
    ttk.Button(category_addition, text="Close this", command=category_addition.destroy).pack()


# create function for adding categories
def add_categories():
    Flatmate_Billing.Category(input("Enter name of category"),
                              int(input("Enter the total amount spent for this category")))
    print("Category added successfully")
    return



add_flatmate_button = ttk.Button(root, text="Add Flatmate", command=add_flatmate_ui)
add_flatmate_button.grid(padx=100, pady=20)


add_category_button = ttk.Button(root, text="Add Category", command=add_category_ui)
add_category_button.grid(padx=100, pady=20)


calculate_bill = ttk.Button(root, text="Calculate Bill", command=calculate_bill)
calculate_bill.grid(padx=100, pady=20)


root.mainloop()
