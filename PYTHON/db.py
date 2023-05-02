from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('database.csv')

@app.route('/database')
def index():
    return jsonify(df.to_dict('records'))

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=3000)
