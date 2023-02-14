from flask import Flask, request, render_template, url_for
from main import get_csv
import pandas as pd
import numpy as np
from liveserver import LiveServer
from locations import locations
from PIL import Image
import base64
import io

empty = np.array([])
async_mode = None
app = Flask(__name__)
ls = LiveServer(app)

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html', markers=empty, image=False)
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
            im = Image.open('fitness_plot.png')
            data = io.BytesIO()
            im.save(data, "PNG")
            encoded_img_data = base64.b64encode(data.getvalue())
            return render_template('index.html', markers=markers, lat=lat, lon=lon, image=True, img_data=encoded_img_data.decode('utf-8'))
        else:
            return "Please select a valid region in the drop down list and values in the allowed range."

@app.route('/about')
def about():
    return "WIP"

@app.route('/update')
def update():
    f = open('logs.txt','r')
    return f.readlines()

#if __name__ == '__main__':
ls.run('0.0.0.0', '8080')