import sqlite3
from contextlib import contextmanager


class Database:

    def __init__(self, db_path="students.db"):
        self.db_path = db_path
        self.initialize()

    @contextmanager
    def connect(self):
        conn = sqlite3.connect(self.db_path)

        try:
            yield conn
            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    def initialize(self):
        with self.connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    course TEXT NOT NULL
                )
            """)