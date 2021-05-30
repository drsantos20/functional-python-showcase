import unittest

from returns.maybe import Some, Nothing

from shopping.order import Order
from shopping.address import Address, get_street_address
from shopping.user import User


class AddressTest(unittest.TestCase):
    def test_address(self):
        with_address = Order(User(Address('Some street')))
        self.assertEqual(get_street_address(with_address), Some('Some street'))

    def test_empty_user_address(self):
        empty_street = Order(User(Address(None)))
        self.assertEqual(get_street_address(empty_street), Nothing)
