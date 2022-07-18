import pymongo
client = pymongo.MongoClient("mongodb+srv://debabrata:Sintu123@cluster0.kafju.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name": "Chitra",
    "mail": "chitrachakraborty2011@gmail.com",
    "surname": "Sahoo"
}
d={
    "name": "Chitra",
    "mail": "chitrachakraborty2011@gmail.com",
    "surname": "Sahoo"
}
d={
    "name": "Chitra",
    "mail": "chitrachakraborty2011@gmail.com",
    "surname": "Sahoo"
}
db2= client['mongotest']
coll=db2['test']
coll.insert_one(d )

