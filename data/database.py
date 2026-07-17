import sqlite3


class DataManager:
    def __init__(self, database_path):
        self.database_path = database_path
        self.conn = None
        self.cursor = None
        self.__create_table()

    def __connect(self):
        try:
            self.conn = sqlite3.connect(self.database_path)
            self.cursor = self.conn.cursor()
            self.cursor.execute("PRAGMA foreign_keys = ON;")
        except sqlite3.Error as e:
            print(f"Error Connecting to databases: {e}")

    def __create_table(self):
        self.__connect()
        self.cursor.execute("""CREATE TABLE if not exists users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            lastname TEXT NOT NULL,
            city TEXT NOT NULL,
            phone TEXT NOT NULL,
            e_mail TEXT NOT NULL UNIQUE,
            summary TEXT NOT NULL,
            github TEXT,
            linkedin TEXT)""")

        self.cursor.execute("""CREATE TABLE if not exists hobbies(
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            name TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
            )""")

        self.cursor.execute("""CREATE TABLE if not exists experiendces(
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            name TEXT,
            position TEXT,
            time TEXT,
            description TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
            )""")

        self.cursor.execute("""CREATE TABLE if not exists skills(
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            name TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
            )""")
        self.conn.commit()
        self.conn.close()
