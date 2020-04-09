import pymongo
import bson
# 连接MongoDB
client = pymongo.MongoClient(host='localhost', port=27017)
# client = MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client['test']
# db = client.test

lists = client.list_database_names()

if 'test' in lists:
    print('数据库已经存在')

# 指定集合
student = db['student']
# student = db.student

student_A = {
    'id': '2001',
    'name': 'Tom',
    'age': '10',
    'gender': 'male'
}

result = student.insert_one(student_A)
print(result)

result = student.find_one({'id': '2001'})
print(result)


student_B = {
    'id': 2002,
    'name': 'Mary',
    'age': '15',
    'gender': 'female'
}

result = student.insert_one(student_B)
print(result)


arr = []
for i in range(0, 5):
    std = {
        'id': 2002+i,
        'name': 'Mary',
        'age': '15',
        'gender': 'female'
    }
    arr.append(std)
result = student.insert_many(arr)
print(result)

print("=================")
results = student.find()
for res in results:
    print(res)

print("=================")

results = student.find({'name': {'$regex': '^M.*?'}})
results = student.find()
for res in results:
    print(res)