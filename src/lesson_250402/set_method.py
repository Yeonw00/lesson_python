s = {1, 2, 3, 4, 5}
print(s)
# 집합에는 순서가 없음
# print(s[0]) -> TypeError
s.add(6)
print(s)
s.remove(6)
print(s)
# 요소가 없어진 집합
s.clear()
print(s) # set()

# print(help(set))