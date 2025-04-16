import os
import platform

if platform.system() == 'Windows':
    CSV_FILE_PATH = 'tmp/test.csv'  # 상대경로로 안전하게
else:
    CSV_FILE_PATH = '/tmp/test.csv'

TEMPLATE_PATH = None