from http.client import responses
from importlib.resources import path
import json
import os
from pathlib import Path
from Nation import Nation

myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'nation.json')
data = open(myFilePath,)

data= json.load(data)
nation:Nation = Nation(**data)

print(f"id: {nation.id}")
print(f"uid: {nation.uid}")
print(f"nationality: {nation.nationality}")
print(f"language: {nation.language}")
print(f"capital: {nation.capital}")
print(f"national sport: {nation.national_sport}")
print(f"flag: {nation.flag}")
print("Others expected...")