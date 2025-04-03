is_empty = None
# print(help(is_empty))

# 이 방식은 추천하지 않음
# if is_empty == None:
if is_empty is None:
    print('None!!!')
if is_empty is not None:
    print('not none!')

# 값을 비교 - True
print(1 == True)
# object끼리 비교 - False
print(1 is True)
# object끼리 비교 - True
print(True is True)
print(None is None)