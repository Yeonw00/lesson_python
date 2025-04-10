class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

a = Person()
print(a)
print(a.x)
print(a.kind)
print(a.what_is_your_kind())
print('###########')
b = Person
print(b)
# b는 오브젝트가 아니기 때문에 Person의 메소드 불러오지 못함
# print(b.x)
# gloabal 변수에는 접근 가능
print(b.kind)
# @classmethod에는 접근 가능
print(b.what_is_your_kind())
b.about(1999)