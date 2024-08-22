import sqlite3
from types import NoneType
import pandas


class ConnectionWithDB:

    connect = None
    cursor = None

    def __init__(self):
        self.connect = sqlite3.connect("users_data.db")
        self.cursor = self.connect.cursor()

    def __del__(self):
        self.cursor.close()
        self.connect.commit()
        self.connect.close()
        print("Connection with DB closed")

    def get_user_data(self, user_id):
        query_result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
        if type(query_result[1]) == NoneType:
            return f"ФИО - None\n"\
                f"город - None\n"\
                f"универ - None\n"\
                f"факультет - None\n"\
                f"специальность - None\n"\
                f"финансирование - None\n"\
                f"форма обучения - None"
        return f"ФИО - {query_result[1]}\n"\
            f"город - {query_result[2]}\n"\
            f"универ - {query_result[3]}\n"\
            f"факультет - {query_result[4]}\n"\
            f"специальность - {query_result[5]}\n"\
            f"финансирование - {query_result[6]}\n"\
            f"форма обучения - {query_result[7]}"

    def is_user_in_db(self, user_id):
        return self.cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,)).fetchone()

    def is_value_in_db(self, user_id, value):
        return self.cursor.execute(f"SELECT * FROM users WHERE user_id = ? AND {value} <> 'None'", (user_id,)).fetchone()

    def add_user_to_db(self, user_id):
        if not self.is_user_in_db(user_id):
            self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
            print(f"{user_id} ДОБАВЛЕН В БАЗУ")
            print(pandas.read_sql("SELECT * FROM users", self.connect) , "\n")
        else: 
            print(f"{user_id} УЖЕ В БАЗЕ")

    def add_value_to_db(self, user_id, category, value):
        self.cursor.execute(f"UPDATE users SET {category} = ? WHERE user_id = ?", (value, user_id))
        if category != "selected_category":
            print(pandas.read_sql("SELECT * FROM users", self.connect), "\n")

    def get_selected_category(self, user_id):
        quer_res = self.cursor.execute("SELECT selected_category FROM users WHERE user_id = ?", (user_id,)).fetchone()[0]
        return quer_res


connect = ConnectionWithDB()
