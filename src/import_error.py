try:
    from lesson_250409 import utils
except ImportError:
    from lesson_250409.tools import utils

print(utils.say_twice('word'))