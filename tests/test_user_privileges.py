import unittest

from userprivileges.user_privileges import UserPrivileges, user_privileges_list


class TestUserPrivileges(unittest.TestCase):
    def test_something(self):
        user_privileges = UserPrivileges()
        self.assertEqual(None, user_privileges_list('user_privileges'))


if __name__ == '__main__':
    unittest.main()
