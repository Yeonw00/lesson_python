class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class HyundaiCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model 3',
                 enable_auto_run=False,
                 passwd='123'):
        # self.model = model
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')

car = Car()
car.run()

print('################')
hyundai_car = HyundaiCar('Genesis')
print(hyundai_car.model)
hyundai_car.run()
print('################')
tesla_car = TeslaCar('Model 3', passwd='456')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()

# property 설정 시 값 덮어쓰기 불가
# setter 설정 시 값 덮어쓰기 가능
tesla_car.enable_auto_run = True
print(tesla_car._enable_auto_run)

# __두개가 있으면 클래스 내에서는 접근할 수 있으나 오브젝트 생성 후 외부에서는 접근 못함
# 예: tesla_car.__enable_autor_run