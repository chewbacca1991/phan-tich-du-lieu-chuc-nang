from flask import Flask, jsonify, request
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Logic để lấy dữ liệu
    data = {'message': 'Dữ liệu sẽ được lấy từ cơ sở dữ liệu'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)