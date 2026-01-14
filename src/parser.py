import engine_utills as utl
import yaml
import preprocess as pre
import logging

logger =logging.getLogger('engine')

class ConfigProcess:
    def __init__(self,config_dir: str = None):
        self.data=utl.get_config('cv_and_yolo.yaml', config_dir)

    def parse(self):
        target_pipeline = self.data.get("pipeline")

        if target_pipeline is None:
            logger.exception
            raise ValueError("pipline 이 없습니다. pipline의 이름의 철자를 확인하시거나  깃헙의 형식을 지켜주시기 바랍니다.")

        for pipeline in target_pipeline:





