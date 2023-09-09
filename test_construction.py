import unittest

from construction import House

class TestHouse(unittest.TestCase):
    
    def setUp(self):
        # Create a sample House instance for testing
        self.house = House(1234, "Meru", False, 150000, "Forthstreet", 3, 2, 2000)
    

    def test_calculate_property_tax(self):
        # Test the calculate_property_tax method
        tax_rate = 9  # Example tax rate (9%)
        expected_property_tax = (self.house._price * tax_rate) / 100
        self.assertEqual(self.house.calculate_property_tax(tax_rate), expected_property_tax)

    def test_estimate_utility_cost(self):
        # Test the estimate_utility_cost method
        expected_utility_cost = self.house.square_footage * 10  # Assuming Ksh.10 per square foot
        self.assertEqual(self.house.estimate_utility_cost(), expected_utility_cost)

    def test_inflation_coefficient(self):
        # Test the set_inflation_coefficient class method
        House.set_inflation_coefficient(6)
        self.assertEqual(House.inflation_coefficient, 6)

if __name__ == '__main__':
    unittest.main()

