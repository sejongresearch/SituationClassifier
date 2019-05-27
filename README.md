# SituationClassifier

## Situation classification using obstacle detection
> 장애물 검출을 통한 상황 분류

### 팀원 구성
| 이름 | 학과 | 학번 | 비고 |
|:---:|:---:|:---:|:---:|
| **위성민** | 무인이동체공학전공 | 17011877 | **팀장** | 
| 최용호 | 스마트기기공학전공 | 17013253 | 팀원 |
| 권영서 | 무인이동체공학전공 | 17011794 | 팀원 |
| 김남훈 | 스마트기기공학전공 | 17011832 | 팀원 |
| 강산희 | 무인이동체공학전공 | 17011855 | 팀원 |


---

[dataset](https://drive.google.com/open?id=1Kq4-xntWRRqfDeJDeFJQO7UrZr0ad7Gm)

---

### Anootation Tool Setting

[VoTT(Visual Object Tagging Tool)](https://github.com/microsoft/VoTT)를 이용하여 Ground Truth를 제작합니다.

1. releases 탭에서 최신 버전(작성일 기준 v2.1.0) exe를 [다운로드](https://github.com/microsoft/VoTT/releases/download/v2.1.0/vott-2.1.0-win32.exe)합니다.

2. 다운받은 파일을 실행하면

![image](https://user-images.githubusercontent.com/30471027/58376468-f00a0d00-7fa6-11e9-9886-cbf6644b327d.png)

다음과 같은 경고창이 뜨는데, `추가 정보`를 눌러 

![image](https://user-images.githubusercontent.com/30471027/58376473-0e700880-7fa7-11e9-8fcb-0a4aa6678e05.png)

실행해줍니다.

3. 설치가 완료되면

![image](https://user-images.githubusercontent.com/30471027/58376487-5858ee80-7fa7-11e9-838c-760709e41304.png)

다음과 같은 창이 뜹니다.

4. [VoTT 프로젝트 파일](https://github.com/sejongbhaj/SituationClassifier/tree/master/VoTT)을 다운로드합니다.

5. 좌측 하단의 아이콘을 눌러 Application Settings를 엽니다.

6. Add Security Tokens를 누릅니다.

![image](https://user-images.githubusercontent.com/30471027/58376695-fef2be80-7faa-11e9-8267-99912a532d3b.png)

7. Name과 Key 칸에 다운받았던 txt파일에 들어있는 값들을 복사해주고 저장합니다.

![image](https://user-images.githubusercontent.com/30471027/58376700-10d46180-7fab-11e9-9c97-2424bbcdfa86.png)
~~~
8. `VoTT/src` 폴더에 들어가 `video2jpg.exe`를 실행합니다.

![image](https://user-images.githubusercontent.com/30471027/58391751-1ba5f980-8072-11e9-9bbf-52dfc0d1e95e.png)
~~~

9. 메인에서 `Open Local Project`를 눌러 `~/Test` 폴더에 있는 `TestProject.vott` 파일을 로드합니다.

10. 좌측 상단에서 플러그 모양 아이콘을 눌러 `Connection Settings` 메뉴로 들어갑니다.

11. src는 비디오 프레임이 있는 경로를, dst는 `~/Test` 경로로 설정해주고 저장합니다.
