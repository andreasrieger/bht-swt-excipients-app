import unittest

from users.app_user import AppUser


class TestAppUser(unittest.TestCase):
    def test_create_user(self):
        user = AppUser('Max', 'Muster', 'mmuster', 'mmuster@example.com')
        self.assertIsInstance(user, AppUser)


if __name__ == '__main__':
    unittest.main()
