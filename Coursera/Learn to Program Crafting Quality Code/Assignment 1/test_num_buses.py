import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    
    def test_exactly_50(self):
        """
        This test tells us if the function works normally when the amount of people is EXACTLY 50
        """
        expected = 1
        actual = a1.num_buses(50)
        
        self.assertEqual(expected, actual)
        
    def test_one(self):
        """
        This test checks the function when there are exactly 1 person
        """
        expected = 1
        actual = a1.num_buses(1)
        
        self.assertEqual(expected, actual)

    def test_zero(self):
        """
        This test tells us if it will behave normally when 0 is passed in
        """
        
        expected = 0
        actual = a1.num_buses(0)
        
        self.assertEqual(expected, actual)
        
    def test_more_than_50(self):
        """
        Tests when the amount of people is more than 50, e.g. 85
        """
        
        expected = 2
        actual = a1.num_buses(85)
        
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
