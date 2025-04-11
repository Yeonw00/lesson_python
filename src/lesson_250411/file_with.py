# with를 쓰면 마지막에 f.close() 하지 않아도 됨
with open('test2.txt', 'w') as f:
    f.write('Test\n')