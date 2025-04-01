s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print('##############')

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))

# 제일 앞글자는 대문자 나머지는 소문자
print(s.capitalize())
# 단어마다 앞글자를 대문자로
print(s.title())
# 문자열을 전부 대문자로
print(s.upper())
# 문자열을 전부 소문자로
print(s.lower())

print(s.replace('Mike','Nancy'))