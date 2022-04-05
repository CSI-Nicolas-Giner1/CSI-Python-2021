# import webbrowser
# webbrowser.open("https://www.mangasee123.com/manga/Hajime-No-Ippo")
import requests 
res = requests.get("https://www.gutenberg.org/cache/epub/67766/pg67766.txt")
print(len(res.text))
print(res.text[:300])