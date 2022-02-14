from ast import Return
from asyncio.windows_events import NULL
import json, ssl
import numbers
import os
import random
from pathlib import Path
from telnetlib import theNULL
from tokenize import Number
from tracemalloc import start
import urllib.request
from Nation import Nation

ssl._create_default_https_context = ssl._create_unverified_context

nationURL = "https://random-data-api.com/api/nation/random_nation"



req = urllib.request.Request(nationURL)
requestData = json.loads(urllib.request.urlopen(req).read())

newNation:Nation = Nation(**requestData)
# print(newNation.nationality)

Steps = ["""
|------------|
|
|
|
|
|
|
""",
""""
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

def get_input():
    while(True):
        Start= input(f"Name a letter for this nationality: ")

        if(len(Start) != 1):
            print("error")
            continue
        if()
        return Start



    

print(get_input())