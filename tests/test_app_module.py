import unittest

from appmodules.app_module import AppModule


class TestAppModule(unittest.TestCase):
    def test_create_app_module(self):
        app_module = AppModule("Test App Module", "Testing App Module feature")
        self.assertIsInstance(app_module, AppModule)


if __name__ == '__main__':
    unittest.main()
