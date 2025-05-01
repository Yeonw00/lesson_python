import datetime

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'data': datetime.datetime.now(datetime.UTC)
}

stack2 = {
    'name': 'customer2',
    'pip': ['python', 'java'],
    'info': {'os': 'windows'},
    'data': datetime.datetime.now(datetime.UTC)
}

db_stacks = db.stacks
# stack_id = db_stacks.insert_one(stack1).inserted_id
# print(stack_id, type(stack_id))
# print('############')

# from bson.objectid import ObjectId
# str_stack_id = '68131f365ada8ff623ff9b8f'
# print(db_stacks.find_one({'_id': ObjectId(str_stack_id)}))

# print(db_stacks.find_one({'name': 'customer1'}))

# stack_id = db_stacks.insert_one(stack2).inserted_id
# print(stack_id, type(stack_id))
#
# for stack in  db_stacks.find():
#     print(stack)

# now = datetime.datetime.now(datetime.UTC)
# #lt는 last than(과거), gt는 greater than(미래)
# for stack in db_stacks.find({'data': {'$lt': now}}):
#     print(stack)


# 값 업데이트
# db_stacks.find_one_and_update(
#     {'name': 'customer1'}, {'$set': {'name': 'YYY'}})
# print(db_stacks.find_one({'name': 'YYY'}))

# 필드명 업데이트
# 대상 문서를 먼저 찾기
# doc = db_stacks.find_one({'name': 'customer2'})
#
# if doc and 'data' in doc:
#     # 기존 'data' 값을 가져와 'date' 필드로 설정하고 'data'는 삭제
#     db_stacks.update_one(
#         {'_id': doc['_id']},
#         {
#             '$set': {'date': doc['data']},
#             '$unset': {'data': ""}
#         }
#     )

# delete
db_stacks.delete_one({'name': 'YYY'})
# 삭제되었기 때문에 None으로 나옴
print(db_stacks.find_one({'name': 'YYY'}))