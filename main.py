import sqlite3

DB_PATH: str = '/Users/20684538/Library/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db'

def interract_with_db(
    dbpath: str,
) -> list:
    con = sqlite3.connect(dbpath)
    cur = con.cursor()

# Напишите SQL запрос в строке.
    cur.execute('''
        SELECT Name 
        FROM Track;
    ''')

    table = cur.fetchall()[0]
    

# Напишите SQL запрос в строке.
    results = cur.execute('SELECT Name FROM Track;')
    output = results.fetchall()
    con.close()
    return output

