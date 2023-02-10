from flask import Flask, render_template
from main import get_csv
import pandas as pd
import numpy as np
from liveserver import LiveServer

#get_csv("Hampshire")
# add dials for changing parameters
# matplotlib graphs per generation
df = pd.read_csv('optimal.csv')
lats = df.iloc[:,0]
lons = df.iloc[:,1]
lat = np.median(lats)
lon = np.median(lons)
app = Flask(__name__)
markers = df.to_numpy()
ls = LiveServer(app)

@app.route('/')
def index():
    return render_template('index.html', markers=markers, lat=lat, lon=lon)

if __name__ == '__main__':
    app.run()