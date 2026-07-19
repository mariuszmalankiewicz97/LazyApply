class HobbyRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def insert_hobby(self, hobby_model):
        sql = "INSERT INTO HOBBIES (user_id, name) VALUES (?, ?)"
        data = [hobby_model.user_id, hobby_model.name]

        self.db_manager.cursor.execute(sql, data)

        self.db_manager.conn.commit()

        return hobby_model

    def select_hobby(self):
        sql = "SELECT * FROM HOBBIES"
        rows = self.db_manager.cursor.execute(sql).fetchall()
        for row in rows:
            print(row)
