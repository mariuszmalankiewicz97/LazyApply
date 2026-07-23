class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def insert_user(self, user_model):
        sql = "INSERT INTO users (name, lastname, city, phone, e_mail, summary, github, linkedin) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        data = (
            user_model.name,
            user_model.lastname,
            user_model.city,
            user_model.phone,
            user_model.e_mail,
            user_model.summary,
            user_model.github,
            user_model.linkedin,
        )

        self.db_manager.cursor.execute(sql, data)
        self.db_manager.conn.commit()

        user_model.id = self.db_manager.cursor.lastrowid
        return user_model

    def select_user(self):
        sql = "SELECT name, lastname, city, phone, e_mail, summary, github, linkedin from users"
        rows = self.db_manager.cursor.execute(sql).fetchall()
        for row in rows:
            return row
