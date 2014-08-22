import datetime, time

from flask import Markup
from flask_peewee.auth import BaseUser
from flask_peewee.rest import RestResource, UserAuthentication
from peewee import FloatField,DateTimeField,TextField,BooleanField,IntegerField,CharField
import random
from redis import Redis
# from rq import Queue
from flask.ext.rq import get_queue

from bikessites import db, admin, api, api_auth
from gdocs import _save_gdocs

# Tell RQ what Redis connection to use
redis_conn = Redis('localhost', 6379)
q = Queue(connection=redis_conn)  # no args implies the default queue

class Comment(db.Model):
    d = datetime.datetime.now()
    uid = IntegerField(default=0)
    lat = FloatField(default=0.0)
    lon = FloatField(default=0.0)
    comment = TextField(default='Hi')
    name = CharField(default='anonymous',max_length=50)
    email = CharField(default='anonymous@gmail.com',max_length=255)
    zipcode = CharField(default='90000',max_length=10)
    reply = TextField(default='')
    pub_date = DateTimeField(default=datetime.datetime.now)
    approved = BooleanField(default=True)
    likes = IntegerField(default=0)
    category=CharField(default='userSelected',max_length=16)
    
    def __unicode__(self):
        return '[%f,%f,%s]' % (self.lat, self.lon, self.comment)
    
    def save(self, *args, **kwargs):
        stamp = int( random.randrange(111111111111,999999999999) )
        self.uid = stamp
        job = get_queue().enqueue( _save_gdocs, self )
        return super(Comment, self).save(*args, **kwargs)

    # def __repr__(self):
    #     return '[%f,%f,%s]' % (self.lat, self.lon, self.comment)

admin.register(Comment) # register "Comment" with vanilla ModelAdmin

# after all models and panels are registered, configure the urls
admin.setup()

# Exclude the uid from the resource listing
class CommentResource(RestResource):
    paginate_by=500
#     exclude = ('uid')

# register our models so they are exposed via /api/<model>/
# api.register(Comment, auth=api_auth, allowed_methods=['GET', 'POST', 'PUT'])
api.register(Comment, CommentResource, auth=api_auth, allowed_methods=['GET', 'POST', 'PUT'])


# configure the urls
api.setup()
