import logging
from pathlib import Path

# 1. 로거 생성 (이름을 라이브러리명으로 지정)
logger = logging.getLogger("engine")
logger.setLevel(logging.INFO) # 어디까지 보여줄지 설정 (DEBUG, INFO, WARNING 등)

# 2. 출력 포맷 설정 (시간 - 이름 - 레벨 - 메시지)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# 3. 콘솔 핸들러 (화면에 뿌리기)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# 4. 파일 핸들러 (파일에 저장하기)
# images_processed 폴더 안에 로그 저장
Path("logs").mkdir(exist_ok=True)
file_handler = logging.FileHandler("logs/process.log", encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

