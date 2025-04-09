# https://docs.python.org/ko/3.13/library/index.html

s = "sdfagswegasdfwvsdfwt"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)


d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

# 표준 라이브러리는 import해서 써야함
from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)

print(d['s'])