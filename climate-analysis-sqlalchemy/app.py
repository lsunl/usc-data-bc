#import dependencies
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#set up database
#create engine to connect
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#reflect databases and tables
Base = automap_base()
Base.prepare(engine, reflect=True)

#reference to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session
session = Session(engine)

#create an app
app = Flask(__name__)



#find the end date
latestdatequery = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
#print(f"End date: {latestdatequery}")

# Turn it to a date
thisyear = dt.date(2017, 8, 23)

# Grab last years starting point
oneyeardelta = thisyear - (dt.timedelta(days=365))
#print(f"Starting date: {oneyeardelta}")

# Query for last 12 months of data
oneyeardata = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > oneyeardelta).all()

#create app routes
@app.route("/")
def welcome():
    return (
        f"Available routes: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/start <br/>"
        f"/api/v1.0/start/end"
    )

@app.route("/api/v1.0/precipitation")
def about():
#Convert the query results to a Dictionary using date as the key and prcp as the value.
    precip = []
    for result in oneyeardata:
        precip_dict = {}
        precip_dict[result.date] = result.prcp
        precip.append(precip_dict)
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def station():
#Return a JSON list of stations from the dataset.
    allstations = session.query(Station.name).all()
    all_names = list(np.ravel(allstations))
    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
def tob():
#query for the dates and temperature observations from a year from the last data point.
#Return a JSON list of Temperature Observations (tobs) for the previous year.
    oneyeartob = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > oneyeardelta).all()
    oneyeartobs = []
    for result in oneyeartob:
        tob_dict = {}
        tob_dict[result.date] = result.tobs
        oneyeartobs.append(tob_dict)
    return jsonify(oneyeartobs)

@app.route("/api/v1.0/<start>")
def description(start):
#Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    start_date = dt.datetime.strptime(start, '%y-%m-%d')
    startonly = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    tempdata = []
    for data in startonly:
        thedata = {}
        thedata["TMIN"] = data[0]
        thedata["TAVG"] = data[1]
        thedata["TMAX"] = data[2]
    tempdata.append(thedata)
    return jsonify(tempdata)

@app.route("/api/v1.0/<start>/<end>")
def description2(start,end):
    start_date= dt.datetime.strptime(start, '%y-%m-%d')
    end_date= dt.datetime.strptime(end, '%y-%m-%d')
    desc = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    temp_data = []
    for data in desc:
        themdata = {}
        themdata["TMIN"] = data[0]
        themdata["TAVG"] = data[1]
        themdata["TMAX"] = data[2]
    temp_data.append(themdata)
    return jsonify(desc)

if __name__ == "__main__":
    app.run(debug=True)
