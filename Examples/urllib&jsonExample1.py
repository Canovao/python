import json
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1636409.json").read().decode()

info = json.loads(fhand)

total = 0
for item in info['comments']:
    total += item['count']
print(total)