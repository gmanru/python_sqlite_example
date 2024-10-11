from sqlite3 import connect, Connection, Cursor

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


def print_beautifull_result(
    input_data
):
    output_data=''
    for data in input_data:
        output_data += data[0] + '\n'

    return output_data
     

def save_to_file(
    input_data,
    output_file_name,
):
    with open(output_file_name, 'w') as file_data:
        file_data.write(input_data)

def main():
    db_result: list = interract_with_db(
        dbpath=DB_PATH
    )
    result= print_beautifull_result(
        input_data=db_result
    )
    save_to_file(
        input_data=result,
        output_file_name='out.txt'
    )

main()

