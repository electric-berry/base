from flask import Flask, render_template
from main import get_csv
import pandas as pd

#get_csv("Hampshire")
df = pd.read_csv('optimal.csv')


app = Flask(__name__)
markers = df.to_dict()
print(markers)

@app.route('/')
def index():
    return render_template('index.html', markers=markers)

if __name__ == '__main__':
    app.run()