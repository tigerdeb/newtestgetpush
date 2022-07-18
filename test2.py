import pymongo
client = pymongo.MongoClient("mongodb+srv://debabrata:<Sintu>@cluster0.kafju.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={
    "name" : "Deba",
    "email" : "debutiger@gmail.com",
    "surname" : "Chakra"

}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
