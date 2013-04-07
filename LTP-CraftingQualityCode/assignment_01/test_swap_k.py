import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.

    def test_swap_k_with_empty_list(self):
        """ Test swap_k with an emply list """

        L = []
        L_expected = []
        a1.swap_k(L, 0)
        self.assertEqual(L, L_expected)
    
    def test_swap_k_with_list_containing_one_element(self):
        """ Test swap_k with a list containing one element with k = 0 and k = 1 """

        # k = 0
        L = [1]
        L_expected = [1]
        a1.swap_k(L, 0)
        self.assertEqual(L, L_expected)
        
        # k = 1
        L = [1]
        L_expected = [1]
        a1.swap_k(L, 1)
        self.assertEqual(L, L_expected)
    
    def test_swap_k_with_list_containing_even_num_of_elements(self):
        """ Test swap_k with a list containing even number of elements with k = 0, k = 1, and k = 2 """

        # k = 0
        L = [1, 2, 3, 4]
        L_expected = [1, 2, 3, 4]
        a1.swap_k(L, 0)
        self.assertEqual(L, L_expected)
        
        # k = 1
        L = [1, 2, 3, 4]
        L_expected = [4, 2, 3, 1]
        a1.swap_k(L, 1)
        self.assertEqual(L, L_expected)
        
        # k = 2
        L = [1, 2, 3, 4]
        L_expected = [3, 4, 1, 2]
        a1.swap_k(L, 2)
        self.assertEqual(L, L_expected)
    
    def test_swap_k_with_list_containing_odd_num_of_elements(self):
        """ Test swap_k with a list containing even number of elements with k = 0, k = 1, k = 2, and k = 3 """

        # k = 0
        L = [1, 2, 3, 4, 5, 6, 7]
        L_expected = [1, 2, 3, 4, 5, 6, 7]
        a1.swap_k(L, 0)
        self.assertEqual(L, L_expected)
        
        # k = 1
        L = [1, 2, 3, 4, 5, 6, 7]
        L_expected = [7, 2, 3, 4, 5, 6, 1]
        a1.swap_k(L, 1)
        self.assertEqual(L, L_expected)
        
        # k = 2
        L = [1, 2, 3, 4, 5, 6, 7]
        L_expected = [6, 7, 3, 4, 5, 1, 2]
        a1.swap_k(L, 2)
        self.assertEqual(L, L_expected)
        
        # k = 3
        L = [1, 2, 3, 4, 5, 6, 7]
        L_expected = [5, 6, 7, 4, 1, 2, 3]
        a1.swap_k(L, 3)
        self.assertEqual(L, L_expected)


if __name__ == '__main__':
    unittest.main(exit=False)

