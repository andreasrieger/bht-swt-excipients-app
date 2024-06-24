import sqlite3

db_name = 'db.sqlite'


def check_table(self):
    db = sqlite3.connect(db_name)

def create_table(sql):
    """Function to create the database table if it does not exist"""

    # Opening database connection and writing data to database.
    db = sqlite3.connect(db_name)

    c = db.cursor()
    c.execute(sql)
    db.commit()


def read_db(sql, tbl_name):
    """Function to read the database"""

    # Opening database connection and writing data to database.
    db = sqlite3.connect(db_name)

    c = db.cursor()
    c.execute(sql, tbl_name)
    return c.fetchall()


def write_db(db, url, filename, duration, blocksize, startdatetime):
    '''Function to write data to database'''

    c = db.cursor()
    sql = '''
        INSERT INTO recordings(url, filename, duration, blocksize, startdatetime)
        VALUES (?,?,?,?,?)
    '''
    c.execute(sql, (url, filename, duration, blocksize, startdatetime))
    db.commit()

# Running the program
if __name__ == '__main__':
    create_table()
