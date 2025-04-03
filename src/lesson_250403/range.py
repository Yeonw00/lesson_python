# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in num_list:
#     print(i)

for i in range(10):
    print(i)

print('###########################')

for i in range(2, 10):
    print(i)

print('###########################')

for i in range(2, 10, 3):
    print(i)

print('###########################')

for i in range(10):
    print(i, 'hello')

print('###########################')

# _를 쓰면 인덱스는 안쓴다는 것을 명시적으로 표현
for _ in range(10):
    print('bye')