import os,re,csv,datetime, time
import simplejson as json

from flask import Flask,request,render_template,jsonify, redirect, url_for
# from flask.ext.cors import cross_origin

from bikessites import app, api, auth, admin
from bikessites.models import Comment

def get_sites():
    sites = Comment.select().where(Comment.approved == True)
    bikeStations = [
    ['34.04179626','-118.2350671','5th / Hewitt'],
    ['34.04572787','-118.2364874','3rd / Traction'],
    ['34.04598345','-118.2325888','3rd / Santa Fe'],
    ['34.03576847','-118.2324278','Industrial / Mateo'],
    ['34.04929039','-118.2391334','1st / Central'],
    ['34.04726802','-118.2565731','7th / Grand'],
    ['34.05655609','-118.2531479','2nd / Figueroa'],
    ['34.05313943','-118.2477915','2nd / Hill'],
    ['34.06268572','-118.2462358','Cesar E Chavez / Figueroa'],
    ['34.05025044','-118.2469305','3rd / Spring'],
    ['34.04813253','-118.2472122','4th / Main'],
    ['34.05100159','-118.2445139','2nd / Main'],
    ['34.04737692','-118.2496235','5th / Spring'],
    ['34.04528338','-118.2499373','6th / Main'],
    ['34.0445344','-118.2522842','7th / Spring'],
    ['34.04593011','-118.2544273','7th / Hill'],
    ['34.04946373','-118.2563639','6th / Hope'],
    ['34.05084158','-118.2641959','7th / Bixel'],
    ['34.04164068','-118.2550228','9th / Main'],
    ['34.04514781','-118.2568628','8th / Olive'],
    ['34.04153844','-118.2619429','11th / Grand'],
    ['34.03940475','-118.2622004','12th / Olive'],
    ['34.04798696','-118.2612146','8th / Figueroa'],
    ['34.04631237','-118.2627368','9th / Figueroa'],
    ['34.04190294','-118.2668996','12th / Figueroa'],
    ['34.06157027','-118.2584681','1st / Toluca'],
    ['34.04325424','-118.2504201','7th / Los Angeles'],
    ['34.03722656','-118.2654566','14th / Grand'],
    ['34.03543061','-118.2714272','18th / Figueroa'],
    ['34.03014481','-118.2730097','23rd / Flower'],
    ['34.03917804','-118.232798','Willow / Mateo'],
    ['34.03453707','-118.2300889','7th / Santa Fe'],
    ['34.02711722','-118.2767165','27th / Figueroa'],
    ['34.02266233','-118.2838297','34th / Trousdale'],
    ['34.02035031','-118.2851601','36th / Trousdale']
    ]

    return sites, json.dumps(bikeStations)

@app.route("/")
def index():
    sites,bikeStations = get_sites()
    return render_template('index.html', sites=sites, bikeStations=bikeStations)

@app.route("/sitesurvey")
def sitesurvey():
    return redirect(url_for('index'))

