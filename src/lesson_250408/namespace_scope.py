"""
Test Test ############
"""
animal = 'cat'

def f():
    animal = 'dog'
    print(f.__name__)
    print('after', locals())
f()
print(__name__)
print('global:', globals())