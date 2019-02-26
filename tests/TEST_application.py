import unittest
import app.application as app
import time
import timeout_decorator

database_path='../app/database/test.db'

class AppTestCase(unittest.TestCase):
    def setUp(self):
       self.db = app.create_large_db(database_path)

    @timeout_decorator.timeout(2)
    def test_db_search(self):
        app.get_query('Hello',self.db)
