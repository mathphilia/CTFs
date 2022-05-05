import os
from collections import Counter

paths = os.listdir('out')
content = {}

for path in paths:
    with open('out/' + path) as f:
        content[path] = f.read()

counter = Counter(content.values())

for path in paths:
    if counter[content[path]] == 1:
        print(path)
