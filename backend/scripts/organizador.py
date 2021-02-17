import json

f = open('applistapi.json', 'r')

apps = f.read()

apps = json.loads(apps)

apps = apps['applist']['apps']

w = open('applist.txt', 'a+')

for app in apps:
    w.write(json.dumps(app)+'\n')

f.close()
w.close()