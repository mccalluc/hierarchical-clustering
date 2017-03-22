from flask import Flask, request, send_from_directory
from cluster import Cluster
from os import environ
import json

app = Flask(__name__, static_url_path=environ['STATIC_DIR'])

@app.route('/cluster')
def cluster():
    matrix_json = request.args.get('matrix')
    matrix = json.loads(matrix_json)
    cluster_order = Cluster(matrix).cluster()
    return json.dumps(cluster_order)

@app.route('/')
def homepage():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(path)
