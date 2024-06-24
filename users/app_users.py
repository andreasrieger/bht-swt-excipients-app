import sqlite3


def create_table(tbl_name):
    db = sqlite3.connect('db.sqlite')
    c = db.cursor()
    sql = """
        CREATE TABLE if not exists %s (
                  id INTEGER PRIMARY KEY,
                  name VARCHAR(30),
                  firstname VARCHAR(30),
                  username VARCHAR(30),
                  user_email VARCHAR(30)
              );
        """
    c.execute(sql % tbl_name)
    db.commit()


class AppUsers:

    def add_app_user(self, app_user):
        create_table('app_users')
        sql = """
                INSERT INTO app_users(name, firstname, username, user_email) 
                VALUES (?, ?, ?, ?)
            """
        db = sqlite3.connect('db.sqlite')
        c = db.cursor()
        c.execute(sql, (app_user.name, app_user.firstname, app_user.username, app_user.user_email))
        db.commit()
        return True
