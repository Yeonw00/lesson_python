s = "AAA\nBBB\nCCC\nDDD\n"

# w+
# with open('test5.txt', 'w+', newline='\n') as f:
#     f.write(s)
#     f.seek(0)
#     print(f.read())

# r+
with open('test5.txt', 'r+', newline='\n') as f:
    print(f.read())
    f.seek(0)
    f.write(s)
