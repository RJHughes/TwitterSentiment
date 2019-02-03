from flask import Flask
from flask import render_template, request, flash
from forms import Search
from db_builder import create_db
import pandas as pd
import datetime
import time
import numpy as np


app = Flask(__name__)
app.config['SECRET_KEY'] = 'agile'

@app.route('/', methods=['GET', 'POST'])
def search():
    form = Search()
    if request.method == 'POST':
        search=request.form['search']
        print(search)

        db_kaggle = create_db('database/kaggle.db')

        # This block demonstrates how to query the database
        start = time.time()
        query = (db_kaggle
                 .select()
                 .where(db_kaggle.content.match(search)))
        end = time.time()
        print(end - start)

        print('Num entries:' + str(len(query)))

        # Now we're going to extract the sentiment and date information and get the average sentiment on a particular date
        sentiment_array = []
        date_dict = {}
        count_dict = {}


        for entry in query:
            sentiment_array.append(entry.sentiment)

            # We need to remove the timezone, day and hour data
            temp_date = entry.date.split()

            temp_date.pop(0)
            temp_date.pop(2)
            temp_date.pop(2)

            # This makes it a datetime object for easier working
            #formatted_date = datetime.datetime.strptime(' '.join(temp_date), '%b %d %Y')
            formatted_date = ' '.join(temp_date)
            # We now take the average of the sentiment by keeping a running average
            if formatted_date in date_dict:
                count_dict[formatted_date] = count_dict[formatted_date] + 1
                date_dict[formatted_date] = (date_dict[formatted_date] +
                                            (entry.sentiment-date_dict[formatted_date])/
                                             count_dict[formatted_date])
            else:
                count_dict[formatted_date] = 0
                date_dict[formatted_date] = 0

            date_list = []
            sentiment_list = []

        for key in sorted(date_dict):
            date_list.append(key), sentiment_list.append(date_dict[key])

        return render_template('hello.html', form=form, labels=date_list, values=sentiment_list)
