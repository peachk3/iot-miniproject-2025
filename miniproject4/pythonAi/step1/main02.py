from fastapi import FastAPI         # FastAPI 웹프레임워크
from pydantic import BaseModel      # 데이터검증, 직렬화(웹을 통해서 데이터 전달기술)를 위한 패키지

app = FastAPI()

class Item(BaseModel):          # 클라이언트로 전송할 데이터 형식클래스
    name: str
    desc: str = None
    price: float
    tax: float = None

@app.get('/items/')
async def get_item(item: Item):    # POSTMan 또는 다른 API 테스트 툴로 테스트
    return item