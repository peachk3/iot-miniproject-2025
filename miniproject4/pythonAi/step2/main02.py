# 이미지 탐지 웹서비스
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
import io
import base64
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import uvicorn

from ultralytics import YOLO
import cv2   # OpenCV

app = FastAPI()

model = YOLO('yolov8m.pt')  # YOLOv8 pretrained model(웹상에 존재, 최초에 다운로드)

# 웹상으로 전달할 BaseModel기반 클래스 생성
class DetectionResult(BaseModel):
    message: str        # 객체인식 결과 메시지
    image: str          # 인식결과 이미지

# 이미지 객체탐지 함수
def detectObjects(image: Image.Image):
    img = np.array(image)       # Pillow이미지 numpy배열로 변환
    results = model(img)        # 객체탐지, 물체 여러개
    class_name = model.names        # person, clock, car...    

    # 그리기 준비 Pillow
    # annotated = image.convert('RGB').copy()  # 원본을 복사
    # draw = ImageDraw.Draw(annotated)  # 복사본 이미지
    # font = ImageFont.load_default()

    for result in results:       # 여러개 물체들을 반복
        boxes = result.boxes.xyxy       
        confiences = result.boxes.conf  # 신뢰도 98.0%
        class_ids = result.boxes.cls    # 클래스 명

        for box, confience, class_id in zip(boxes, confiences, class_ids):
            x1, y1, x2, y2 = map(int, box)  # x1,y1(사각형 왼쪽 상단), x2,y2(사각형 오른쪽 하단)
            label = class_name[int(class_id)]    # 단일된 클래스 명

            # 각 인식된 객체에 사각형            
            # draw.rectangle([x1, y1, x2, y2], outline=(255,0,0), width=3)
            cv2.rectangle(img,(x1,y1), (x2,y2), (255,0,0), thickness=2)
            # HACK : 종류별로 색상 다르게, 라벨(클래스명)
            cv2.putText(img, f'{label} {confience:.2f}', (x1+7,y1+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
            
    result = Image.fromarray(img)                 # 결과를 다시 Pillow로 변환
    return result

@app.get('/')
async def index():
    image = Image.open('./test.jpg')  # 이미지 로드
    result = detectObjects(image)
    result.save('result.jpg')
     
    return { 'message': 'Hello FastAPI' } #, 'result': 'Image saved!' }

# ASP.NET에서 전달받은 이미지로 객체 인식, 인식결과를 다시 ASP.NET으로 전달
@app.post('/detect', response_model=DetectionResult)
async def detectService(message: str = Form(...), file: UploadFile = File(...)):
    # 이미지 읽어서 PIL 이미지로 변환
    image = Image.open(io.BytesIO(await file.read()))  # 웹으로 전달된 이미지 객체 로드

    # RGB 변환
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # 객체탐지 수행
    result = detectObjects(image)

    # 이미지 결과를 base64 인코딩(웹상으로 전달)
    buffered = io.BytesIO()
    result.save(buffered, format='JPEG')

    # JSON으로 이미지 전달하려면 base64로 인코딩된 문자열로 전달
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return DetectionResult(message=message, image=img_str)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)