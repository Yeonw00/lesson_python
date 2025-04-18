import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    # 계승한 클래스에서는 꼭 실행해달라는 의미
    @abc.abstractmethod
    def drive(self):
        pass

    # def drive(self):
    #     if self.age >= 18:
    #         print('ok')
    #     else:
    #         raise Exception('No drive')

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No drive')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('ok')

baby = Baby()
# baby.drive()
adult = Adult()
adult.drive()

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, person):
        person.drive()

car = Car()
# car.ride(baby)
car.ride(adult)