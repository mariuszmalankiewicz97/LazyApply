class SkillRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def insert_skill(self, skill_model):
        sql = "INSERT INTO SKILLS (user_id, name) VALUES (?, ?)"
        data = [skill_model.user_id, skill_model.name]

        self.db_manager.cursor.execute(sql, data)
        self.db_manager.conn.commit()

        return skill_model

    def select_skill(self):
        sql = "SELECT * FROM SKILLS"
        rows = self.db_manager.cursor.execute(sql).fetchall()
        for row in rows:
            print(row)
