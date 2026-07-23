import sqlite3


class DataManager:
    def __init__(self, database_path):
        self.database_path = database_path
        self.conn = None
        self.cursor = None
        self.__create_table()
        self.close()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.database_path)
            self.cursor = self.conn.cursor()
            self.cursor.execute("PRAGMA foreign_keys = ON;")
        except sqlite3.Error as e:
            print(f"Error Connecting to databases: {e}")

    def close(self):
        if self.conn:
            self.conn.close()

    def __create_table(self):
        self.connect()
        self.cursor.execute("""CREATE TABLE if not exists users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            lastname TEXT NOT NULL,
            city TEXT NOT NULL,
            phone TEXT NOT NULL,
            e_mail TEXT NOT NULL UNIQUE,
            summary TEXT NOT NULL,
            github TEXT,
            linkedin TEXT
            )""")

        self.cursor.execute("""CREATE TABLE if not exists education(
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            name TEXT NOT NULL,
            time TEXT NOT NULL,
            description TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
            )""")

        self.cursor.execute("""CREATE TABLE if not exists hobbies(
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            name TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
            )""")

        self.cursor.execute("""CREATE TABLE if not exists experiences(
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            time TEXT NOT NULL,
            description TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
            )""")

        self.cursor.execute("""CREATE TABLE if not exists skills(
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            name TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
            )""")
        self.conn.commit()
        self.close()
