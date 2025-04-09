#https://docs.python.org/ko/3.6/library/functions.html
import builtins

# print는 내장함수
builtins.print("print is built-in function")

print(globals())

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

for key in ranking:
    print(key)

print('############')

print(sorted(ranking, key=ranking.get, reverse=True))