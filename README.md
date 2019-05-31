# SituationClassifier

## Situation classification using obstacle detection
> 장애물 검출을 통한 상황 분류

### Team
| 이름 | 학과 | 학번 | 구성 | 역할 |
|:---:|:---:|:---:|:---:|:---:|
| **위성민** | 무인이동체공학전공 | 17011877 | **팀장** | 도로 검출 |
| 최용호 | 스마트기기공학전공 | 17013253 | 팀원 | 
| 권영서 | 무인이동체공학전공 | 17011794 | 팀원 |
| 김남훈 | 스마트기기공학전공 | 17011832 | 팀원 |
| 강산희 | 무인이동체공학전공 | 17011855 | 팀원 |

---

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

- [COCO Dataset](http://cocodataset.org/)
- *[Toward Driving Scene Understanding: A Dataset for Learning Driver Behavior and Causal Reasoning, CVPR2018](http://openaccess.thecvf.com/content_cvpr_2018/papers/Ramanishka_Toward_Driving_Scene_CVPR_2018_paper.pdf)*


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

---

## 한계

- 

---


























---

###### unused

~~[dataset](https://drive.google.com/open?id=1Kq4-xntWRRqfDeJDeFJQO7UrZr0ad7Gm)~~

~~[cropped_frame](https://drive.google.com/file/d/1QIeH_7zVEwnaaPsmO8BWLoxuz_kGcBMo/view?usp=sharing)~~

- _~~VOTT(Labeling tool)~~


---
