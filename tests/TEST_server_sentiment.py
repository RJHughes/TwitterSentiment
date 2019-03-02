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
       self.pos_sentiment_list = sentiment.get_sentiment(self.query)[1]
       self.neg_sentiment_list = sentiment.get_sentiment(self.query)[2]
       self.total_search = sentiment.get_sentiment(self.query)[3]
       self.hash_list = sentiment.get_sentiment(self.query)[4]
       self.months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    def test_date_returns(self):
        for date in self.date_list:
            month, day, year = date.split()
            self.assertTrue(month in self.months,month+ ' is an invalid month')
            self.assertTrue(int(day) in range(1,32), str(day)+' is not a valid day')
            self.assertTrue(int(year) in range(2000,datetime.datetime.now().year),year +' is not a valid year')

    def test_sentiment_positive_returns(self):
        for sentiment in self.pos_sentiment_list:
            self.assertIs(type(sentiment),float,'Sentiment must be a float')
            self.assertGreaterEqual(sentiment,0,'Sentiment must be greater or equal to 0')
            self.assertLessEqual(sentiment,1,'Sentiment must be less than or equal to 1')

    def test_sentiment_negative_returns(self):
        for sentiment in self.neg_sentiment_list:
            self.assertIs(type(sentiment),float,'Sentiment must be a float')
            self.assertGreaterEqual(sentiment,-1,'Sentiment must be greater or equal to -1')
            self.assertLessEqual(sentiment,0,'Sentiment must be less than or equal to 0')

    def test_count_dict(self):
        for counts in self.total_search:
            self.assertIs(type(counts),int)
            self.assertGreaterEqual(counts,0)

    def test_hash_list(self):
        for hashtags in self.hash_list:
            self.assertIs(type(hashtags),list)
            self.assertIs(type(hashtags[0]),str)
            self.assertIs(type(hashtags[1]),int)
