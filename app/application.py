from flask import Flask
from flask import render_template, request, flash
from app.forms import Search
from app.db_builder import create_large_db
from app.sentiment import get_sentiment
import pandas as pd
import json
import datetime
import time
import numpy as np
import os


application = Flask(__name__)
application.config['SECRET_KEY'] = 'agile'


@application.route('/', methods=['GET', 'POST'])
def search():
    date_list = []
    sentiment_list = []
    search=''
    form = Search()
    if request.method == 'POST':
        search=request.form['search']

        # Error handling for invalid search case
        if search == '':
            search = ' '
        if '-' in search[0]:
            print('uh oh')
            return render_template('search.html')


        db= create_large_db('app/database/test.db')


        # This block performs a query on the text field of the db and looks
        # for matches
        start = time.time()
        query = (db
                 .select()
                 .where(db.text.match(search)))
        end = time.time()
        print(end - start)

        date_list, sentiment_list, count_dict, hash_list = get_sentiment(query)
        #hash_list = [['foo',120], ['bar',60]]
        print(hash_list)
    return render_template('index.html', form=form, labels=date_list, values=sentiment_list, title=search, hash_list=json.dumps(hash_list))
