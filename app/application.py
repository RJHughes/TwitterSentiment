from flask import Flask
from flask import render_template, request, flash
from app.forms import Search
from app.db_builder import create_large_db
from app.sentiment import get_sentiment
from app.wordcloud_gen import create_wordcloud
import pandas as pd
import json
import datetime
import time
import numpy as np
import os


application = Flask(__name__)
application.config['SECRET_KEY'] = 'agile'

def handle_search_errors(search):
    """ Error handling for invalid search cases. Returns a default page on error """

    if search == '':
        search = ' '
    if '-' in search[0]:
        print('Invalid search params entered')
        return render_template('search.html')

def get_query(search, db):
    """ Returns query object based on matches in database content """

    start = time.time()
    query = (db
             .select()
             .where(db.text.match(search)))
    end = time.time()
    print(end - start)
    return query

if __name__ == '__main__':
    @application.route('/', methods=['GET', 'POST'])
    def search():

        # Initialise variables
        date_list = []
        sentiment_list = []
        hash_list = []
        img_handle=[]
        search=''
        form = Search()

        if request.method == 'POST':
            search=request.form['search']
            handle_search_errors(search)
            db= create_large_db('app/database/test.db')
            query = get_query(search, db)
            date_list, sentiment_list, count_dict, hash_list = get_sentiment(query)
            img_handle = create_wordcloud(hash_list)

        return render_template('index.html',
                                form=form,
                                labels=date_list,
                                values=sentiment_list,
                                title=search,
                                hash_list=json.dumps(hash_list),
                                handle=img_handle)
