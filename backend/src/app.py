from flask import Flask
import json

app = Flask(__name__)

@app.route('/search/<name>')
def search_name(name):

    try:
        search = name
        db = open ('src/allgames.txt')

        for line in db:
            if search in line:
                return json.loads(line)
    
    except IOError as error: 
        return f"Message: {error}"

@app.route('/graph/<appid>')
def get_graph(appid):
    return appid

