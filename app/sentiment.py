import ast

def get_sentiment(query):
    """ Given a query, this function returns the sentiment for the items in
    that query and returns the dates and sentiment for each date """

    print('Num entries:' + str(len(query)))

    # Now we're going to extract the sentiment and date information and get the average sentiment on a particular date
    sentiment_array = []
    pos_sent_dict = {}
    neg_sent_dict = {}
    pos_count_dict = {}
    neg_count_dict = {}
    hash_dict = {}
    hash_list = []
    fav_max = 0

    for entry in query:
        sentiment_array.append(entry.sentiment)

        hashtags = ast.literal_eval(entry.hashtags)
        if len(hashtags)!=0:
            for tags in hashtags:
                tags = dict(tags)
                if tags['text'] in hash_dict:
                    hash_dict[tags['text']] =  hash_dict[tags['text']] + 100
                else:
                    hash_dict[tags['text']] = 100

        # We need to remove the timezone, day and hour data
        temp_date = entry.created_at.split()

        temp_date.pop(0)
        temp_date.pop(2)
        temp_date.pop(2)

        # This makes it a datetime object for easier working
        # formatted_date = datetime.datetime.strptime(' '.join(temp_date), '%b %d %Y')
        formatted_date = ' '.join(temp_date)
        # We now take the average of the sentiment by keeping a running average

        # Positive sentiment
        if entry.sentiment > 0:
            if formatted_date in pos_sent_dict:
                pos_count_dict[formatted_date] = pos_count_dict[formatted_date] + 1
                pos_sent_dict[formatted_date] = (pos_sent_dict[formatted_date] +
                                             (entry.sentiment - pos_sent_dict[formatted_date]) /
                                             pos_count_dict[formatted_date])
            else:
                pos_count_dict[formatted_date] = 1
                pos_sent_dict[formatted_date] = 1
        else:
            if formatted_date in neg_sent_dict:
                neg_count_dict[formatted_date] = neg_count_dict[formatted_date] + 1
                neg_sent_dict[formatted_date] = (neg_sent_dict[formatted_date] +
                                             (entry.sentiment - neg_sent_dict[formatted_date]) /
                                             neg_count_dict[formatted_date])
            else:
                neg_count_dict[formatted_date] = 1
                neg_sent_dict[formatted_date] = 0

    date_list = []
    pos_sentiment_list = []
    neg_sentiment_list = []

    for key in sorted(pos_sent_dict):
        date_list.append(key), \
        pos_sentiment_list.append(pos_sent_dict[key]), \

    for key in sorted(neg_sent_dict):
        if key not in date_list: date_list.append(key)
        neg_sentiment_list.append(neg_sent_dict[key]), \

    for items in hash_dict:
        hash_list.append([items,hash_dict[items]])

    return date_list, pos_sentiment_list, neg_sentiment_list, pos_count_dict, hash_list
