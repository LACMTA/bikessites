import os,re,csv,datetime, time
# import pymongo
import simplejson as json
from bson import json_util,objectid
from flask import Flask,request,render_template,jsonify
from flask.ext import restful
from flask.ext.restful import reqparse, Resource, Api
from flask.ext.cors import cross_origin

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

def get_sites():
    csv_file = open(app.config['DATAFILE'], 'r')
    rows = csv.DictReader(csv_file)
    sites = []
    for row in rows:
        sites.append(row)
    return sites

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
        d = datetime.datetime.now()
        uid = int(time.mktime(d.timetuple())) * 1000
        # add an entry to a csv file
        with open(app.config['DATAFILE'], 'a') as fp:
            a = csv.writer(fp, delimiter=',')
            data = [
                uid,
                lat,
                lon,
                comment,
                ]
            a.writerow(data)
                    
        return {
            "uid": uid,
            "lat": lat,
            "lon": lon,
            "comment": comment,
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
    #
    # # @cross_origin() # allow all origins all methods.
    # def post(self):
    #     d = datetime.datetime.now()
    #     uid = int(time.mktime(d.timetuple())) * 1000
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('lat', type=float, help='latitude')
    #     parser.add_argument('lon', type=float, help='longitude')
    #     parser.add_argument('comment', type=str, help='comment')
    #     args = parser.parse_args()
    #
    #     # add an entry to a csv file
    #     with open(app.config['DATAFILE'], 'a') as fp:
    #         a = csv.writer(fp, delimiter=',')
    #         data = [
    #             uid,
    #             args['lat'],
    #             args['lon'],
    #             args['comment'],
    #             ]
    #         a.writerow(data)
    #
    #     return {
    #         "uid": uid,
    #         "lat": args['lat'],
    #         "lon": args['lon'],
    #         "comment": args['comment'],
    #         }

api.add_resource(BikeSite,
    '/bikesite',
    '/bikesite/',
    # '/bikesite/<float:lat>/<float:lon>/<string:comment>',
    )



if __name__ == "__main__":
    app.run()

