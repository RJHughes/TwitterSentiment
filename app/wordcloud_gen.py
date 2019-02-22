from os import path, getcwd
from PIL import Image
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import os, re

def create_wordcloud(data):

    if len(data) == 0:
        handle='_default'
        return handle
    d = {}
    for k,v in data:
        d[k] = v


    wordcloud = WordCloud(
        background_color='white',
        max_words=200,
        max_font_size=60,
        scale=3,
        random_state=1,
        relative_scaling=1,
        normalize_plurals=False
    ).generate_from_frequencies(d)


    for f in os.listdir("app/static/pictures/"):
        print(f)
        if re.search("wordcloud0", f):
            os.remove(os.path.join("app/static/pictures/", f))

    handle = str(np.random.rand(1)[0])

    wordcloud.to_file("app/static/pictures/wordcloud"+handle+".png")
    return handle
