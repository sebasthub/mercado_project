from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.db_ops import crud, schemas
from app.db_ops.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/produto/", response_model=schemas.Produto, tags=["produto"])
def create_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return crud.create_produto(db=db, produto=produto)


@router.get("/produto/", response_model=list[schemas.Produto], tags=["produto"])
def read_produtos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    produtos = crud.get_produtos(db, skip=skip, limit=limit)
    return produtos


@router.get("/produto/{produto_id}", response_model=schemas.Produto, tags=["produto"])
def read_user(produto_id: int, db: Session = Depends(get_db)):
    db_produto = crud.get_produto(db, produto_id= produto_id)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_produto


@router.post("/compra/", response_model=schemas.Compra, tags=["Compra"])
def create_item_for_user(compra: schemas.CompraCreate, db: Session = Depends(get_db)):
    return crud.create_compra(db=db, compra=compra)


@router.get("/compra/", response_model=list[schemas.Compra], tags=["Compra"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_compras(db, skip=skip, limit=limit)
    return items
