import uvicorn
from typing import Union
from fastapi import FastAPI
from common.config import DB_CONFIG, IS_PRODUCTION
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()
register_tortoise(
    app=app,
    config=DB_CONFIG,
    generate_schemas=False if IS_PRODUCTION else True,
    add_exception_handlers=True if IS_PRODUCTION else False,
)


@app.get("/")
def read_root():
    return "Welcome to Dive Match!"


@app.get("/items/{item_id}")
def read_items(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
