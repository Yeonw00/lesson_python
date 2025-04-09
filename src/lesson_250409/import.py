# 별로 추천하지 않는 방법
#import collections, sys, os

# 알파벳 순으로 쓰는게 읽기 쉬운 방법이라는 인식이 있음
import collections
import os
import sys

#thirdparty 라이브러리 import할 때는 한 줄 띄어서 써줄 것
import termcolor

# 같은 회사에서 다른 팀이 만든 프로젝트도 한 줄 띄어서 써줄 것
import src

# 자기 자신이 만든 경로도 한 줄 띄어서 써줄 것
import command_line_args


print(collections.__file__)
print(termcolor.__file__)
print(src.__file__)
print(command_line_args.__file__)

print(sys.path)