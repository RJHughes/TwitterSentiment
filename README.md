# Twitter Sentiment analysis

[![Build Status](https://travis-ci.com/RJHughes/TwitterSentiment.svg?branch=master)](https://travis-ci.com/RJHughes/TwitterSentiment)

To run the app, you'll need to get the dependencies from the requirements.txt file

I'd suggest making a new virtualenv and running 

`pip install -r requirements.txt`

If you then navigate to the TwitterSentiment folder you need to set the FLASK_APP environment variable. Run the below command
`export FLASK_APP=app/application.py`

You can then run

`flask run`

To run the site locally on localhost:5000


You can run the tests from the top level with

` python -m unittest discover tests "TEST*"`
