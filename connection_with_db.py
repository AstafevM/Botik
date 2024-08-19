import sqlite3


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

    async def add_user_to_db(self, user_id):
        if not self.is_user_in_db(user_id):
            self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        else:
            print("User already in the DB")

    async def add_value_to_db(self, user_id, category, value):
        if self.is_user_in_db(user_id):
            self.cursor.execute(f"UPDATE users SET {category} = ? WHERE user_id = ?", (value, user_id))
        else:
            print("User is not in the DB")


connect = ConnectionWithDB()









