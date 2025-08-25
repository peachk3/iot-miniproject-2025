# 동영상 탐지 서비스
import numpy as np
from ultralytics import YOLO
import cv2
import time

model = YOLO('yolov8n.pt')   ## 모델 생성및 사전훈련모델 다운로드

# 클래스라벨별 색상 설정 함수 
def getColors(num_colors):
    np.random.seed(42)
    colors = [tuple(np.random.randint(0,255,3).tolist()) for _ in range(num_colors)]

    return colors

# 색상표  - detectObjects() 소스 안에 넣어도?
class_names = model.names
num_classes = len(class_names)  
colors = getColors(num_classes)

## 물체 인식
def detectObjects(image: np.array):
    results = model(image, verbose=False)   # 각 프레임별 물체탐지
    class_names = model.names        # 탐지 클래스명

    for result in results:
        boxes = result.boxes.xyxy
        confidences = result.boxes.conf
        class_ids = result.boxes.cls

        for box, confidence, class_id in zip(boxes, confidences, class_ids):
            x1, y1, x2, y2 = map(int, box)  # 좌표를 정수로
            label = class_names[int(class_id)]
            cv2.rectangle(image, (x1,y1), (x2,y2), colors[int(class_id)], 2)
            cv2.putText(image, f'{label} - {confidence:.2f}', (x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 0.8, colors[int(class_id)], 2)

    return image

w, h = 640, 360
# api = cv2.CAP_DSHOW

# 비디오캡쳐 시작 0:웹캠 or 동영상경로
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('./data/vietnam_traffic.mp4')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

# 소스 FPS 읽기 (코덱에 따라 0이 나올 수도 있어서 보정)
src_fps = cap.get(cv2.CAP_PROP_FPS)
if not src_fps or src_fps <= 1:
    src_fps = 30.0  # 합리적 
   
frame_time_ms = 1000.0 / src_fps  # 한 프레임에 할당할 시간(ms)

while cap.isOpened():
    t0 = time.perf_counter()

    ret, frame = cap.read()

    if not ret: break   # 동영상이 열리지 않으면 종료

    result_image = detectObjects(frame)  # 한 프레임씩 객체 탐지

    # 프레임을 화면에 표시
    cv2.imshow('Frame', np.array(result_image))

    # 이번 프레임 처리에 걸린 시간(ms)
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    remain_ms = max(1, int(frame_time_ms - elapsed_ms))  # 남은 시간만큼 기다리기

    key = cv2.waitKey(remain_ms) & 0xFF
    if key == ord('q'):
        break
    elif key == ord(' '):  # 스페이스로 일시정지/재개
        while True:
            k2 = cv2.waitKey(50) & 0xFF
            if k2 in (ord(' '), ord('q')):
                if k2 == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    raise SystemExit
                break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()