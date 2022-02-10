import json, ssl
import os
from pathlib import Path
import urllib.request
from Nation import Nation

ssl._create_default_https_context = ssl._create_unverified_context

nationURL = "https://random-data-api.com/api/nation/random_nation"



req = urllib.request.Request(nationURL)
requestData = json.loads(urllib.request.urlopen(req).read())

newNation:Nation = Nation(**requestData)
print(newNation.nationality)

Steps = ["""
|-----------|
|           o
|          
|          
|
|
|
""",
"""
|-----------|
|           o
|           |
|          
|
|
|
""",
"""
|-----------|
|           o
|          /|
|          
|
|
|
""","""
|-----------|
|           o
|          /|\\
|          
|
|
|
""",
"""
|-----------|
|           o
|          /|\\
|          /
|          
|
|
|
""",
"""
|-----------|
|           o
|          /|\\
|          / \\
|          
|
|
|
"""
]

print(Steps[0])

print(len(newNation.nationality)*" _ ")






