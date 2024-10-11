from sqlite3 import Connection, Cursor, connect


DB_PATH: str = '/Users/20684538/Library/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db'


def _interact_with_db(
    database_path: str,
) -> list[tuple] | None:
    try:
        connection_with_db: Connection = connect(database_path)
        db_cursor: Cursor = connection_with_db.cursor()
        db_response: Cursor = db_cursor.execute('SELECT Name FROM Track;')
        function_output: list[tuple] = db_response.fetchall()
    except Exception as e:
        print(e)
        connection_with_db.close()
        return None

    return function_output


def _split_tracks_to_new_lines(
    input_data: list[tuple],
) -> str:
    output_data: str = ''
    for track in input_data:  # noqa: WPS519
        output_data += '{0}\n'.format(track[0])

    return output_data


def _save_to_file(
    input_data,
    output_file_name,
):
    with open(
        file=output_file_name,
        mode='w',
        encoding='utf-8',
    ) as file_data:
        file_data.write(input_data)


def main():
    """Функция для основной работы скрипта.

    Получем данные об именах песен из БД
    Сохраняем их в txt файл.
    """
    db_result: list[tuple] | None = _interact_with_db(database_path=DB_PATH)
    if db_result is None:
        print('failed script')
        return
    string_of_split_tracks: str = _split_tracks_to_new_lines(input_data=db_result)
    _save_to_file(input_data=string_of_split_tracks, output_file_name='out.txt')
    print('ok')


if __name__ == '__main__':
    main()
