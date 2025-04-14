import zipfile
import glob


with zipfile.ZipFile('test.zip', 'w') as z:
    # z.write('test_dir')
    # z.write('test_dir/test.txt')
    for f in glob.glob('test_dir/**', recursive=True):
        # print(f)
        z.write(f)

with zipfile.ZipFile('test.zip', 'r') as z:
    # z.extractall('zzz2')
    # 파일 하나만 보고싶을 때는
    with z.open('test_dir/test.txt') as f:
        print(f.read())

# mac에서 터미널로 압축푸는 명령어:
# unzip test.zip -d zzz (zzz라는 폴더에 압축해제)