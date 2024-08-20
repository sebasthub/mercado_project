from fastapi import FastAPI

from app.db_ops import models
from app.db_ops.database import engine
from .routers import produto_compras

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "Hello World"}

@app.get("/s2")
async def root():
    return {"msg": "corazon"}

app.include_router(produto_compras.router)
