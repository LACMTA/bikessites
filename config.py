# config

class Configuration(object):
    DATABASE = {
        'name': 'data.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }
    SECRET_KEY = 'm3tr0'
    DATAFILE = 'data.csv'
    DEBUG = True
    #add this so that flask doesn't swallow error messages
    PROPAGATE_EXCEPTIONS = DEBUG
    # CORS
    CORS_ORIGINS = ['http://localhost', 'http://127.0.0.1', 'http://metro.net']
    CORS_HEADERS = ['Content-Type']
    
    
