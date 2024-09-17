from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db_ops import models
from app.db_ops.database import engine
from .routers import produto_compras

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sebasthub.github.io"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"msg": "Hello World"}

@app.get("/hello")
async def root():
    return {"msg": "Hello James"}

app.include_router(produto_compras.router)
