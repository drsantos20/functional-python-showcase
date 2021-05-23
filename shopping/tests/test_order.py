import unittest

from returns.maybe import Some

from shopping.order.order import Order
from shopping.user.wallet import Wallet


class UserOrder(unittest.TestCase):
    def test_order(self):
        order = Order(total_value=100)
        user = Wallet(name='daniel', username='drsantos20', email='daniel@gmail.com', funds=100)
        # self.assertEqual(order.pay_order(user), 0)
        self.assertEqual(order.pay_order(user), Some(0))


if __name__ == '__main__':
    unittest.main()
