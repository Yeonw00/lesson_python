# 파이썬은 변수 선언 시 타입을 쓰지 않아도 됨
# 변수명은 숫자로 시작하면 안됨

num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

number = '1'
new_num = int(number)

print(new_num, type(new_num))

print('Hi','Mike')
print('Hi', 'Mike', sep=',', end='')
print('Hi', 'Mike', sep=',', end='\n')
print('Hi', 'Mike', sep=',', end='.\n')