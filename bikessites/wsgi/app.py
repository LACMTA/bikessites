import os,re,csv,datetime, time
# from tempfile import NamedTemporaryFile
# import shutil
# import pymongo
import simplejson as json
# from bson import json_util,objectid
from flask import Flask,request,render_template,jsonify
from flask.ext import restful
from flask.ext.restful import reqparse, Resource, Api
from flask.ext.cors import cross_origin
from table_fu import TableFu
# from urlparse import urljoin
# from flask import request
# from werkzeug.contrib.atom import AtomFeed

app = Flask(__name__)
api = restful.Api(app)

#add this so that flask doesn't swallow error messages
app.config['PROPAGATE_EXCEPTIONS'] = True
# mongodb
# data collection
app.config['DATAFILE'] = 'data.csv'
app.config['DEBUG'] = True
# CORS
app.config['CORS_ORIGINS'] = ['http://localhost', 'http://127.0.0.1', 'http://metro.net']
app.config['CORS_HEADERS'] = ['Content-Type']

#
#
#
# def make_external(url):
#     return urljoin(request.url_root, url)
#
# @app.route('/atom')
# def recent_feed():
#     feed = AtomFeed('Recent Comments',feed_url=request.url, url=request.url_root)
#
#     table = TableFu.from_file(app.config['DATAFILE'])
#     t2 = table.filter(approved='1')
#
#     articles = t2
#
#     for article in articles:
#         d=
#         d.strftime("%a, %d %b %Y %H:%M:%S %z")
#         feed.add(article.title, unicode(article.rendered_text),
#             content_type='html',
#             author=article.author.name,
#             url=make_external(article.url),
#             updated=article.last_update,
#             published=article.published)
#     return feed.get_response()

# def edit_csv(uid='1406159698000'):
#     filename = app.config['DATAFILE']
#     tempfile = NamedTemporaryFile(delete=False)
#
#     with open(filename, 'rb') as csvFile, tempfile:
#         reader = csv.reader(csvFile, delimiter=',', quotechar='"')
#         writer = csv.writer(tempfile, delimiter=',', quotechar='"')
#
#         for row in reader:
#             row[1] = row[1].title()
#             writer.writerow(row)
#
#     shutil.move(tempfile.name, filename)


def get_sites():
    table = TableFu.from_file(app.config['DATAFILE'])
    t2 = table.filter(approved='1')
    return t2

def get_site(uid='1406159698000'):
    sites = get_sites()
    for site in sites:
        print "does %s == %s ? %s" %( int(site['uid']) , int(uid), (int(site['uid'])==int(uid)) )
        if (int(site['uid'])==int(uid)):
            return site
        else:
            return {'message':'oops'}

class AddSite(Resource):
    """POST is problematic. Let's try a GET"""
    def get(self,lat=11.111,lon=-111.111,comment='No Comment'):
        if (lon > 0):
            # make it negative
            lon = (lon * -1)
        d = datetime.datetime.now()
        uid = int( (int(time.mktime(d.timetuple())) *1000) +(d.microsecond/100))
        # add an entry to a csv file
        with open(app.config['DATAFILE'], 'a') as fp:
            a = csv.writer(fp, delimiter=',')
            data = [
                uid,
                lat,
                lon,
                comment,
                '1',
                0,
                ]
            a.writerow(data)
                    
        return {
            "uid": uid,
            "lat": lat,
            "lon": lon,
            "comment": comment,
            "approved": comment,
            "likes": comment,
            }
api.add_resource(AddSite, 
    '/siteadd/<float:lat>/-<float:lon>/',
    '/siteadd/<float:lat>/-<float:lon>/<string:comment>',
    '/siteadd/<float:lat>/-<float:lon>/<string:comment>/',
    )

@app.route("/sitesurvey")
def sitesurvey():
    sites = get_sites()
    return render_template('index.html', sites=sites)

class BikeSite(Resource):
    def get(self):
        sites = get_sites()
        if (app.config['DEBUG']): print sites
        return sites

api.add_resource(BikeSite,
    '/bikesite',
    '/bikesite/',
    # '/bikesite/<float:lat>/<float:lon>/<string:comment>',
    )

# class LikeBikeSite(Resource):
#     def get(self,uid='1406247848123'):
#         table = TableFu.from_file(app.config['DATAFILE'])
#         t2 = table.filter( uid=str(uid) )
#         row = t2[0]
#         print "I LIKE YOU %s" %(row)
#         return t2.json()
#
# api.add_resource(LikeBikeSite,
#     '/bikesite/like/<uid:int>',
#     '/bikesite/like/<uid:int>/',
#     )



if __name__ == "__main__":
    app.run()

