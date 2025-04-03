count = 0

while count < 5:
    if count == 1:
        # while문 안에 break가 있으면 else 실행하지 않고 여기서 종료
        break
    print(count)
    count += 1
# while문 안에 break가 없을 때 else를 실행하고 while문 종료
else:
    print('done')