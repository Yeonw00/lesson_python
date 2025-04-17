# lambda 사용법
def other_func(f):
    print(f(10))

def normal_func(x):
    return x * 2

# lambda x: x * 2

other_func(normal_func)
other_func(lambda x: x * 2)
other_func(lambda x: x * 5)

y = None
# y에 값이 있으면 1 아니면 2
x = 1 if y else 2
print(x)

def base(x):
    def plus(y):
        return x + y
    return plus

plus = base(10)
print(plus(10))
print(plus(30))

i = 0
def add_num():
    def plus(y):
        return i + y
    return plus

i = 10
plus = add_num()
print(plus(10))
i = 100
print(plus(30))

def hello_decorator():
    pass

@hello_decorator
def recommend_restaurant():
    pass

# 이건 옛날 방식
#recommend_restaurant() = hello_decorator(recommend_restaurant())
# 요즘은 decorator를 쓰는 편


