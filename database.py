import sqlite3

def db_connect(db_name='db.sqlite'):
    # Opening database connection
    return sqlite3.connect(db_name)
    
def create_table(sql):
    """Function to create the database table if it does not exist"""
    db = db_connect()
    db.execute(sql)
    db.commit()

def read_db(sql, tbl_name):
    """Function to read the database"""
    db = db_connect()
    db = db.cursor()
    db.execute(sql, tbl_name)
    return db.fetchall()

def write_db(tbl_name, url, filename, duration, blocksize, startdatetime):
    '''Function to write data to database'''
    db = db_connect()
    db = db.cursor()
    sql = '''
        INSERT INTO %s(url, filename, duration, blocksize, startdatetime)
        VALUES (?,?,?,?,?)
    '''
    db.execute(sql % tbl_name, (url, filename, duration, blocksize, startdatetime))
    db.commit()

# Running the program
#if __name__ == '__main__':
    