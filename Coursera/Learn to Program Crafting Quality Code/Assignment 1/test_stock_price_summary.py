import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    
    def test_empty_list(self):
        """
        Tests the function's behavior when an empty list is passed in
        """
        
        expected = (0, 0)
        actual = a1.stock_price_summary([])
        
        self.assertEqual(expected, actual)
        
    def test_single_positive(self):
        """
        Tests the function's behavior when only one positive element is seen in the list
        """
        expected = (0.5, 0)
        actual = a1.stock_price_summary([0.5])
        
        self.assertEqual(expected, actual)
        
    def test_single_negative(self):
        """
        Tests when only a single negative is in the list
        """
        expected = (0, -0.5)
        actual = a1.stock_price_summary([-0.5])
        
        self.assertEqual(expected, actual)
        
    def test_single_zero(self):
        """
        Tests the function when only a single zero is included in the list
        """
        expected = (0, 0)
        actual = a1.stock_price_summary([0])
        
    def test_all_positive(self):
        """
        Tests the result when all numbers in the list are positive
        """
        
        expected = (1.5, 0)
        actual = a1.stock_price_summary([0.1, 0.2, 0.3, 0.4, 0.5])
        
        self.assertEqual(expected, actual)
        
    def test_all_negative(self):
        """
        Tests the result when all numbers in the list are negative
        """
        
        expected = (0, -1.5)
        actual = a1.stock_price_summary([-0.1, -0.2, -0.3, -0.4, -0.5])
        
        self.assertEqual(expected, actual)
        
    def test_zero(self):
        """
        Tests the result when the list of numbers being passed in are all 0
        """
        
        expected = (0, 0)
        actual = a1.stock_price_summary([0, 0, 0, -0, -0, 0])
        
        self.assertEqual(expected, actual)
        
    def test_combined(self):
        """
        Tests the function's behavior when the tests above are combined
        """

        expected = (1.5, -1.5)
        actual = a1.stock_price_summary([1, -1, 0, 0, -0.5, 0.5])
        
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main(exit=False)
