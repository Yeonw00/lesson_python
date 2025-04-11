s = """AAA
BBB
CCC
DDD
"""
with open('test3.txt', 'w') as f:
    f.write(s)

with open('test3.txt', 'r') as f:
    # 파일 전체 읽어오기
    # print(f.read())
    # 한줄 씩 읽어오기
    # while True:
    #     line = f.readline()
    #     print(line, end='')
    #     if not line:
    #         break
    # chunk로 읽어오기
    # 예: 네트워크에서 패킷 단위로 읽어올 때 쓰임
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break
