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
    reply = TextField(default='')
    pub_date = DateTimeField(default=datetime.datetime.now)
    approved = BooleanField(default=True)
    likes = IntegerField(default=0)

    def __unicode__(self):
        return '[%f,%f,%s]' % (self.lat, self.lon, self.comment)

    # def __repr__(self):
    #     return '[%f,%f,%s]' % (self.lat, self.lon, self.comment)

admin.register(Comment) # register "Comment" with vanilla ModelAdmin

# after all models and panels are registered, configure the urls
admin.setup()

# Exclude the uid from the resource listing
class CommentResource(RestResource):
    paginate_by=200
#     exclude = ('uid')

# register our models so they are exposed via /api/<model>/
# api.register(Comment, auth=api_auth, allowed_methods=['GET', 'POST', 'PUT'])
api.register(Comment, CommentResource, auth=api_auth, allowed_methods=['GET', 'POST', 'PUT'])


# configure the urls
api.setup()