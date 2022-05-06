import Flatmate_Billing


# create fun for adding flatmate
def add_flatmate():
    Flatmate_Billing.Flatmate(input("Enter the name"), int(input("days in house")))
    print("Added flatmate successfully ")
    return


# create function for adding categories
def add_categories():
    Flatmate_Billing.Category(input("Enter name of category"),
                                         int(input("Enter the total amount spent for this category")))
    print("Category added successfully")
    return


# func for generating bill
def generate_bill():
    if len(Flatmate_Billing.Flatmate.flatmates) == 0:
        return "There is no one to share bill with"
    if len(Flatmate_Billing.Category.all_categories) == 0:
        return "There is no category added , Please add category "
    Flatmate_Billing.Bill(Flatmate_Billing.Flatmate.flatmates)
    Flatmate_Billing.PDFReport.create_pdf(Flatmate_Billing.Flatmate.flatmates,
                                          Flatmate_Billing.Category.all_categories)
    return "Bill Generated"


while True:
    inp = "0" + input("Hello there! Enter the action number, 1. Add Flatmate 2.Add category 3. Generate Bill")
    if len(inp) > 1:
        inp = int(inp[1:])
    elif len(inp) == 1:
        inp = int(inp)
    if inp == 1:
        add_flatmate()
    elif inp == 2:
        add_categories()
    elif inp == 3:
        print(generate_bill())
        break
    else:
        print("enter valid input")

