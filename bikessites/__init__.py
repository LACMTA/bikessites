from flask import Flask
# flask-rq
from flask.ext.rq import RQ
# flask-bootstrap
# from flask_bootstrap import Bootstrap
# flask-peewee
from flask_peewee.auth import Auth
from flask_peewee.rest import RestAPI, UserAuthentication
from flask_peewee.db import Database
from flask_peewee.admin import Admin

app = Flask(__name__)
# Bootstrap(app)
RQ(app)
app.config.from_object('config.Configuration')
db = Database(app)

# needed for authentication
auth = Auth(app, db)
api_auth = UserAuthentication(auth, protected_methods=['PUT', 'DELETE'])

api = RestAPI(app, default_auth=api_auth)
admin = Admin(app, auth)

from bikessites import models, views 



