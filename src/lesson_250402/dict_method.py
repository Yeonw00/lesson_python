d = {'x': 10, 'y': 20}
print(d)
# print(help(d))

# key만 필요할 때
print(d.keys())

# value만 필요할 때
print(d.values())

d2 = {'x': 1000, 'j': 500}
print(d2)
# d를 d2로 덮어씌우라는 의미
d.update(d2)
print(d)

print(d['x'])
print(d.get('x'))

# 이렇게 하면 KeyError
# print(d['z'])

# 이렇게 하면 값이 None
print(d.get('z'))

# x를 꺼내고 싶을 때
print(d.pop('x'))
# pop 이후에 x의 키와 값은 d에서 사라짐
print(d)

# y의 키-값을 삭제하라
del d['y']
print(d)

# d 자체를 삭제(del 쓸 땐 주의!)
del d
# 삭제 되었기에 d가 정의 되어 있지 않음
# print(d)

d = {'a': 100, 'b': 200}
print(d)

# 사전형의 안의 값을 다 지움
d.clear()
# {}
print(d)

d = {'a': 100, 'b': 200}
# True
print('a' in d)
# False
print('j' in d)
