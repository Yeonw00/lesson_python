import os
import subprocess

#요즘은 추천하지 않는 방법
# os.system('dir')

# os보다 subprocess가 더 고기능(추천)
# shell=True는 삭제하는 명령어를 넣으면 쉽게 삭제할 수 도 있기 때문에 비추천
# check=True는 명령어 실행이 실패했을 때 오류를 내도록 만드는 옵션 -> subprocess.CalledProcessError
#  r = subprocess.run('dir', shell=True, check=True)
# print(r.returncode)

p1 = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, encoding='cp949')
p2 = subprocess.Popen('findstr test', shell=True, stdin=p1.stdout, stdout = subprocess.PIPE, encoding='cp949')
p1.stdout.close()
output = p2.communicate()[0]
print(output)

#dir /ah는 숨김파일 보여주라는 명령어