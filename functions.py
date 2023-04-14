import sqlite3



def user_data_create(username, user_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        print("Подключен к SQLite user_data_create")
        cursor = sqlite_connection.cursor()
        sql_select_query = """select user_id from user_data"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        data = ()
        for row in records:
            data += (row[0],)
        if user_id not in data:
            data = (str(username),) + (str(user_id),) + ('NULL',) + ('NULL',)
            cursor.execute("INSERT INTO user_data VALUES(?, ?, ?, ?);", data)
            sqlite_connection.commit()
            cursor.close()
        else:
            user_data_update(user_id, username, restart=True)
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто user_data_create")


def user_data_update(user_id, username="NULL",  restart=False):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite user_data_update")
        if restart:
            print("restart")
            sql_update_query = """Update user_data set username = ? where user_id = ?"""
            data = (str(username), str(user_id))
            print(data)
            cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто user_data_update")


def get_user_data(user_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite get_user_data")
        sql_select_query = """select * from user_data where user_id = ?"""
        cursor.execute(sql_select_query, (str(user_id),))
        records = cursor.fetchall()
        return records[0][-2], records[0][-1]


    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто get_user_data")



def get_user_data_by_name(username):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite get_user_data_by_name")
        sql_select_query = """select * from user_data where username = ?"""
        cursor.execute(sql_select_query, (str(username[0:len(username)]),))
        records = cursor.fetchall()
        return records[0][-2]


    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто get_user_data_by_name")



def update_moder_data(username, state_to_set):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite update_moder_data")
        sql_update_query = """Update user_data set moder = ? where username = ?"""
        data = (str(state_to_set), str(username))
        print(data)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто update_moder_data")


def get_users_id():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite get_users_id")
        sql_select_query = """select user_id from user_data"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        return records
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто get_users_id")
