print('hello')
print("hello")
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")

print('hello.\nHow are you?')

# 로우 데이터 표시
print(r'C:\name\name')

print('##############')
print("""\
line1
line2
line3\
""")
print('##############')

print('Hi.' * 3 + 'Mike.')

print('Py''thon')
prefix = 'Py'
print(prefix + 'thon')

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print('##############')
print(word[0:2])
print(word[:2])
print('##############')
print(word[2:])
print('##############')
word = 'j' + word[1:]
print(word[:])
n = len(word)
print(n)