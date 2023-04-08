from flask import Flask, request, render_template, url_for
from flask_socketio import SocketIO
from threading import Lock
from main import get_csv
import pandas as pd
import numpy as np
from liveserver import LiveServer
from locations import locations
from PIL import Image
import base64
import io
import time

thread = None
thread_lock = Lock()

f = open("optimal.csv", "w+")

empty = np.array([])
app = Flask(__name__)
app.config['SECRET_KEY'] = 'evops'
socketio = SocketIO(app, cors_allowed_origins='*')
#ls = LiveServer(app)

region, pop, gen, bud, complete = None,None,None,None,None

from access_data import get_possible_spots
from input_data import get_data
from genetic_algorithm_test import genetic_algorithm
import csv
import os

#TODO:
# Somehow notify the frontend that a generation has passed

def get_csv(location,pop_size,generations,budget):
    print("Getting Data...")
    try:
        get_data(location)
    except:
        print("Error when collecting data.")
        print("Processing existing CSV file...")
    print("Done!")
    print("Processing Data...")
    possible,latitudes,longitudes,traffics = get_possible_spots()
    print(traffics)
    print("Done!")
    ga = genetic_algorithm()
    print("Running Genetic Algorithm...")
    for i in range(generations):
        agent = ga.execute(latitudes,longitudes,traffics,pop_size,generations,possible,budget)
        socketio.emit('updateSensorData', {'value': ga.fitness_values[-1], "date": i})
    print("Done!")
    # ! lats, longs, pop_size, generations, possible_coordinates, budget
    # print(agent.fitness,agent.config)
    optimal = agent.config
    os.system("cls")
    print("Top Fitness:",str(agent.fitness))
    print("Writing to CSV...")
    with open('optimal.csv', 'w') as fh:
        spamwriter = csv.writer(fh)
        for t in agent.config:
            spamwriter.writerow(t)
    print("Done!")
    
def background_thread():
    global region, pop, gen, bud
    while True:
        if region:
            get_csv(region, int(pop), int(gen), int(bud))
            region = False
            complete = True
    #get_csv(region, int(pop), int(gen), int(bud))

@app.route('/', methods =["GET", "POST"])
def index():
    global region,pop,gen,bud
    if request.method == "GET":
        return render_template('index_test.html', markers=empty, image=False)
    elif request.method == "POST":
        region = request.form.get("region")
        pop = request.form.get("pop")
        gen = request.form.get("gen")
        bud = request.form.get("bud")
        if region in locations:
            while not(complete):
                pass
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
            return render_template('index_test.html', markers=markers, lat=lat, lon=lon, image=True, img_data=encoded_img_data.decode('utf-8'))
        else:
            return "Please select a valid region in the drop down list and values in the allowed range."

@app.route('/about')
def about():
    return "WIP"

@app.route('/update')
def update():
    f = open('logs.txt','r')
    return f.readlines()

@socketio.on('connect')
def connect():
    global thread
    print('Client connected')

    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)

"""
Decorator for disconnect
"""
@socketio.on('disconnect')
def disconnect():
    print('Client disconnected',  request.sid)

if __name__ == '__main__':
    socketio.run(app)