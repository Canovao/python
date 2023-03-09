import json

fHandle = open('Knowledge.json')
data = json.load(fHandle)

for i in data:
    print(i)

fHandle.close()

# /Images -> All images
# Knowledges : Links -> All links