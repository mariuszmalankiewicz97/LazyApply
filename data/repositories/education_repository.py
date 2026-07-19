class EducationRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def insert_education(self, education_model):
        sql = "INSERT INTO education (user_id, name, time, description) VALUES (?, ?, ?, ?)"
        data = [
            education_model.user_id,
            education_model.name,
            education_model.time,
            education_model.description,
        ]

        self.db_manager.cursor.execute(sql, data)

        self.db_manager.conn.commit()

        return education_model

    def select_education(self):
        sql = "SELECT * FROM education"

        rows = self.db_manager.cursor.execute(sql).fetchall()

        for row in rows:
            print(row)
