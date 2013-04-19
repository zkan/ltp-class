import a2
import unittest

class TestRatMethods(unittest.TestCase): 
    """ Test class for methods in class Rat. """ 

    def test_init_rat(self): 
        """ Test __init__ with symbol 'P' at the location (1, 4). """

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
        """ Test set_location to be at (2, 3). """

        rat = a2.Rat('P', 1, 4)
        rat.set_location(2, 3)
        actual_row = rat.row
        actual_col = rat.col
        expected_row = 2
        expected_col = 3

        self.assertEqual(expected_row, actual_row)
        self.assertEqual(expected_col, actual_col)

    def test_eat_sprout(self):
        """ Test eat_sprout, so the number of sprouts eaten 
        increases by one for the particular rat. """

        rat = a2.Rat('P', 1, 4)
        rat.eat_sprout()
        actual_num_sprouts_eaten = rat.num_sprouts_eaten
        expected_num_sprouts_eaten = 1

        self.assertEqual(expected_num_sprouts_eaten, actual_num_sprouts_eaten)

    def test_str_repr(self):
        """ Test the string representation of the rat. Suppose we have P at (1, 4) 
        ate 2 sprouts. """

        rat = a2.Rat('P', 1, 4)
        rat.eat_sprout()
        rat.eat_sprout()
        actual = rat.__str__()
        expected = 'P at (1, 4) ate 2 sprouts.'

        self.assertEqual(expected, actual)
    

if __name__ == '__main__':
    unittest.main(exit=False)
