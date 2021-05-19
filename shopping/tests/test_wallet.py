import unittest

from shopping.user.wallet import Wallet


class UserTest(unittest.TestCase):
    def test_user(self):
        user = Wallet(name='daniel', username='drsantos20', email='daniel@gmail.com', funds=30)
        self.assertEqual(user.name, 'daniel')
        self.assertEqual(user.username, 'drsantos20')
        self.assertEqual(user.email, 'daniel@gmail.com')
        self.assertEqual(user.funds, 30)

    def test_add_funds(self):
        user = Wallet(name='daniel', username='drsantos20', email='daniel@gmail.com', funds=0)
        self.assertEqual(user.funds, 0)
        user.add_funds(amount=10)
        self.assertEqual(user.funds, 10)


if __name__ == '__main__':
    unittest.main()
