# with open('my_thoughts.txt', 'w', encoding='utf-8') as f:
#     f.write('오늘은 그냥 아무것도 하기 싫은 날이었다. \n그래도 나는 이 파일을 만들었다.')

with open('my_thoughts.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print('파일 내용 :\n', content)