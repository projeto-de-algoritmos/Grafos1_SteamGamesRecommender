from flask import Flask
import json

app = Flask(__name__)

@app.route('/search/<name>')
def search_name(name):

    try:
        search = name
        db = open ('src/database/allgames.txt')

        for line in db:
            if search in line:
                return json.loads(line)
        db.close()
    
    except IOError as error: 
        return f"Message: {error}"


@app.route('/filter_api/<appid>')
def filter_api(appid):

    try:
        db_game = search_name(appid)
        game_categories = db_game.get(appid).get('categories')
        
        all_games = open ('src/database/allgames.txt')
        lines = all_games.readlines()

        similar_games = {'categories': [], 'genres': [], 'developers':[]}
        peso = 0

        for comparison_line in lines:
            aux_line = json.loads(comparison_line)
            aux_game_id = list(aux_line.keys())[0]
            aux_categories = aux_line.get(aux_game_id).get('categories')

            for categorie in game_categories: 
                for i in aux_categories:
                    if categorie.get('id') == i.get('id'):
                        peso += 1
            save = {'appid': list(aux_line.keys())[0], 'peso': peso}
            similar_games['categories'].append(save)  

            peso = 0
        return similar_games
    
    except IOError as error: 
        return f"Message: {error}"

@app.route('/graph/<appid>')
def get_graph(appid):
    return appid


