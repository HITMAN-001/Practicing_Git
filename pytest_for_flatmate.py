import pytest
import Flatmate_Billing


@pytest.fixture
def input_value():
    input1 = [30,40,50]
    return input1


def test_input(input_value):
    assert input_value == [30,40,50]


@pytest.mark.one
def test_add_flatmate():
    Flatmate_Billing.Flatmate("Rohan", 30)
    Flatmate_Billing.Flatmate("Toyas", 30)
    Flatmate_Billing.Flatmate("Abhishek", 30)
    Flatmate_Billing.Category("Electricity", 2000)
    Flatmate_Billing.Category("Sweeping", 1000)
    Flatmate_Billing.Category("Food", 4000)
    Flatmate_Billing.Category("Entertainment", 2000)
    Flatmate_Billing.Category("Rent", 15000)
    assert len(Flatmate_Billing.Flatmate.flatmates) == 3  # add assertion here


if __name__ == '__main__':
    pytest.main()
