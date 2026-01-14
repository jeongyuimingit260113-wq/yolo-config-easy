import yaml
import os
from pathlib import Path
import cv2
import numpy as np
import logging

# 이곳은 전체 파일 경로 처리 및 로직 흐름 제어
logger = logging.getLogger("engine")

def get_config(target_yaml: str, config_dir: str = None):
    """
    지정된 YAML 설정 파일을 로드합니다.

    Args:
        target_yaml (str): 설정 파일 이름 (예: 'config.yaml')
        config_dir (str, optional): 설정 파일이 위치한 폴더 경로.
                                   미지정 시 현재 작업 디렉토리의 'config' 폴더를 탐색.
    """

    # 1. 기준 경로 설정 (사용자 지정 우선 -> 없으면 실행 위치의 /config)
    if config_dir:
        base_path = Path(config_dir).resolve()
    else:
        base_path = Path.cwd() / "config"

    config_path = base_path / target_yaml

    # 2. 파일 존재 여부 체크 및 엄격한 가이드 제공
    if not config_path.exists():
        # 사용자가 알아먹기 쉽게 "기대하는 구조"를 시각적으로 표시
        expected_structure = f"""
        [설정 파일을 찾을 수 없습니다!]
        - 탐색 시도 경로: {config_path.absolute()}

        라이브러리 사용을 위해 아래와 같이 폴더 구조를 맞춰주세요:
        {Path.cwd().name}/
        ├── main.py (현재 실행 파일)
        └── config/
            └── {target_yaml}  <-- 이 파일이 필요합니다. (혹은 맞춤법을 확인해보세요) 

        만약 다른 폴더에 있다면 config_dir 인자를 사용하세요.
        """
        logger.error(expected_structure)
        raise FileNotFoundError(expected_structure)

    # 3. 파일 로드
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if data is None:
               logger.error(f"설정 파일이 비어있습니다: {config_path}")
               raise ValueError(f" ({target_yaml}) ")
        logger.info(f"성공적으로 YAML파일을 로드 했습니다.: {config_path.absolute()}")
        return data

    except yaml.YAMLError as e:
        logger.error(f"YAML 파일 형식이 잘못되었습니다: {e}")
        raise ValueError(f"{target_yaml} invalid format") from e




class GetData:
    def __init__(self):
        self.base_path = Path.cwd()
        self.data_path = self.base_path / "data" / "images"

        # 1. 폴더 자체가 없는 경우 체크
        if not self.data_path.exists():
            expected_structure = f"""
               파일 경로를 찾을 수가 없습니다. 
               루트 폴더: {self.base_path.name} 
               찾는파일의 절대 경로 : {self.data_path.absolute()} 
               꼭 깃헙의 파일 구조를 지켜주시길 바랍니다. 
               """
            logger.error(expected_structure)
            raise FileNotFoundError(expected_structure)

    def data_load(self):
        # 처리된 이미지를 저장할 폴더 생성
        os.makedirs('images_processed', exist_ok=True)

        # 2. PNG 파일 목록을 먼저 가져옴
        png_files = sorted(list(self.data_path.glob('*.png')))

        # 3. 만약 PNG 파일이 하나도 없다면 강제로 에러 발생
        if not png_files:
            logger.error(f"폴더 안에 png 파일을 꼭 채워주세요")
            raise FileNotFoundError(f"❌ '{self.data_path.absolute()}' no such PNG file")

        # 4. 파일이 존재할 때만 루프 실행
        for filepath in png_files:
            try:
                full_path = filepath.absolute()
                cv_img = cv2.imread(str(full_path))

                if cv_img is None:
                    logger.warning(f"⚠️ 경고: {filepath.name}을 읽을 수 없습니다. 건너뜁니다.")
                    continue

                yield cv_img , filepath.name

            except Exception as e:
                logger.exception(f"예상치 못한 오류 발생{e}")
                raise ValueError("Uncaught exception ") from e









