import dbm

# with dbm.open('cache.db', 'c') as db:
#     db['key1'] = 'value1'
#     db['key2'] = 'value2'
# 값에 정수형은 못 넣음
# ex) db['key3'] = 1

with dbm.open('cache.db', 'r') as db:
    print(db.get('key1'))