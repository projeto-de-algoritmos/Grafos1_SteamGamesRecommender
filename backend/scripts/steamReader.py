'''This Script serves to get data from games at consuming the Steam API'''

import json
import requests
import time

applistfile = open('applist.txt', 'r')

lastreadfile = open('lastread.txt', 'r')
lastread = int(lastreadfile.readline())
lastreadsuccess = int(lastreadfile.readline())
lastreadfile.close()

def savelastread(lastread, lastreadsuccess):
    lastreadf = open('lastread.txt', 'w+')
    lastreadf.write(str(lastread)+'\n')
    lastreadf.write(str(lastreadsuccess)+'\n')
    lastreadf.close()

savelastread(lastread, lastreadsuccess)

allgames = open('allgames.txt', 'a')
# dlc = list()

count = 0
applist = applistfile.readlines()
for appstr in applist:
    if count <= lastread:
        count += 1
        continue
    app = json.loads(appstr)
    lastread += 1
    # if dlc.count(app['appid']) > 0:
    #     savelastread(lastread, lastreadsuccess)
    #     continue

    if app['name'].isspace() or app['name'] == '':
        savelastread(lastread, lastreadsuccess)
        continue
    time.sleep(1.5)
    appinfo = requests.get('https://store.steampowered.com/api/appdetails/?appids='+str(app['appid']))

    if appinfo.status_code != 200:
        savelastread(lastread, lastreadsuccess)
        for i in range(0, 10):
            time.sleep(30)
            appinfo = requests.get('https://store.steampowered.com/api/appdetails/?appids='+str(app['appid']))
            if appinfo.status_code == 200:
                break
        if appinfo.status_code != 200:
            print("status code")
            break

    appinfo = json.loads(appinfo.text)
    appid = str(app['appid'])

    
    if appinfo == None:
        print("null")
        savelastread(lastread, lastreadsuccess)
        break

    if appinfo[appid]['success'] != True:
        savelastread(lastread, lastreadsuccess)
        continue

    data = appinfo[appid]['data']
    
    if data['type'] != 'game':
        savelastread(lastread, lastreadsuccess)
        continue
    
    # dlcs = data.get('dlc')
    # if dlcs != None:   
    #     for d in dlcs:
    #         dlc.append(d)

    if data.get('recommendations') == None:
        appinfo.clear()
        savelastread(lastread, lastreadsuccess)
        continue
    elif data.get('recommendations').get('total') < 5000:
        appinfo.clear()
        savelastread(lastread, lastreadsuccess)
        continue

    game = {}
    game[appid] = {}
    game[appid]['name'] = data.get('name')
    game[appid]['steam_appid'] = data.get('steam_appid')
    game[appid]['required_age'] = data.get('required_age')
    game[appid]['is_free'] = data.get('is_free')
    game[appid]['header_image'] = data.get('header_image')
    game[appid]['developers'] = data.get('developers')
    game[appid]['publishers'] = data.get('price_overview')
    game[appid]['categories'] = data.get('categories')
    game[appid]['genres'] = data.get('genres')
    game[appid]['recommendations'] = data.get('recommendations')
    game[appid]['release_date'] = data.get('release_date')
    # print(game)
    allgames.write(json.dumps(game)+'\n')
    
    game.clear()
    appinfo.clear()

    lastreadsuccess = lastread
    count += 1
    savelastread(lastread, lastreadsuccess)
    # if count >= 5:
    #     break
    # time.sleep(1.5)

applistfile.close()
allgames.close()
