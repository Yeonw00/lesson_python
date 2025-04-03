def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)

y = [1, 2, 3]
r = test_func(200, y)
print(r)

# l 인수는 안넣어서 자동으로 빈 리스트에 100을 넣음
r = test_func(100)
print(r)

# 한번 더 실행하면 100이 들어간 리스트가 나옴
r = test_func(100)
print(r)

# 파이썬에서 디폴트 인수로 list나 dict를 쓰면 버그가 생길 가능성 있음
# 디폴트 인수로 빈 list를 쓰고 싶다면 l = None으로 씀
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func(100)
print(r)

# 한번 더 실행하면 100이 들어간 리스트가 나옴
r = test_func(100)
print(r)
