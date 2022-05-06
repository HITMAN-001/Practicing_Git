from datetime import date


class Flatmate:
    flatmates = []

    def __init__(self, name, days_in_house=30):
        self.name = name
        self.categorical_bill_amount = {}
        self.days_in_house = days_in_house
        self.set_flatmates()

    @staticmethod
    def get_flatmates():
        return Flatmate.flatmates

    def set_flatmates(self):
        Flatmate.flatmates.append(self)




class Category:
    all_categories = []

    def __init__(self, name, category_amount):
        self.name = name
        self.category_amount = category_amount
        Category.all_categories.append(self)




class Bill(Category, Flatmate):
    def __init__(self):
        self.__period = date.today()
        self.new_calculate_bill()

    def get_period(self):
        return self.__period

    @staticmethod
    def new_calculate_bill():
        total_days = 0
        for flatmate in Flatmate.flatmates:
            total_days = total_days + int(flatmate.days_in_house)

        for flatmate in Flatmate.flatmates:
            for category in Category.all_categories:
                flatmate.categorical_bill_amount[category.name] = round(
                            (int(flatmate.days_in_house) / int(total_days)) * int(category.category_amount), 2)
        Bill.get_bill()

    @staticmethod
    def get_bill():
        for flatmate in Flatmate.flatmates:
            print(flatmate.name, flatmate.categorical_bill_amount)


class PDFReport:
    # Python program to create
    # a pdf file
    @staticmethod
    def create_pdf(flatmates, categories):
        from fpdf import FPDF

        # save FPDF() class into a
        # variable pdf
        pdf1 = FPDF()

        # Add a page
        pdf1.add_page()

        # set style and size of font
        # that you want in the pdf
        pdf1.set_font("Arial", size=15)

        # create a cell
        pdf1.cell(196, 10, txt='The Bill for {}.'.format(date.today()),
                  ln=10, align='C', border=1)
        pdf1.cell(28, 10, txt='Category',
                  ln=0, align='L', border=1)
        for category in categories:
            pdf1.cell(28, 10, txt=str(category.name[:10]),
                      ln=0, align='L', border=1)
        pdf1.cell(28, 10, txt=str("Total"),
                  ln=0, align='L', border=1)
        pdf1.cell(28, 10, txt='',
                  ln=1, align='L')
        for flatmate in flatmates:
            total = 0
            pdf1.cell(28, 10, txt=str(flatmate.name),
                      ln=0, align='L', border=1)
            for category_value in flatmate.categorical_bill_amount.values():
                pdf1.cell(28, 10, txt=str(category_value),
                          ln=0, align='L', border=1)
                total = total + category_value
            pdf1.cell(28, 10, txt=str(total),
                      ln=0, align='L', border=1)
            pdf1.cell(28, 10, txt='',
                      ln=1, align='L')
        # save the pdf with name .pdf
        pdf1.output("Bill_{}.pdf".format(date.today()))




'''
rohan = Flatmate("Rohan")
toyas = Flatmate("Toyas")
abhi = Flatmate("Abhishek")
Category("Sweeper", 500)
Category("Electricity", 1000)
Category("Water Bill", 500)
Category("Rent", 15000)
Category("Food", 2500)
bill = Bill()
PDFReport.create_pdf(Flatmate.flatmates, Category.all_categories)
'''