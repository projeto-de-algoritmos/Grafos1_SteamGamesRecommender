from flask import Flask
import json
import src.graph as graph

app = Flask(__name__)

@app.route('/search/<name>')
def search_name(name):
    return graph.search_names(name)

@app.route('/graph/<appid>')
def get_graph(appid):
    return graph.bfs_filter(appid)
