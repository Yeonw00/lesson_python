i = [1, 2, 3, 4, 5]
j = i
# 같은 참조값에 대입하기 때문에 i[0]에도 값이 들어감
j[0] = 100
print('j = ', j)
print('i = ', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
#y = x[:]
y[0] = 100
print(f'y = {y}')
print(f'x = {x}')

x = 20
y = x
y = 5
print(id(y))
print(id(x))
print(y)
print(x)

x = ['a', 'b']
y = x
y[0] = 'p'
print(id(y))
print(id(x))
print(y)
print(x)