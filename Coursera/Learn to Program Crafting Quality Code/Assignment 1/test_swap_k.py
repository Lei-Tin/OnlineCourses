import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.

    def test_k_zero(self):
        """
        Tests the situation where k is equal to 0, i.e. No swap
        """
        k = 0
        L = [1, 2, 3, 4, 5, 6]
        expectedL = [1, 2, 3, 4, 5, 6]
        
        # Now the L is already swapped
        a1.swap_k(L, k)
        
        self.assertEqual(expectedL, L)
        
    def test_k_one(self):
        """
        Tests the situation when k is equal to 1, minimum based from the precondition except from 0
        """
        k = 1
        L = [1, 2, 3, 4, 5, 6]
        
        expectedL = [6, 2, 3, 4, 5, 1]
        
        a1.swap_k(L, k)
        
        self.assertEqual(expectedL, L)
        
    def test_empty_list(self):
        """
        Tests the case where the list provided is empty, k must be 0 based from the precondition, 0 <= k <= len(L) // 2
        """
        k = 0
        L = []
        
        expectedL = []
        
        a1.swap_k(L, k)
        
        self.assertEqual(expectedL, L)
        
    def test_k_max(self):
        """
        Tests the maximum value of k that is possible, k = len(L) // 2
        """
        L = [1, 2, 3, 4, 5, 6, 7]
        
        k = len(L) // 2
        
        expectedL = [5, 6, 7, 4, 1, 2, 3]
        
        a1.swap_k(L, k)
        
        self.assertEqual(expectedL, L)

    def test_list_even(self):
        """
        Tests the case where the list is even (len(L) % 2 == 0) and k is an arbitrary number        
        """
        k = 2
        L = [1, 2, 3, 4, 5, 6]
        
        expectedL = [5, 6, 3, 4, 1, 2]
        
        a1.swap_k(L, k)
        
        self.assertEqual(expectedL, L)
        
    
    def test_list_odd(self):
        """
        Tests the case where the list is odd (len(L) % 2 == 1) and k is an arbitrary number
        """
        k = 2
        L = [1, 2, 3, 4, 5, 6, 7]
        
        expectedL = [6, 7, 3, 4, 5, 1, 2]
        
        a1.swap_k(L, k)
        
        self.assertEqual(expectedL, L)

if __name__ == '__main__':
    unittest.main(exit=False)
