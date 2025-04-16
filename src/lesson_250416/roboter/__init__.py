from pathlib import Path

from lesson_250416.settings import CSV_FILE_PATH

path = Path(CSV_FILE_PATH)
path.parent.mkdir(parents=True, exist_ok=True)  # ✅ 폴더 생성
path.touch(exist_ok=True)                       # ✅ 이제 파일 생성 안전함
