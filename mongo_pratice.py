from os import unsetenv
from sre_constants import SUCCESS
from ssl import _SrvnmeCbType
from tkinter import ALL
from bson import ObjectId
import pymongo
import bson
#連線到雲端
client = pymongo.MongoClient("mongodb+srv://root:root1234@atlascluster.dkq4s.mongodb.net/?retryWrites=true&w=majority")
db = client.test

collection = db.users
# find_doc = collection.find_one({
#     '$and':
#     [{'Name':'cotespa'},
#     {'gender':''}]})
cur = collection.find({
    '$or':
    [{'Name':'cotespa'},
    {'gender':'female'}]}, sort = [('level', pymongo.DESCENDING)])
for doc in cur:
    print(doc)

# for doc in find_doc:
#     print(doc)

# collection.delete_many({
#     'Name':'cotespa','gender':'male','status':'good','level':'3'
#     })
# collection.insert_many([{
#     'Name':'cotespa','gender':'male','status':'good','level':'3'
#     },{
#        'Name':'yinjin','gender':'female','status':'good','level':'2'
#     },{
#         'Name':'jinjin','gender':'unknown','status':'unknown','level':'1'
#     }]
#     )
print('successed')

# res = collection.find_one({
#         'Name':'cotespa'})
# print(res)
# print(res.modified_count)
# data = collection.find_one()
# data = collection.find_one(ObjectId['62b93544f75a10c7ff2b294d'])
# print(data)
# print(data['_id'])
# print(data['Name'])
# cur = collection.find()
# for i in cur:
#     print(i['_id'])
# res = collection.insert_many([{
#     'Name':'cotespa',
#     'gender':'male',
#     },{
#     'Name':'cotespa',
#     'gender':'male'
#     }])

# print(res.inserted_ids)
# print('successful accessed')  