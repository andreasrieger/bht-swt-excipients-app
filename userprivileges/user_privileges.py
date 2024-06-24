import sqlite3


def create_table(app_module_name=None):
    sql = """
        CREATE TABLE if not exists %s (
                  id INTEGER PRIMARY KEY,
                  app_module VARCHAR(30),
                  privileges VARCHAR(30)
              );
        """
    db = sqlite3.connect('db.sqlite')
    c = db.cursor()
    c.execute(sql % app_module_name)
    db.commit()


def user_privileges_list(app_module_name=None):
    create_table(app_module_name)
    sql = '''
        SELECT * FROM %s
    '''
    db = sqlite3.connect('db.sqlite')
    c = db.cursor()
    c.execute(sql % app_module_name)
    db.commit()


class UserPrivileges:
    app_module_name = 'user_privileges'

