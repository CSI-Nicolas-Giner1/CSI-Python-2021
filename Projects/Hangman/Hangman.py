import json, ssl
from pipes import Template
from tempfile import template
from tracemalloc import start
import urllib.request
from Nation import Nation

ssl._create_default_https_context = ssl._create_unverified_context

nationURL = "https://random-data-api.com/api/nation/random_nation"

special_character = "[@_!#$%^&*()<>?/\|}{~:]')"

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
            print("Error. It's too long. Try again")
            continue
        if(Start.isnumeric()):
            print("Error. Don't use a number. Try again.")
            continue 
        if(Start in special_character):
          print("Error. Don't use special characters.")
          continue 

        return Start
    
print(get_input())

def print_word():
    Tempt:str=" "

    for Start in print_word:

        for (matches) or in():
            {temp+="_" or Start
        
        return or print
        temp} 


print(print_word())