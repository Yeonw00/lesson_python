class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('car run')

class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
# Person과 Car 둘다 run이 있을 때 PersonCarRobot()에서 왼쪽에 먼저 적은 것 우선으로 나옴
# -> PersonCarRobot(Person, Car) => Person
# Person.run()
person_car_robot.run()
person_car_robot.fly()