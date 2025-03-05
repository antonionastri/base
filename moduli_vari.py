# math
import math

x = math.sqrt(64)
print(x)

x = math.ceil(1.2)  # 2

import random

r = random.randint(1, 6)
print(r)

lista = ["mo", "bo", "rm", "pa"]
r = random.choice(lista)

random.shuffle(lista)
print(lista)

estratti = []
r = random.randint(1, 90)
if r not in estratti:
    estratti.append(r)

print(estratti)

# json

# da json a python
import json

x = '{ "name": "john", "age":30, "city": "new york"}'
print(type(x))

y = json.loads(x)
print(type(x))
print(y["name"])

# da python (list o dict) a json
x = {"name": "john", "age": 30, "city": "new york"}
y = json.dumps(x)

# requests
import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts")

if resp.status_code == 200:
    body = resp.text

    with open("articoli.json", "wt") as f:
        f.write(body)
    
    posts = resp.json()
    
    print(posts[1]["title"])


# altra request per immagine
resp = requests.get("https://cdn-imgix.headout.com/media/images/c90f7eb7a5825e6f5e57a5a62d05399c-25058-BestofParis-EiffelTower-Cruise-Louvre-002.jpg?auto=format&w=1051.2&h=540&q=90&fit=fit")

if resp.status_code == 200:

    with open("eiffel.jpg", "wb") as f:
        f.write(resp.content)
    