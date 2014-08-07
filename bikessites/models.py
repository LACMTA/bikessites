import datetime, time

from flask_peewee.auth import BaseUser
from flask_peewee.rest import RestResource, UserAuthentication
from peewee import FloatField,DateTimeField,TextField,BooleanField,IntegerField

from bikessites import db, admin, api, api_auth

class Comment(db.Model):
    d = datetime.datetime.now()
    stamp = int( (int(time.mktime(d.timetuple())) *1000) +(d.microsecond/100))
    uid = IntegerField(default=stamp)
    lat = FloatField(default=0.0)
    lon = FloatField(default=0.0)
    comment = TextField(default='Hi')
    pub_date = DateTimeField(default=datetime.datetime.now)
    approved = BooleanField(default=True)
    likes = IntegerField(default=0)

    def __unicode__(self):
        return '(%s,%s) %s' % (self.lat, self.lon, self.comment)

admin.register(Comment) # register "Comment" with vanilla ModelAdmin

# after all models and panels are registered, configure the urls
admin.setup()

# register our models so they are exposed via /api/<model>/
api.register(Comment, auth=api_auth, allowed_methods=['GET', 'POST'])

# configure the urls
api.setup()