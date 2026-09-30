import unittest
import tempfile
import os

from app.database import Database
from app.student_service import StudentService


class TestStudentService(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        path = os.path.join(self.temp.name, "test.db")
        self.service = StudentService(Database(path))

    def tearDown(self):
        self.temp.cleanup()

    def test_add_student(self):
        result = self.service.add_student(
            1, "Charitha", 21, "Computer Science"
        )
        self.assertTrue(result)

    def test_get_student(self):
        self.service.add_student(2, "Ravi", 22, "IT")
        student = self.service.get_student(2)
        self.assertEqual(student[1], "Ravi")

    def test_get_all_students(self):
        self.service.add_student(1, "Ravi", 22, "IT")
        self.service.add_student(2, "Sita", 20, "CSE")
        self.assertEqual(len(self.service.get_all_students()), 2)

    def test_update_student(self):
        self.service.add_student(3, "Ram", 23, "IT")
        result = self.service.update_student(
            3, "Ramesh", 24, "CSE"
        )
        self.assertTrue(result)
        self.assertEqual(self.service.get_student(3)[1], "Ramesh")

    def test_delete_student(self):
        self.service.add_student(4, "Anu", 21, "ECE")
        self.assertTrue(self.service.delete_student(4))
        self.assertIsNone(self.service.get_student(4))

    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            self.service.add_student(5, "Ravi", 12, "IT")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            self.service.add_student(6, "", 21, "IT")

    def test_duplicate_id(self):
        self.service.add_student(7, "Ram", 22, "IT")
        with self.assertRaises(Exception):
            self.service.add_student(7, "Sita", 21, "CSE")


if __name__ == "__main__":
    unittest.main()
