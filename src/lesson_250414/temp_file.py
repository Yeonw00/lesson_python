import tempfile

# 일시적인 파일
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# 파일 만든 후 지우고 싶지 않다면
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# 일시적인 폴더
with tempfile.TemporaryDirectory() as td:
    print(td)

# 일시적인 폴더가 지워지지 않도록 할 때
temp_dir = tempfile.mkdtemp()
print(temp_dir)