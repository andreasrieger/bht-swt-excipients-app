import unittest
from unittest.mock import patch, Mock

from users.app_user import AppUser
from users.app_users import AppUsers


class TestAppUsers(unittest.TestCase):

    def setUp(self):
        """Setting up tests environment"""
        self.app_users = AppUsers()
        self.assertIsInstance(self.app_users, AppUsers)

    # def test_add_app_user(self):
    #     """Adding new user"""
    #     self.app_user = AppUser('Max', 'Muster', 'mmuster', 'mmuster@example.com')
    #     self.assertTrue(self.app_users.add_app_user(self.app_user))

    # @patch('users.AppUser')
    def test_add_app_user(self):
        """Adding new user with Mock"""
        self.app_users = Mock()
        self.app_users.add_app_user.return_value = True
        self.app_user = AppUser('Max', 'Muster', 'mmuster', 'mmuster@example.com')
        self.assertTrue(self.app_users.add_app_user(self.app_user))


if __name__ == '__main__':
    unittest.main()
