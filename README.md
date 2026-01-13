# 🚀 YOLO Config Easy

YOLO 설정 및 CV 전처리 , 후처리를 하드코딩 하지 않고  YAML 파일로 쉽게 관리하기 위한 프로젝트입니다.

## 📂 폴더 구조
* `configs/`: YOLO 모델 및 데이터 설정 (YAML)
* `src/`: 전처리 및 실행 관련 파이썬 모듈
* `results/` : train 및 predict 결과 
* `data/`: 이미지 및 라벨 데이터셋

## 🛠️ 사용법
```text
│  main.py
│  README.md
│  
│          
├─configs
│      data.yaml
│      model.yaml
│      process.yaml
│      
├─data
│  ├─images
│  │  ├─train   이 파일에 원하시는 이미지를 넣어주시길 바랍니다. 
│  │  │      README.md  
│  │  │      
│  │  └─val    이파일에 검증용 파일을 넣어주시길 바랍니다. 
│  │          README.md
│  │          
│  ├─images_processed    
│  │  ├─train
│  │  │      README.md
│  │  │      
│  │  └─val
│  │          README.md   
│  │          
│  └─labels
│      ├─train
│      │      README.md
│      │      
│      └─val
│              README.md
│              
├─results
│  ├─predict_results
│  │      README.md
│  │      
│  └─train_results
│          README.md
│          
└─src
        parser.py
        preprocess.py
        yolo_predict.py
        yolo_train.py
        __init__.py
        
        
```