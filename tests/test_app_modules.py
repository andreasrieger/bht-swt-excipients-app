import unittest
from appmodules.app_module import AppModule
from appmodules.app_modules import AppModules


class TestAppModules(unittest.TestCase):

    def setUp(self):
        """Setting up tests environment"""
        self.app_modules = AppModules()
        self.assertIsInstance(self.app_modules, AppModules)
        self.assertEqual(None, self.app_modules.clear_app_modules())
        self.assertEqual(0, self.app_modules.get_app_modules_list_length())

    def test_add_app_module(self):
        """Adding app modules"""
        self.assertEqual(None, self.app_modules.clear_app_modules())
        self.assertTrue(self.app_modules.add_app_module(AppModule('Test', 'Testing')))
        self.assertNotEqual(0, self.app_modules.get_app_modules_list_length())

    def test_add_app_module_2(self):
        """Adding 2 app modules"""
        self.assertEqual(None, self.app_modules.clear_app_modules())
        self.assertTrue(self.app_modules.add_app_module(AppModule('Test', 'Testing')))
        self.assertTrue(self.app_modules.add_app_module(AppModule('Test 2', 'Testing')))
        self.assertEqual(2, self.app_modules.get_app_modules_list_length())

    def test_find_app_module_na(self):
        """Try to find module that does not exist"""
        self.assertFalse(self.app_modules.find_app_module('FooBarBaz'))

    def test_remove_app_module_na(self):
        """Try to remove module that does not exist"""
        self.assertRaises(ValueError, self.app_modules.remove_app_module, 'FooBarBaz')

    def tearDown(self):
        """Tear down tests environment"""
        self.assertEqual(None, self.app_modules.clear_app_modules())


if __name__ == '__main__':
    unittest.main(verbosity=2)
