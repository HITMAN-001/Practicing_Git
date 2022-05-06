import unittest
import Flatmate_Billing


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        Flatmate_Billing.Flatmate("Rohan", 30)
        Flatmate_Billing.Flatmate("Toyas", 30)
        Flatmate_Billing.Flatmate("Abhishek", 30)
        Flatmate_Billing.Category("Electricity", 2000)
        Flatmate_Billing.Category("Sweeping", 1000)
        Flatmate_Billing.Category("Food", 4000)
        Flatmate_Billing.Category("Entertainment", 2000)
        Flatmate_Billing.Category("Rent", 15000)

    def test_add_flatmate(self):
        self.assertEqual(len(Flatmate_Billing.Flatmate.flatmates), 3)  # add assertion here

    def test_add_categories(self):
        self.assertEqual(len(Flatmate_Billing.Category.all_categories), 5)

    def test_generate_bill(self):
        Flatmate_Billing.Bill()
        Flatmate_Billing.PDFReport.create_pdf(Flatmate_Billing.Flatmate.flatmates,
                                              Flatmate_Billing.Category.all_categories)


if __name__ == '__main__':
    unittest.main()
