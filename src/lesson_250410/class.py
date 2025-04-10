class Person(object):
    # 생성자
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)

    # 소멸자
    def __del__(self):
        print('good bye')


person = Person('Odung')
person.say_something()

del person

print('###########')

def person(name):
    if name == 'A':
        print('hello')
