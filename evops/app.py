from flask import Flask, render_template
from main import get_csv
import pandas as pd
import numpy as np
from liveserver import LiveServer

#get_csv("Hampshire")
df = pd.read_csv('optimal.csv')
lats = df.iloc[:,0]
lons = df.iloc[:,1]
lat = np.median(lats)
lon = np.median(lons)
app = Flask(__name__)
markers = df.to_numpy()
ls = LiveServer(app)
empty = np.array([])

@app.route('/')
def index():
    return render_template('index.html', markers=empty)

#if __name__ == '__main__':
ls.run('0.0.0.0', '8080')