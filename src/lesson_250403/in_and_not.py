y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

# 여기선 not을 쓰는 걸 추천하지 않음
# if not a == b:
#     print('Not equal')

#추천하는 방식은
if a != b:
    print('Not equal')

is_ok = True
# boolean 타입은 == True라고 하지않고 if 변수명: 하면 됨
if is_ok:
    print('hello')
is_ok = False
# boolean 타입 False인 경우
if not is_ok:
    print('I\'m not ok')