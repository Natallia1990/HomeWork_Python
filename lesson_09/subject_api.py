from sqlalchemy import create_engine, text


class SubjectAPI:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
        self.connection_string = connection_string

    def connect(self):
        return self.db.connect()

    def select_subject_by_id(self, subject_id):
        connection = self.connect()
        try:
            sql_statement = text("SELECT * FROM subject WHERE subject_id = :subject_id")
            result = connection.execute(sql_statement, {"subject_id": subject_id})
            return result.mappings().all()
        finally:
            connection.close()

    def add_subject(self, subject_id, subject_title):
        connection = self.connect()
        try:
            self.cleanup_subject(subject_id)

            insert_sql = text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)")
            connection.execute(insert_sql, {"id": subject_id, "title": subject_title})
            connection.commit()

            select_sql = text("SELECT * FROM subject WHERE subject_id = :id")
            result = connection.execute(select_sql, {"id": subject_id})
            rows = result.mappings().all()

            return len(rows) == 1
        finally:
            connection.close()

    def update_subject(self, subject_id, new_title):
        connection = self.connect()
        try:
            update_sql = text("UPDATE subject SET subject_title = :new_title WHERE subject_id = :id")
            result = connection.execute(update_sql, {"new_title": new_title, "id": subject_id})
            connection.commit()
            return result.rowcount
        finally:
            connection.close()

    def delete_subject(self, subject_id):
        connection = self.connect()
        try:
            delete_sql = text("DELETE FROM subject WHERE subject_id = :id")
            result = connection.execute(delete_sql, {"id": subject_id})
            connection.commit()
            return result.rowcount
        finally:
            connection.close()

    def get_subject_count(self, subject_id):
        connection = self.connect()
        try:
            result = connection.execute(text("SELECT COUNT(*) FROM subject WHERE subject_id = :id"),
                                        {"id": subject_id})
            return result.scalar()
        finally:
            connection.close()

    def cleanup_subject(self, subject_id):
        connection = self.connect()
        try:
            connection.execute(text("DELETE FROM subject WHERE subject_id = :id"), {"id": subject_id})
            connection.commit()
        finally:
            connection.close()
