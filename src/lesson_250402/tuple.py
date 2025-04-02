t = (1, 2, 3, 4, 1, 2)
print(t)
print(type(t))
# 튜플은 list처럼 t[0] = 100 이런식으로 수치 변경은 불가
print(t[0])
print(t[-1])
print(t[2:5])
print(t.index(1))
print(t.index(1,1))
print(t.count(1))

# print(help(tuple))

# 튜플 안에 list 넣는 것은 가능
t = ([1, 2, 3], [4, 5, 6])
print(t)

t[0][0] = 100
print(t)