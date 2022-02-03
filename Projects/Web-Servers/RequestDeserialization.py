import os
import json, ssl
from pathlib import Path
import urllib.request
from Nation import Nation

ssl._create_default_https_context = ssl._create_unverified_context

nationURL = "https://random-data-api.com/api/nation/random_nation?size=100"

nations:Nation = []

myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')
os.mkdir(myFolderPath)

req = urllib.request.Request(nationURL)
requestData = json.loads(urllib.request.urlopen(req).read())

for r in requestData:
    nations:Nation = Nation(**r)
    nations.append(nations)
    print(Nation.id)

myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'responses')

with open(myFolderPath, 'w') as outfile:
        json.dump([data.__dict__ for data in Nation], outfile)

