def g():
    for i in range(10):
        yield i

g = g()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# 튜플로 하고 싶을땐 괄호 앞에 tuple이라고 선언
# g = tuple(i for i in range(10))

# generator는 괄호만 쓰면 됨
g= (i for i in range(10) if i % 2 == 0)
print(type(g))

for x in g:
    print(x)