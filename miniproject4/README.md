# 미니 프로젝트 4

## 파이썬 AI(API동작) + ASP.NET Core 연동 프로젝트

### python 기본

#### 파이썬 웹애플리케이션
1. dJango : 대규모 웹앱 개발시 사용 프레임워크. 구조화 잘되어 있음. 무겁다
2. flask : 소규모 웹앱 개발시 사용. 가볍다. 필요 개발을 개발자가 모두 구현
3. `uvicorn` : 진짜 소규모 웹앱 개발 사용. FastAPI랑 연동. 무지 가볍다

#### FastAPI
- RESTful API를 손쉽게 만들어주는 웹 프레임워크
- uvicorn 웹앱 프레임워크와 같이 사용

#### 기본 패키지 설치

```shell
> pip install fastapi uvicorn
```

[소스](./pythonAi/step1/main.py)

#### 데이터 유효성검사 패키지 pydantic

[소스](./pythonAi/step1/main02.py)

#### 전체 통합

[소스](./pythonAi/step1/main03.py)

### ASP.NET Core 기본
- 파이썬에서 만들어져서 uvicorn으로 전달되는 데이터를 수신받아서 표현하는 웹앱
- `ASP.NET Core 비어있음`으로 생성. MVC로 생성 시 필요없는 파일이 다수 생성
- HTTPS를 선택 해제

[소스](./backend/ASPWebSolution/TestWebApp/Program.cs)

#### 파이썬 웹서버 송신 데이터 처리
- html에서 javascript로 처리
- ASP.NET Core API 경유 처리

### 파이썬 AI Server 구현

#### 필요 라이브러리
- fastapi
- uvicorn
- pydantic
- Pillow : 이미지 열기, 저장 라이브러리
- numpy : 수치 연산
- requests : HTTP로 요청
- opencv-python : 이미지, 비디오 처리
- python-multipart : 멀티파트(이미지, 비디오) 파싱

```shell
> pip install Pillow numpy requests opencv-python python-multipart
```

- ultralytics : YOLO 이미지, 동영상 객체탐지. 
    - ultralytics 를 먼저 설치하면 Pytorch CPU버전이 설치

- Pytorch GPU 사용버전 설치(2.9GB)

```shell
> pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
```

<img src="../image/mp0021.png" width="600">

#### AI Server

- 웹서버 실행

[소스](./pythonAi/step2/main01.py)