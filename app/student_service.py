import sqlite3

class StudentService:
    def __init__(self, database):
        self.database = database

    def add_student(self, student_id, name, age, course):
        if not isinstance(student_id, int) or student_id <= 0:
            raise ValueError("Invalid student ID")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name is required")
        if not isinstance(age, int) or not 16 <= age <= 100:
            raise ValueError("Age must be between 16 and 100")
        if not isinstance(course, str) or not course.strip():
            raise ValueError("Course is required")

        with self.database.connect() as conn:
            try:
                conn.execute(
                    "INSERT INTO students (student_id, name, age, course) VALUES (?, ?, ?, ?)",
                    (student_id, name.strip(), age, course.strip())
                )
            except sqlite3.IntegrityError:
                raise Exception("Duplicate ID")
        return True

    def get_student(self, student_id):
        with self.database.connect() as conn:
            row = conn.execute(
                "SELECT * FROM students WHERE student_id = ?",
                (student_id,)
            ).fetchone()
            return row

    def get_all_students(self):
        with self.database.connect() as conn:
            rows = conn.execute(
                "SELECT * FROM students ORDER BY student_id"
            ).fetchall()
            return rows

    def update_student(self, student_id, name, age, course):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name is required")
        if not isinstance(age, int) or not 16 <= age <= 100:
            raise ValueError("Age must be between 16 and 100")
        if not isinstance(course, str) or not course.strip():
            raise ValueError("Course is required")

        with self.database.connect() as conn:
            cursor = conn.execute(
                "UPDATE students SET name = ?, age = ?, course = ? WHERE student_id = ?",
                (name.strip(), age, course.strip(), student_id)
            )
            return cursor.rowcount == 1

    def delete_student(self, student_id):
        with self.database.connect() as conn:
            cursor = conn.execute(
                "DELETE FROM students WHERE student_id = ?",
                (student_id,)
            )
            return cursor.rowcount == 1
