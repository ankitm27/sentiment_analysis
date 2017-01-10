import json

data = []
with open('python.json') as f:
    for line in f:
        data.append(json.loads(line))

for i in data:
    print i["text"]
