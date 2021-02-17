from flask import Flask

app = Flask(__name__)

@app.route('/search/<name>')
def search_name(name):
    return f'{name}'

@app.route('/graph/<appid>')
def get_graph(appid):
    return appid