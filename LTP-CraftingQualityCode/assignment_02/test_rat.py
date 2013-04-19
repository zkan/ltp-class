import a2
import unittest

class TestInitializeRat(unittest.TestCase): 
    """ Test class for method a2. """ 

    def test_init_rat(self): 
        """ Test __init__ with symbol 'P' at the location (1, 4) """

        actual = a2.Rat('P', 1, 4)
        expected_symbol = 'P'
        expected_row = 1
        expected_col = 4
        expected_num_sprouts_eaten = 0

        self.assertEqual(expected_symbol, actual.symbol)
        self.assertEqual(expected_row, actual.row)
        self.assertEqual(expected_col, actual.col)
        self.assertEqual(expected_num_sprouts_eaten, actual.num_sprouts_eaten)


if __name__ == '__main__':
    unittest.main(exit=False)
