from peewee import *
from playhouse.sqlite_ext import *

pragmas = [
    ('journal_mode', 'wal'),
    ('cache_size', -1024 * 32)]

def create_db(path_to_db):

    db= SqliteExtDatabase(path_to_db,pragmas=pragmas)
    print('SQL database built at ' + path_to_db)
    
    class FTSEntry(FTSModel):
        sentiment = IntegerField()
        username = CharField()
        date = DateTimeField()
        content = SearchField()

        class Meta:
            database = db

    return FTSEntry
