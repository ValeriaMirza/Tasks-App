import unittest
from database import (save_to_database, get_last_inserted_id,
                      create_database_and_table_if_not_exists)
from datetime import datetime
from config import user_email
import unittest.mock


class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_database_and_table_if_not_exists()

    def test_save_to_database(self):
        success = save_to_database(user_email, 'Test Task',
                                   datetime(2024, 12, 31, 23, 59))
        self.assertTrue(success)

    def test_get_last_inserted_id(self):
        save_to_database(user_email, 'Test Task',
                         datetime(2024, 12, 31, 23, 59))
        last_id = get_last_inserted_id()
        print(f"Last inserted ID: {last_id}")
        self.assertIsNotNone(last_id)


if __name__ == '__main__':
    unittest.main()
