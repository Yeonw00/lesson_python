# 표준 라이브러리 먼저 알파벳 순으로 쓰고
import os
import sys

# 써드파티 라이브러리를 쓰고
# import flask

# 로컬의 패키지를 씀
import roboter.controller.conversation


class MainError(Exception):
    pass


# 이렇게 쓰는게 좋은 코딩
def do_it():
    try:
        roboter.controller.conversation.talk_about_restaurant()
    # except할 때 모든 exception은 안적는게 좋음
    # except Exception as exc:
    #     print(exc)
    except:
        raise MainError('error')

# 코드 읽기 힘든 방식이므로 지양할 것
# x = [(i, x, y) for i in [1,2,3] for x in [1,2,3] for y in [1,2,3]]


d = {'key1': 'value1', 'key2': 'value2'}
if 'key1' in d:
    print('test')

# 위의 방식을 더 추천
# if 'key1' in d.keys():
#     print('test')

# 딕셔너리 전개
# 줄이 길어질 때는 변수명 알기 쉽게 설정할 것 예:k, v 말고 name, count
for k, v in d.items():
    print(k, v)

# 제너레이터는 메모리에서 빨리 움직이기때문에 for문보다 좋은 경우가 있음
def t():
    num = []
    for i in range(10):
        yield i
        # num.append(i)
    # return num

for i in t():
    print(i)