from fastapi import FastAPI
import uvicorn

import secret

app = FastAPI()

@app.get('/')
async def root():
    return {"Hello": "Это моё первое прложение на FastAPI!"}

if __name__ == '__main__':
    uvicorn.run(app, host=secret.HOST, port=secret.PORT)








