import uvicorn
from fastapi import FastAPI

app = FastAPI(title='University')


@app.get('/')
def root():
    return 'Hey'


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return user_id


fake_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
