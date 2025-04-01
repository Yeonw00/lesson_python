print('a is {}'. format('a'))
print('a is {}'. format('test'))
print('a is {} {} {}'. format(1, 2, 3))
print('a is {0} {1} {2}'. format(1, 2, 3))
print('a is {2} {1} {0}'. format(1, 2, 3))
print('My name is {0} {1}'. format('Yeonwoo', 'Kang'))
print('My name is {0} {1}. 저는 {1} {0} 입니다 .'.format('Yeonwoo', 'Kang'))
print('My name is {name} {family}. 저는 {family} {name} 입니다 .'.format(name = 'Yeonwoo', family = 'Kang'))

print(1)
print('1')
print(str(1))
x = str(1)
print(type(x))

# f-strings
a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Yeonwoo'
family = 'Kang'
print(f'My name is {name} {family}. I am {family} {name}')