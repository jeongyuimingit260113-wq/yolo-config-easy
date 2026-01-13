import yaml
import os
from pathlib import Path


def get_process_config(target_yaml):
    # 1. 현재 파일(loader.py)의 위치를 기준으로 프로젝트 루트 찾기
    # .parent를 사용해 'utils' -> 'src' -> 'Root'로 올라감
    current_path = Path(__file__).resolve()
    root_path = current_path.parent.parent.parent

    # 2. 루트 폴더 기준으로 config 파일 경로 설정
    config_path = root_path / "config" / target_yaml

    # 3. 파일 읽기
    if not config_path.exists():
        raise FileNotFoundError(f"설정 파일을 찾을 수 없습니다: {config_path}")

    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


get_process_config()