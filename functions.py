import sqlite3



# def get_practise_task(task_id=-1):
#     try:
#         sqlite_connection = sqlite3.connect('sqlite_python.db')
#         cursor = sqlite_connection.cursor()
#         print("Подключен к SQLite")
#
#         sql_select_query = """select * from words where id = ?"""
#         if task_id == -1:
#             task_id = random.randint(0, 261)
#             cursor.execute(sql_select_query, (task_id,))
#             records = cursor.fetchall()
#             msg = ""
#             curr_right_variant_id = "0"
#             for row in records:
#                 msg += "Task №" + str(row[0]) + "\nWord: " + row[1].lower() + "\n1) " + row[2] + "\n2) " + row[3]
#                 if row[4] != "NULL":
#                     msg += "\n3) " + row[4]
#                 if row[5] != "NULL":
#                     msg += "\n4) " + row[5]
#                 curr_right_variant_id = row[6]
#             cursor.close()
#             return msg, curr_right_variant_id, task_id
#         else:
#             cursor.execute(sql_select_query, (task_id,))
#             records = cursor.fetchall()
#             msg = ""
#             curr_right_variant_id = "0"
#             for row in records:
#                 msg += "Task №" + str(row[0]) + "\nWord: " + row[1].lower() + "\n1) " + row[2] + "\n2) " + row[3]
#                 if row[4] != "NULL":
#                     msg += "\n3) " + row[4]
#                 if row[5] != "NULL":
#                     msg += "\n4) " + row[5]
#                 curr_right_variant_id = row[6]
#             cursor.close()
#             return msg, curr_right_variant_id, task_id
#
#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#     finally:
#         if (sqlite_connection):
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")
#

def user_data_create(username, user_id, task_status):
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
            data = (str(username),) + (str(user_id),) + (str(task_status),) + ('NULL',) + ('NULL',)
            cursor.execute("INSERT INTO user_data VALUES(?, ?, ?, ?, ?);", data)
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
        print(records)


    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто get_user_data")
