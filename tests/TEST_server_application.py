import unittest
import app.application as app
import time
import timeout_decorator
import sys

database_path = 'app/database/test.db'

class SearchCaseTest(unittest.TestCase):
    def setUp(self):
       self.db = app.create_large_db(database_path)

    @timeout_decorator.timeout(2)
    def test_search_Hello(self):
        query = app.get_query('Hello',self.db)

    @timeout_decorator.timeout(2)
    def test_search_123(self):
        query = app.get_query('123',self.db)

    @timeout_decorator.timeout(2)
    def test_search_space(self):
        query = app.get_query('bdsfga FSFVA',self.db)

    @timeout_decorator.timeout(2)
    def test_search_dash(self):
        query = app.get_query('--ffsag',self.db)

    @timeout_decorator.timeout(2)
    def test_search_escape(self):
        query = app.get_query('/\fdewq',self.db)

    @timeout_decorator.timeout(2)
    def test_search_I(self):
        query = app.get_query('I',self.db)

    def test_search_and_confirm_structure(self):
        query = app.get_query('Twitter',self.db)
        if len(query) > 0:
            for content in query:
                self.assertTrue(hasattr(content, 'sentiment'),'Content has no sentiment attribute')
                self.assertTrue(hasattr(content, 'user_id'),'Content has no user_id attribute')
                self.assertTrue(hasattr(content, 'created_at'),'Content has no created_at attribute')
                self.assertTrue(hasattr(content, 'text'),'Content has no text attribute')
                self.assertTrue(hasattr(content, 'hashtags'),'Content has no hashtags attribute')
                self.assertTrue(hasattr(content, 'user_mentions'),'Content has no user_mentions attribute')
                self.assertFalse(hasattr(content, 'Scooby'),'Content a Scooby attribute??')
                break

if __name__ == '__main__':
    unittest.main()
