import requests

def git(name):
    req = requests.get('https://api.github.com/users/'+ name +'/repos')

    json = req.json()

    for k in range(0, len(json)):
        print(json[k]["name"])