import pymongo
client = pymongo.MongoClient("mongodb+srv://phanisriramk:Phani123@cluster0.decec.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Phani",
    "email":"phanisriramk@gmail.com",
    "surname":"Kolavennu"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

d = {
    "name":"Phani",
    "email":"phanisriramk@gmail.com",
    "surname":"Kolavennu"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

d = {
    "name":"Phani",
    "email":"phanisriramk@gmail.com",
    "surname":"Kolavennu"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)