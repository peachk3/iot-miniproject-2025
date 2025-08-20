from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def getRoot():
    return { 'Greeting' : 'Hello FastAPI' }

@app.get('/items/{id}') # RESTful API POST(C), GET(R), PUT(U), DELETE(D)
async def getItem(id: int, desc: str = None):
    return { 'ID': id, 'DESC': desc }