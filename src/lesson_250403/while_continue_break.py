count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while True:
    if count >= 5:
        break # while문에서 빠져나와라
    if count == 2:
        count += 1
        continue # while문으로 바로 올라가라
    print(count)
    count += 1