from flask import Flask, request
from cluster import Cluster
import json

app = Flask(__name__)

@app.route('/cluster')
def cluster():
    matrix_json = request.args.get('matrix')
    matrix = json.loads(matrix_json)
    cluster_order = Cluster(matrix).cluster()
    return json.dumps(cluster_order)
