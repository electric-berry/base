from flask import Flask, render_template
from main import get_csv
import pandas as pd

get_csv("Hampshire")
df = pd.read_csv('optimal.csv')

app = Flask(__name__)

@app.route('/')
def index():
    return(df.to_string())

if __name__ == '__main__':
    app.run()