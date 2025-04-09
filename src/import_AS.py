# import lesson_250409.utils
# from lesson_250409.utils import say_twice
# from lesson_250409 import utils as u

# 가장 추천하는 방법
from src.lesson_250409.tools import utils
from lesson_250409.talk import human
from lesson_250409.talk import animal

# talk.__init__.py에 해당 모듈을 추가하면 되지만 추천하지 않는 방법
# from lesson_250409.talk import *


# r = lesson_250409.utils.say_twice('hello')
# r = say_twice('hello')

r = utils.say_twice('hello')
print(r)

print(human.sing())
print(human.cry())

print(animal.sing())
print(animal.cry())