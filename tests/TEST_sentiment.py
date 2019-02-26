import unittest
import app.sentiment as sentiment
import app.application as app
import time
import timeout_decorator
import sys
import datetime

database_path = 'app/database/test.db'

class SentimentTest(unittest.TestCase):
    def setUp(self):
       self.db = app.create_large_db(database_path)
       self.query = app.get_query('Twitter',self.db)
       self.date_list = sentiment.get_sentiment(self.query)[0]
       self.sentiment_list = sentiment.get_sentiment(self.query)[1]
       self.count_dict = sentiment.get_sentiment(self.query)[2]
       self.hash_list = sentiment.get_sentiment(self.query)[3]
       self.months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    def test_date_returns(self):
        for date in self.date_list:
            month, day, year = date.split()
            self.assertTrue(month in self.months,month+ ' is an invalid month')
            self.assertTrue(int(day) in range(1,32), str(day)+' is not a valid day')
            self.assertTrue(int(year) in range(2000,datetime.datetime.now().year),year +' is not a valid year')

    def test_sentiment_returns(self):
        for sentiment in self.sentiment_list:
            self.assertGreaterEqual(sentiment,-1)
            self.assertLessEqual(sentiment,1)
