import json

def search_names(name):
    
    try:
        search = name.lower()
        db = open ('src/database/allgames.txt')
        
        count = 0
        gameslist = []

        for line in db.readlines():
            game = json.loads(line)
            key = list(game.keys())[0]
            if search in game.get(key).get('name'):
                gameslist.append({'appid': key, 'name': game.get(key).get('name')})
                count += 1
                if count >= 10:
                    break
        db.close()
        return json.dumps(gameslist)
    
    except IOError as error: 
        return f"Message: {error}"


def search_game(appid):
    game_info = {}    
    try:
        search = appid
        db = open ('src/database/allgames.txt')

        for line in db.readlines():
            game = json.loads(line)
            for key in game:
                if key == appid:
                    game_info = destructure_game(game, key)
        db.close()
        return game_info
    
    except IOError as error: 
        return f"Message: {error}"

def destructure_game(game, key):
    game_info = {
        'appid': key,
        'name': game.get(key).get('name'),
        'categories': game.get(key).get('categories'),
        'genres': game.get(key).get('genres'),
        'developers': game.get(key).get('developers')
    }
    return game_info


def filter_api_(appid, visited=[], max_comparations = 20):

    try:
        db_game = search_game(appid)

        all_games = open ('src/database/allgames.txt')
        lines = all_games.readlines()

        # '''[{"appid": "xxx", "peso_categories" = a, "peso_genres" = b, "peso_developers" = c}, ...]'''
        similar_games = []

        for comparison_line in lines:
            aux_line = json.loads(comparison_line)
            aux_game_id = list(aux_line.keys())[0]

            visitedappids = []
            for visit in visited:
                visitedappids.append(visit.get('appid'))
                    
            if aux_game_id in visitedappids:
                continue

            aux_comparator = destructure_game(aux_line, aux_game_id)
            
            if hasEmptyProperty(aux_comparator):
                continue

            weights = {
                'appid': aux_game_id,
                'peso_categories': compare('categories', db_game, aux_comparator),
                'peso_genres': compare('genres', db_game, aux_comparator),
                'peso_dev': compare('developers', db_game, aux_comparator)
            }
            
            if filter_weights(weights):
                similar_games.append(weights)

            if len(similar_games) >= max_comparations:
                break

        all_games.close()
        return similar_games
    
    except IOError as error: 
        return f"Message: {error}"

def hasEmptyProperty(game):
    for keys in game:
        if game.get(keys) == None:
            return True
    return False

def filter_weights(weights, min_categories = 2, min_genres = 2, min_developers = 1):
    if weights.get('peso_dev') >= min_developers:
        return True
    elif weights.get('peso_categories') >= min_categories:
        return True
    elif weights.get('peso_genres') >= min_genres:
        return True
    return False

def compare(key, game_main, game_loop):
    weight = 0
    if key == 'developers':
        for dev in game_main.get(key):
            for dev_aux in game_loop.get(key):
                if dev == dev_aux:
                    weight += 1
    else:
        for categorie in game_main.get(key):
            for categorie_aux in game_loop.get(key):
                if categorie.get('id') == categorie_aux.get('id'):
                    weight += 1
    return weight

def bfs_filter(appid, maxlayer = 2):
    layer = 0
    fila = [[appid, layer]]
    visited = []
    visited.append(
        {
            'appid': appid,
            'name': search_game(appid).get('name')
        }
    )
    edges = []
    while len(fila) > 0:
        w, layer = fila.pop(0)

        w = search_game(w)

        if hasEmptyProperty(w):
            continue

        for visit in visited:
            if visit.get('appid') == w.get('appid'):
                visit['name'] = w.get('name')

        if layer >= maxlayer:
            continue

        w['similar_games'] = filter_api_(w.get('appid'), visited=visited)
        for v in w.get('similar_games'):
            if not (v.get('appid') in visited):
                fila.append([v.get('appid'), layer+1])
                visited.append({
                    'appid': v.get('appid')
                })
                edges.append({
                    'from': w.get('appid'),
                    'to': v.get('appid')
                })

    return {
        'nodes': visited,
        'edges': edges
    }

# if __name__ == '__main__':
    
    # print(search_names("this war"))
    # print(search_names("cel"))
    # print(search_names("G"))

    # print(compare('categories', search_game('282070'), search_game('504230')))
    # print(compare('genres', search_game('282070'), search_game('504230')))
    # print(compare('developers', search_game('282070'), search_game('504230')))

    # print(filter_api_('504230'))

    # print(search_game('282070'))
    # print(search_game('504230'))

    # print(bfs_filter('504230'))