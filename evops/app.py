from flask import Flask, request, render_template
from main import get_csv
import pandas as pd
import numpy as np
from liveserver import LiveServer
from locations import locations

empty = np.array([])
app = Flask(__name__)  
ls = LiveServer(app)

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html', markers=empty)
    elif request.method == "POST":
        region = request.form.get("region")
        pop = request.form.get("pop")
        gen = request.form.get("gen")
        bud = request.form.get("bud")
        if region in locations:
            get_csv(region, int(pop), int(gen), int(bud))
            df = pd.read_csv('optimal.csv')
            lats = df.iloc[:,0]
            lons = df.iloc[:,1]
            lat = np.median(lats)
            lon = np.median(lons)
            markers = df.to_numpy()
            return render_template('index.html', markers=markers, lat=lat,lon=lon)
        else:
            return "Please select a valid region in the drop down list."

#if __name__ == '__main__':
ls.run('0.0.0.0', '8080')