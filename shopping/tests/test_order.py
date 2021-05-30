import unittest

from returns.maybe import Nothing

from shopping.address import get_street_address
from shopping.order import Order


class OrderTest(unittest.TestCase):
    def test_order(self):
        empty_user = Order(None)
        self.assertEqual(get_street_address(empty_user), Nothing)


if __name__ == '__main__':
    unittest.main()
