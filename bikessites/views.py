import os,re,csv,datetime, time
import simplejson as json

from flask import Flask,request,render_template,jsonify, redirect, url_for
# from flask.ext.cors import cross_origin

from bikessites import app, api, auth, admin
from bikessites.models import Comment

def get_sites():
    sites = Comment.select().where(Comment.approved == True)
    bikeStations = app.config['BIKESTATIONS']
    return sites, jsonify(bikeStations)

@app.route("/")
def index():
    sites,bikeStations = get_sites()
    return render_template('index.html', sites=sites, bikeStations=bikeStations)

@app.route("/sitesurvey")
def sitesurvey():
    return redirect(url_for('index'))

