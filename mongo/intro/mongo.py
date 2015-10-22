import random
from pymongo import MongoClient

# connection = MongoClient('hostname')
connection = MongoClient()

# connection.admin = use admin
# connection['admin'] = use admin
# admin is a special db used for usernames / pw

## db = connection.admin
## To authenticate after connecting
## db.authenticate('username','password')

db = connection['pd5']
print db.collection_names()

names = ["Thluffy", "Bucky", "Susan", "Victor", "Sarah", "Kictor"]

dtype = ['plain','frosted','glazed','jelly']

l = []
for l in range(10):
    d = {'name':random.choice(names),
         'donut':random.choice(dtype),
         'age':random.randrange(10,30)}
    db.people.insert(d);

res = db.people.find({'donut':'jelly'}).sort('age')
for r in res:
    print r
