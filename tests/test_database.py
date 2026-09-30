import unittest
import tempfile
import os
from app.database import Database


class TestDatabase(unittest.TestCase):

    def test_database_initialization(self):
        with tempfile.TemporaryDirectory() as temp:
            path = os.path.join(temp, "test.db")
            db = Database(path)

            with db.connect() as conn:
                result = conn.execute("""
                    SELECT name FROM sqlite_master
                    WHERE type='table' AND name='students'
                """).fetchone()

            self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
