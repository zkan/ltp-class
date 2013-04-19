import a2
import unittest

class TestRatMethods(unittest.TestCase): 
    """ Test class for methods in class Rat """ 

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

    def test_set_location(self):
        """ Test set_location to be at (2, 3) """

        rat = a2.Rat('P', 1, 4)
        rat.set_location(2, 3)
        actual_row = rat.row
        actual_col = rat.col
        expected_row = 2
        expected_col = 3

        self.assertEqual(expected_row, actual_row)
        self.assertEqual(expected_col, actual_col)


if __name__ == '__main__':
    unittest.main(exit=False)
