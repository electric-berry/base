from flask import Flask, render_template
from main import get_csv
import pandas as pd
import numpy as np

#get_csv("Hampshire")
# add dials for changing parameters
# matplotlib graphs per generation
df = pd.read_csv('optimal.csv')

app = Flask(__name__)
markers = df.to_numpy()

@app.route('/')
def index():
    return render_template('index.html', markers=markers)

if __name__ == '__main__':
    app.run()