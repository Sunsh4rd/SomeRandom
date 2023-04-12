import uvicorn
from fastapi import FastAPI

app = FastAPI(title='University')


@app.get('/')
def root(name: str):
    return f'Hey, {name}'


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
