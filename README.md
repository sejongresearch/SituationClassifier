# SituationClassifier

## Situation classification using obstacle detection
> 장애물 검출을 통한 상황 분류

### Team
| 이름 | 학과 | 학번 | 구성 | 역할 |코드|
|:---:|:---:|:---:|:---:|:---:|:---:|
| **위성민** | 무인이동체공학전공 | 17011877 | **팀장** | 도로 검출 |[Road Detection](https://github.com/sejongresearch/SituationClassifier/blob/master/roaddetection.ipynb) [Free Space Detection](https://github.com/sejongresearch/SituationClassifier/blob/master/freespacedetection.ipynb)|
| 최용호 | 스마트기기공학전공 | 17013253 | 팀원 | 깊이 추정 |~~[뎁스](링크)~~ |
| 권영서 | 무인이동체공학전공 | 17011794 | 팀원 | UI |[GUI](https://github.com/sejongbhaj/SituationClassifier/blob/master/GUI.py#L8) |
| 김남훈 | 스마트기기공학전공 | 17011832 | 팀원 | 객체 검출 | [물체 검출](https://github.com/sejongresearch/SituationClassifier/blob/master/ODTA_SejongBHAJ_OneClick(for_Marking).ipynb)|
| 강산희 | 무인이동체공학전공 | 17011855 | 팀원 | 데이터셋 | |

---
- [논문](https://github.com/sejongresearch/SituationClassifier/blob/master/SejongBHAJ.pdf)
- [PPT](https://drive.google.com/file/d/12MXcc1t8vGPjQFWNhLX-h3dCDu7KwUGf/view?usp=sharing)
---
## 목표
---
-  상황은 세종대 캠퍼스 내의 장애물을 한정한다.
-  보행자의 시야를 직선으로 제한한다.
-  각각의 장애물을 라벨링 툴을 활용하여 데이터셋을 만든다.
- 비올라-존스 디텍션을 활용하여 장애물을 검출한다.
- CNN을 사용하여 정확성을 높이기위해 검증한다.
- depth 거리에 따른 위험도를 classifier 한다.
---
## 기술

- Viola-Jones Detection
- CNN
  - Single Shot Multibox Detection
  - You Only Look Once V3
---

## 마인드맵

![image](https://user-images.githubusercontent.com/30471027/58703456-b9d3ef80-83e3-11e9-8983-fa7ba789665c.png)

---
## 사전 survery

> Core

- [COCO Dataset](http://cocodataset.org/)
- *[Toward Driving Scene Understanding: A Dataset for Learning Driver Behavior and Causal Reasoning, CVPR2018](http://openaccess.thecvf.com/content_cvpr_2018/papers/Ramanishka_Toward_Driving_Scene_CVPR_2018_paper.pdf)*

> 이 외는 회의록에서 열람 가능

---

## 가정
-	도로를 기준으로 할 것인지, 보행자를 기준으로 할 것인지 기준을 결정하였다.
-	장애물에 대한 분류 기준이 모호하므로 움직임의 유무와 객체의 종류에 따라서 분류하기로 하였다.
-	잘 안보이는 밤일시  추가적인 기술이 필요하므로 낮을 전제로 진행했다.
-	데이터셋을 공공데이터를 쓸지, 직접 찍어서 만들어서 사용할 것인지 아니면 섞어서 사용할지 결정하였다.
-	장애물을 실내로 할 것인지, 실외의 캠퍼스내로 할 것인지 결정하였다.

---


## 기존 진행 계획

1. 분류기 알고리즘 설계 : 위험도 분류 정도
  - 객체의 종류에 따른 분류

  물체의 종류를 분류하고 그 다음 위험도를 분류함
  - 관심 영역(ROI) 설정 & 영역 안에 들어온 물체

  관심영역을 설정 한 후 그 영역 안에 물체가 들어올 경우 위험도 판단
  
    A. 관심영역은 차선 개념에서 차용하여, 가상의 사다리꼴 모양의 영역을 설정함
    B. 검출된 영역 내에서 거리 정보를 얻어 거리에 따라 위험도 가중치를 부여함 
    C. 검출된 물체의 종류에따라 위험도 가중치를 달리 부여함
    
2. 데이터셋 제작
  A. 데이터 수집 및 촬영
  B. 전처리
  C. Ground Truth 제작

3. 모델 학습
  - 학습 이전에, MATLAB Toolbox를 이용하여 보도블럭의 경계선이 잘 검출되는지 사전 검토
  - SSD: Single Shot MultiBox Detector를 이용하여 학습 4 성능 평가(테스트)
  - 데이터셋 제작시 만들어 놨던 Test dataset 이용
  - COCOEval을 이용하여 모델 평가 5 결과 지표화
  - matplotlib을 이용하여 mAP 그래프 출력
  - 실제 세종대학교 데이터셋에 적용하여 시연

---

## 진행 경과

- 05/22 8분여 분량의 30FPS HD 교내 도보영상 촬영
- 05/23 14,000여개의 프레임으로 분할 후 각 팀원에게 할당
- 05/24 물체 분류 기준 설정
- 05/25~ VoTT 작업 환경 구축
- 05/27 annotation 작업
- ~05/28 Pre-trained COCO SSD dataset을 이용한 Activate Learning에 현재까지 작업된 annotation을 적용하기로 함
- 05/29 label crop 작업하여 class별로 추출 후 인계
- 05/30
  - Viola Jones에 문제점 발생, Darknet 도입 의논
  - 교수님과의 면담 -> 방향 재설정
---

## 한계

- 양질의 public dataset을 이용하지 않고 직접 제작을 시도했으나,
  - 촬영 장비가 스마트폰이여서 흔들림이 심하고
  - 촬영 장소인 교내가 차도와 인도의 구분이 뚜렷하지 않고
  - 분량이 턱없이 부족하여
  학습하기에 부적합하였음

- 장애물의 기준이 상이하여 팀원 간 일부 태그에 불일치가 발견됨

- 경계석(연석)을 기준으로 위험도를 분류하기 위해 검출을 시도했으나,
  - 경계석의 곡률이 커서 객체 검출 방법론으로 학습하기에 어려움이 있음

- 최신 버전의 도구를 이용하다 보니 메뉴얼이나 관련 이슈에 관한 솔루션 등이 적어 어려움을 겪음

- 팀원들의 역량만으로는 해결하기에 어려움이 큰 주제

- 이에 따라 교수님과의 면담 후 역할 분담과 계획을 재설정하기로 결정함

---

## 남은 목표

- DATASET에 대한 문제점을 KITTI 데이터셋을 이용하여 DEPTH, RGB데이터를 통한 장애물들을 인식할 수 있는지 시도

- 시간적인 여유를 고려하여 결과물을 보일 시 먼저 데모를 뽑아 확인

- Object Detection으로 SSD, YOLO를 동시 구현해보고 두 방법론의 성능 차이를 비교

- 위의 결과로 User Interface를 어떤 것을 서비스 할 수 있을지 연구

---

## 개발 일정

6/2  오후 9시 - 연구 방향성 각자의 결과를 ISSUE 에 리포트한다.

6/2 (일) - KITTI 데이터셋에 대한 각자의 이해 문서로 표현하여 돌려본다.

6/3 (월) - 각자의 역할에 대한 연구를 시작한다. (어려운 점은 바로바로 공유한다)

6/4 (화) - 중간점검  

---

## 중간 점검

![image](https://user-images.githubusercontent.com/11037567/58944007-dd1fe580-87bb-11e9-9b82-d5cf3eabc7e4.png)

## Demonstration_Plan

![1252352364364364](https://user-images.githubusercontent.com/11037567/58977034-cf8e4e00-8803-11e9-8ae9-2b54a442b625.png)

---

6/5 (수) - 역할 조정

---

## survey

- [SSD-tensorflow](https://github.com/balancap/SSD-Tensorflow)

- [KITTI Vision Benchmark Suite](http://www.cvlibs.net/datasets/kitti/)

- [mannequinchallenge](https://github.com/google/mannequinchallenge)



---

## Applied reference

> 준비중입니다.

---

## unused

~~[dataset](https://drive.google.com/open?id=1Kq4-xntWRRqfDeJDeFJQO7UrZr0ad7Gm)~~

~~[cropped_frame](https://drive.google.com/file/d/1QIeH_7zVEwnaaPsmO8BWLoxuz_kGcBMo/view?usp=sharing)~~

- _~~[VOTT(Labeling tool)](https://github.com/microsoft/VoTT)~~


---
