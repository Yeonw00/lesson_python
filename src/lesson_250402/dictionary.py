d = {'x': 10, 'y': 20}
print(d)
print(type(d))
print(d['x'])
print(d['y'])

d['x'] = 100
print(d)
# 문자열도 대입 가능
d['x'] = 'XXXX'
print(d)
# 새로운 key-value도 대입 가능
d['z'] = 200
print(d)
# key가 숫자여도 됨
d[1] = 10000
print(d)

print(dict(a=10, b=20))

print(dict([('a', 10), ('b',20)]))