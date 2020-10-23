import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod1 = Product('Test Product1')
        self.assertEqual(prod1.weight, 20)

    def test_product_stealability_explode(self):
        prod2 = Product('Test Product2', 35, 10, 2)
        actual1 = prod2.stealability()
        actual2 = prod2.explode()
        expected1 = "Very stealable!"
        expected2 = '...boom!'
        self.assertEqual(actual1, expected1)
        self.assertEqual(actual2, expected2)


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        """checks that it really does receive a list of
        length 30 """
        l1 = generate_products()
        actual = len(l1)
        expected = 30
        self.assertEqual(actual, expected)

    def test_legal_names(self):
        l1 = generate_products()
        for i in l1:
            txt = i.name.split()
            str1 = txt[0][2:-2]
            str2 = txt[1][2:-2]
            self.assertIn(str1, ADJECTIVES, msg=None)
            self.assertIn(str2, NOUNS, msg=None)

if __name__ == '__main__':
    unittest.main()
