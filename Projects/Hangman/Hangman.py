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

attempted_letters = []

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
        
        attempted_letters.append(Start)
        return Start
    
print(get_input())

def print_word():
    Tempt:str=" "
    for Start in newNation.nationality:
        if Start in attempted_letters:
            Tempt+= Start
        else:
            Tempt+= " _ "
    print(Tempt)

def print_steps():
    mistake = 0
    for Start in attempted_letters:
        if Start not in newNation.nationality:
            mistake = mistake + 1
        if mistake > 6:
            print ("Game Over. Start again!")
             

    
    print (Steps[mistake])

while True:
    get_input()
    print_word()
    print_steps()
