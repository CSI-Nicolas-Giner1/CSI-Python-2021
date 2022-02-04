from asyncore import loop
import os
import json, ssl
from pathlib import Path
from urllib import response
import urllib.request
from Nation import Nation

ssl._create_default_https_context = ssl._create_unverified_context

nationURL = "https://random-data-api.com/api/nation/random_nation?size=100"

nations:Nation = []

myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')
os.mkdir(myFolderPath)

for i in range(100):
    req = urllib.request.Request(nationURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    for r in requestData:
        newNation:Nation = Nation(**r)
        nations.append(newNation)
        print(newNation.uid)

        myFilePath = os.path.join(myFolderPath, f'response{newNation.uid}.json')

        with open(myFilePath, 'w') as outfile:
            json.dump(newNation.__dict__, outfile)

