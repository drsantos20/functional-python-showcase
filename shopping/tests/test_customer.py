import unittest

from shopping.user.customer import Customer


class CustomerTest(unittest.TestCase):
    def test_customer(self):
        customer = Customer(name='daniel', joined_at=None, username='drsantos20', email='daniel@gmail.com')

        self.assertEqual(customer.name, 'daniel')
        self.assertEqual(customer.username, 'drsantos20')
        self.assertEqual(customer.email, 'daniel@gmail.com')
        self.assertIsNone(customer.joined_at)


if __name__ == '__main__':
    unittest.main()
