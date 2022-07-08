# app.py

from flask import Flask, request, render_template
import pandas as pd
from ghg_calculator import calculate_emissions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    activity_data = float(request.form['activity_data'])
    emission_factor = float(request.form['emission_factor'])
    emissions = calculate_emissions(activity_data, emission_factor)
    return render_template('result.html', emissions=emissions)

if __name__ == '__main__':
    app.run(debug=True)
