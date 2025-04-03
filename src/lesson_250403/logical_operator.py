a = 2
b = 2

# a가 b와 같다
if a == b:
    print('equal')

# a가 b와 다르다
a != b

# a가 b보다 작다
a < b

# a가 b보다 크다
a > b

# a가 b 이하다
a <= b

# a가 b 이상이다
a >= b

# a도 b도 양수이다
# and를 쓰지 않으면 이런식으로 써야함
"""
if a > 0:
    if b > 0:
        print('a and b are positive')
"""
if a > 0 and b > 0:
    print('a and b are positive')


# a 또는 b가 양수이다
a = 1
b = -1
# or을 안쓰고 쓰면 이렇게 할 수 있다
"""
if a > 0:
    print('a or b is positive')
elif b> 0:
    print('a or b is positive')

"""
if a > 0 or b > 0:
    print('a or b is poisitive')