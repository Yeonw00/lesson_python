import os
import pathlib
import glob
import shutil

# print(os.path.exists('test.csv'))
# print(os.path.isfile('test.csv'))
# print(os.path.isdir('test.csv'))

# os.rename('test.csv', 'renamed.csv')
# os.symlink('renamed.csv', 'symlink.csv')

# os.mkdir('test_dir')
# 디렉토리 안에 아무것도 없을 때는 이렇게 삭제 가능
# os.rmdir('test_dir')

# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# print(os.listdir('test_dir'))
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# shutil.copy('test_dir/test_dir2/empty.txt',
#             'test_dir/test_dir2/empty2.txt')
# print(glob.glob('test_dir/test_dir2/*'))

# 디렉토리 안에 파일이 있을 경우는 이렇게 삭제 해야함
# shutil.rmtree('test_dir')

#지금 디렉토리의 위치를 알고 싶을 때
print(os.getcwd())

