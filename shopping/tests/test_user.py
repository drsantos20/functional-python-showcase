import unittest

from shopping.user.user import User


class UserTest(unittest.TestCase):
    def test_user(self):
        user = User(name='daniel', username='drsantos20', email='daniel@gmail.com')
        self.assertEqual(user.name, 'daniel')
        self.assertEqual(user.username, 'drsantos20')
        self.assertEqual(user.email, 'daniel@gmail.com')


if __name__ == '__main__':
    unittest.main()
