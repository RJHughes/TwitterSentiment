def get_sentiment(query):
    """ Given a query, this function returns the sentiment for the items in
    that query and returns the dates and sentiment for each date """

    print('Num entries:' + str(len(query)))

    # Now we're going to extract the sentiment and date information and get the average sentiment on a particular date
    sentiment_array = []
    date_dict = {}
    count_dict = {}
    fav_max = 0

    for entry in query:
        sentiment_array.append(entry.sentiment)
        # if entry.urls is not None:
        # print(entry.retweet_count)
        # We need to remove the timezone, day and hour data
        temp_date = entry.created_at.split()

        temp_date.pop(0)
        temp_date.pop(2)
        temp_date.pop(2)

        # This makes it a datetime object for easier working
        # formatted_date = datetime.datetime.strptime(' '.join(temp_date), '%b %d %Y')
        formatted_date = ' '.join(temp_date)
        # We now take the average of the sentiment by keeping a running average
        if formatted_date in date_dict:
            count_dict[formatted_date] = count_dict[formatted_date] + 1
            date_dict[formatted_date] = (date_dict[formatted_date] +
                                         (entry.sentiment - date_dict[formatted_date]) /
                                         count_dict[formatted_date])
        else:
            count_dict[formatted_date] = 0
            date_dict[formatted_date] = 0

    sorted_dates = sorted(count_dict)

    date_list = []
    sentiment_list = []

    for key in sorted(date_dict):
        date_list.append(key), sentiment_list.append(date_dict[key])

    return date_list, sentiment_list
