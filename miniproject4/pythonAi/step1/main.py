from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def getRoot():
    return {'Greeting' : 'Hello FastAPI'}
