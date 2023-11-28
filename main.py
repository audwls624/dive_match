import uvicorn
from dataclasses import asdict
from typing import Union
from fastapi import FastAPI
from common.config import get_conf
from fastapi import Depends
from database.connections import db
from sqlalchemy.orm import Session


env_conf = asdict(get_conf())
app = FastAPI()
db.init_app(app, **env_conf)


@app.get("/")
def read_root():
    return "Welcome to Dive Match!"


@app.get("/items/{item_id}")
def read_items(
    item_id: int, db: Session = Depends(db.session), q: Union[str, None] = None
):
    # 여기에서 데이터베이스 세션 'db'를 사용하여 작업 수행
    print(db)
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
