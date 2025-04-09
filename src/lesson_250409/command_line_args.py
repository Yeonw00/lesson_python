# 1. 콘솔에서 py가 있는 경로로 이동
# 2. python command_line_args.py -> commannd_line_args.py 파일 실행 됨
# 3. python command_line_args.py option1 option2 -> ['.\\command_line_args.py', 'option1', 'option2'] 반환
# 4. python command_line_args.py option1 option2 option3 -> ['command_line_args.py', 'option1', 'option2', 'option3'] 반환
import sys
print(sys.argv)