def say_something():
    print('hi')

say_something()

# <class 'function'>
print(type(say_something))

f = say_something
f()


def say_anything():
    s = 'bye'
    return s

result = say_anything()
print(result)

def what_is_this(color):
    if color == 'pink':
        return 'cotton candy'
    elif color == 'violet':
        return 'egg plant'
    else:
        return 'I don\'t know'

result = what_is_this('pink')
print(result)
result = what_is_this('violet')
print(result)
result = what_is_this('yellow')
print(result)