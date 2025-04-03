x = 10

# if 다음 줄은 암묵적으로 스페이스 4칸
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('ten')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')


# debug 시에는 검사하고 싶은 부분에 브레이크 포인트 놓고 step over 또는 step into 쓰면서 한줄 씩 검사