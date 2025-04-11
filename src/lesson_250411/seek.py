s = "AAA\nBBB\nCCC\nDDD\n"

# with open('test4.txt', 'w', newline='\n') as f:
#     f.write(s)

with open('test4.txt', 'r') as f:
    print(f.tell())
    print(f.read(1))
    f.seek(5)
    print(f.read(1))
    f.seek(14)
    print(f.read(1))
    f.seek(5)
    print(f.read(1))

# with open('test4.txt', 'r') as f:
#     content = f.read()
#     for i, c in enumerate(content):
#         print(f'{i}: {repr(c)}')

# with open('test4.txt', 'r') as f:
#     content = f.read()
#     print(f'총 길이: {len(content)}')
#     for i, c in enumerate(content):
#         print(f'{i}: {repr(c)}')
#
#     f.seek(14)
#     print('---')
#     print('f.seek(14) →', repr(f.read(1)))
#     f.seek(15)
#     print('f.seek(15) →', repr(f.read(1)))


