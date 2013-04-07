import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.

    def test_stock_price_summary_with_empty_list(self):
        """ Test stock_price_summary with an empty list """

        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)
    
    def test_stock_price_summary_with_list_containing_one_positive_eliment(self):
        """ Test stock_price_summary with a list containing one positive element """

        actual = a1.stock_price_summary([0.11])
        expected = (0.11, 0)
        self.assertEqual(actual, expected)
    
    def test_stock_price_summary_with_list_containing_one_negative_eliment(self):
        """ Test stock_price_summary with a list containing one negative element """

        actual = a1.stock_price_summary([-0.5])
        expected = (0, -0.5)
        self.assertEqual(actual, expected)
    
    def test_stock_price_summary_with_list_containing_one_positive_and_one_negative_elements(self):
        """ Test stock_price_summary with a list containing one positive and one negative elements """

        actual = a1.stock_price_summary([0.03, -0.02])
        expected = (0.03, -0.02)
        self.assertEqual(actual, expected)
    
    def test_stock_price_summary_with_list_containing_positive_and_negative_eliments(self):
        """ Test stock_price_summary with a list containing positive and negative elements """

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)

