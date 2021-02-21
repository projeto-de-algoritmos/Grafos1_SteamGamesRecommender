from flask import Flask
from flask_cors import CORS
import json
import src.graph as graph

app = Flask(__name__)
CORS(app)

@app.route('/search/<name>')
def search_name(name):
    return json.dumps(graph.search_names(name))

@app.route('/graph/<appid>')
def get_graph(appid):
    return graph.bfs_filter(appid)
