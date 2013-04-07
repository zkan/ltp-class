import a1
import unittest

class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.

    def test_num_buses_people_less_than_fifty(self):
        """ Test num_buses with the number of people less than 50 """

        actual = a1.num_buses(49)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_people_equal_fifty(self):
        """ Test num_buses with the number of people equal to 50 """

        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)
    
    def test_num_buses_people_greater_than_fifty(self):
        """ Test num_buses with the number of people greater than 50 """

        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(actual, expected)

    def test_num_buses_people_greater_than_hundred(self):
        """ Test num_buses with the number of people greater than 100 """

        actual = a1.num_buses(101)
        expected = 3
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)

