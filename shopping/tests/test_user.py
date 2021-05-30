import unittest

from returns.maybe import Nothing

from shopping.address import get_street_address
from shopping.order import User, Order


class UserTest(unittest.TestCase):
    def test_user(self):
        empty_address = Order(User(None))
        self.assertEqual(get_street_address(empty_address), Nothing)


if __name__ == '__main__':
    unittest.main()
