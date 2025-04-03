def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(10, 20)
print(r)

# int 인수형에 string타입 넣어도 파이썬에서는 에러가 나지 않음
r = add_num('a', 'b')
# ab
print(r)