class AppModules:
    app_modules_list = []

    def __init__(self, app_modules_list):
        self.app_modules_list = app_modules_list

    def add_app_module(self, app_module):
        self.app_modules_list.append(app_module)
        return True

    def find_app_module(self, app_module_name):
        lst = self.app_modules_list
        for m in lst:
            if m.name == app_module_name:
                return True
        return False

    # Method to remove an app module from the list
    # Raises an exception if module is not in list
    # String app_module_name: App module name to be removed
    def remove_app_module(self, app_module_name):
        return self.app_modules_list.remove(app_module_name)

    def clear_app_modules(self):
        return self.app_modules_list.clear()

    def get_app_modules_names(self):
        lst = self.app_modules_list
        lst2 = []
        for m in lst:
            lst2.append(m.name)
        return lst2

    def get_app_modules_list_length(self):
        return len(self.app_modules_list)
