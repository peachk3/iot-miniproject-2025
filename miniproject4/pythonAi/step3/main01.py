# 동영상 탐지 서비스
import base64
import numpy as np
from ultralytics import YOLO
import cv2
import json
import paho.mqtt.client as mqtt    ## pip install paho-mqtt

model = YOLO('yolov8n.pt')   ## 모델 생성및 사전훈련모델 다운로드

broker = 'localhost'
# port는 웹소켓용 포트로 변경할 것
port = 9001 # 1883
topic = '/aiserver/objectdetects'

# MQTT 클라이언트
client = mqtt.Client(
            client_id='RealTimeClient',
            transport='websockets',
            protocol=mqtt.MQTTv5,
            userdata=None,
            callback_api_version=mqtt.CallbackAPIVersion.VERSION2
         )

def onConnect(client, userdata, flags, reason_code, properties=None):
    print(f'[MQTT] 연결됨. reason={reason_code}')

def onMessage(client, userdata, msg):
    print(msg.topic, msg.payload.decode())

client.on_connect = onConnect
client.on_message = onMessage
client.connect(host=broker, port=port, keepalive=60)
client.loop_start()

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
api = cv2.CAP_DSHOW

# 비디오캡쳐 시작 0:웹캠 or 동영상경로
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

while cap.isOpened():
    # t0 = time.perf_counter()

    ret, frame = cap.read()

    if not ret: break   # 동영상이 열리지 않으면 종료

    result_image = detectObjects(frame)  # 한 프레임씩 객체 탐지

    # 이미지결과 base64 인코딩
    _, buffer = cv2.imencode('.jpg', result_image)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')

    # 객체탐지 이미지 MQTT Websocket으로 전송
    payload = json.dumps({'image': jpg_as_text})
    client.publish(topic, payload)

    # 혹시 카메라가 16:9를 지원하지 않아 다른 비율이 들어오면 리사이즈로 맞춰서 표시
    # frame_disp = cv2.resize(result_image, (w, h), interpolation=cv2.INTER_AREA)
    # 프레임을 화면에 표시
    cv2.imshow('Frame', np.array(result_image))

    if cv2.waitKey(1) & 0xFF == ord('q'): break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
client.disconnect()