# 통합
from fastapi import FastAPI, HTTPException   # HTTPException, 웹상의 발생하는 예외처리 클래스
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):          # 클라이언트로 전송할 데이터 형식클래스
    name: str
    desc: str = None
    price: float
    tax: float = None

# 가상 DB
items = {}    # 정보를 담을 딕셔너리 <==> json

# 기본 URL 확인 메시지
@app.get('/')
async def getRoot():
    return { 'Greeting' : 'Hello FastAPI' }

# post에서 저장한 데이터를 확인 함수
@app.get('/items/{id}')
async def getItem(id: int):
    if id not in items:   # 없는 데이터는 404 오류 발생
        raise HTTPException(status_code=404, detail='Item not found')
    
    return items[id]

# 데이터 생성
@app.post('/items')
async def setItem(item: Item):
    id = len(items) + 1   # 0부터 시작하니까 +1 더해서 id 생성
    items[id] = item
    
    # ** 딕셔너리를 키=값 쌍 형태로 풀어서 함수전달 또는 새로운 딕셔너리 만들때 사용
    # *args 위치 인자를 튜플로 받음
    # **kwargs 키워드 인자를 딕셔너리로 받음
    return { 'id': id, **item.model_dump() }