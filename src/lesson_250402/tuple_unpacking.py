num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(f'x = {x}')
print(f'y = {y}')

x, y = 30, 40
print(f'x = {x} , y = {y}')

min, max = 0, 100
print(min, max)

# 너무 많은 변수를 한번에 튜플에 넣는 것은 지양할 것 (두개 정도가 적당)
# 예: a, b, c, d, e, f = 'Mike', '1', '1', '1', 'e', 'f'

i = 10
j = 20
print(i, j)
tmp = i
i = j
j = tmp
print(i, j)

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)