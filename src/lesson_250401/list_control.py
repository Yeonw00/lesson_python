s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)
print(s[0])
s[0] = 'X'
print(s)
print(s[2:5])
s[2:5] = ['C', 'D', 'E']
print(s)
s[2:5] = []
print(s)
print(s[:])
s[:] = []
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
n.append(100)
print(n)
n.insert(0, 200)
print(n)
# 리스트의 제일 뒤에있는 요소를 꺼집어냄
print(n.pop())
# 마지막 요소가 리스트에서 사라짐
print(n)
# 리스트의 0번째에 있는 요소를 꺼집어냄
print(n.pop(0))
# 0번째 요소가 리스트에서 사라짐
print(n)

# n의 0번째 요소를 삭제
del n[0]
print(n)

n = [1, 2, 2, 2, 3]
# 제일 처음의 2가 사라짐
n.remove(2)
print(n)
# 남의 두개의 2와 3도 지워줌
n.remove(2)
n.remove(2)
n.remove(3)
print(n)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(a)
print(b)
x = a + b
print(x)
print(a)
print(b)
a += b
print(a)

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
print(f'x = {x}')
print(f'y = {y}')
# x 리스트 안에 y값 넣어줌
x.extend(y)
print(f'x = {x}')