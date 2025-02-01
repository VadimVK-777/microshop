from fastapi import FastAPI
import uvicorn
from pydantic import EmailStr, BaseModel
from items_views import router as items_router
from users.views import router as users_router

print("Hello World")
app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)
# You're going to force push to new. It may overwrite commits at the remote. Are you sure you want to proceed?

@app.get("/")
def hello_index():
    return {"message": "Hello World"}


@app.get("/hello/")
def hello(name: str = "world"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


@app.post("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
