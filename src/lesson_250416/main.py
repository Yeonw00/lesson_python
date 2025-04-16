"""
pip install pep8
pip install flake8
pip install pylint

"""
import os


import roboter.controller.conversation

def main():
    roboter.controller.conversation.talk_about_restaurant()

if __name__ == '__main__':
    main()

y           = 1
x = {'sfadffdsfa',        "dsafsdfs"}

"""
pep8 main.py 실행 시
main.py:13:2: E221 multiple spaces before operator
main.py:22:20: W291 trailing whitespace
main.py:28:1: W391 blank line at end of file

flake8 main.py 실행 시 
main.py:9:1: F401 'os' imported but unused
main.py:13:2: E221 multiple spaces before operator
main.py:14:18: E231 missing whitespace after ','
main.py:23:20: W291 trailing whitespace
main.py:29:1: W391 blank line at end of file

pylint main.py 실행 시 
************* Module src.lesson_250416.main
main.py:30:0: C0305: Trailing newlines (trailing-newlines)
main.py:8:0: E0401: Unable to import 'roboter.controller.conversation' (import-error)
main.py:13:0: C0103: Constant name "y" doesn't conform to UPPER_CASE naming style (invalid-name)
main.py:9:0: C0411: standard import "os" should be placed before first party import "roboter.controller.conversation"  (wrong-import-order)
main.py:9:0: W0611: Unused import os (unused-import)

-----------------------------------
Your code has been rated at 0.00/10


"""

