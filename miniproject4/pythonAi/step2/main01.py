# step1의 웹서버 반복
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def getRoot():
    return { 'greeting': 'Hello FastAPI!' }

if __name__ == '__main__':   # 메인 엔트리포인트 지정
    uvicorn.run(app, host='127.0.0.1', port=8000)