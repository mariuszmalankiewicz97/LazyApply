class ExperienceRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def insert_experience(self, expierience_model):
        sql = "INSERT INTO EXPERIENCES (user_id, name, position, time, description) VALUES (?, ?, ?, ?, ?)"
        data = [
            expierience_model.user_id,
            expierience_model.name,
            expierience_model.position,
            expierience_model.time,
            expierience_model.description,
        ]

        self.db_manager.cursor.execute(sql, data)
        self.db_manager.conn.commit()

        return expierience_model

    def select_experience(self):
        sql = "SELECT * FROM EXPERIENCES"

        rows = self.db_manager.cursor.execute(sql).fetchall()

        for row in rows:
            print(row)
