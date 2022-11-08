
from flask_restful import Resource, Api
from flask import Flask, render_template, request, redirect, url_for, Response
import logging
import fetchdata as datafetcher
import db as db


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


app = Flask(__name__, template_folder='template')
api = Api(app)


# /Country/**
@app.route("/country/all", methods=["GET"])
def findAllCountry ():
    result = db.findAllCountry()
    return { 'data' : result }

@app.route("/country/id/<int:countryId>", methods=["GET"])
def findCountryById (countryId):
    result = db.findCountryById(countryId)
    return { 'data' : result }

@app.route("/country/add/<string:countryName>", methods=["PUT"])
def addCountry (countryName):
    result = db.addCountry(countryName)
    return "Ok"

    
@app.route("/country/delete/<int:countryId>", methods=["DELETE"])
def deleteCountryById (countryId):
    result = db.deleteCountryById(countryId)
    if result:
        return "OK"
    else:
        return Response("Error", 404)


# /data/**
@app.route("/data/all", methods=["GET"])
def findAllData ():
    result = db.findAllData() 
    return {'data': result}

@app.route("/data/country/<string:countryName>", methods=["GET"])
def findDataByCountry (countryName):
    result = db.findDataByCountry(countryName)
    if(result != None):
        return { 'data' : result }
    else:
        return Response("Error", 404)

@app.route("/data/id/<int:dataId>", methods=["GET"])
def findDataById (dataId):
    result = db.findDataById(dataId) 
    return { 'data' : result }

@app.route("/data/change/<int:dataId>", methods=["POST"])
def changeData (dataId):
    result = db.changeData(dataId)
    if result:
        return "OK"
    else:
        return Response("Error", 404)
    
@app.route("/data/delete/<int:dataId>", methods=["DELETE"])
def deleteDataById (dataId):
    result = db.deleteDataById(dataId)
    if result:
        return "OK"
    else:
        return Response("Error", 404)

if __name__ == '__main__':
    db.initDB()
    datafetcher.fetchData()
    app.run(debug=True, use_reloader=False)
    