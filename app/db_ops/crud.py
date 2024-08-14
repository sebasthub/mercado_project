from sqlalchemy.orm import Session

from app.db_ops import models, schemas


def get_produto(db: Session, produto_id: int):
    return db.query(models.Produto).filter(models.Produto.id == produto_id).first()


def get_produto_by_bar_code(db: Session, code: int):
    return db.query(models.Produto).filter(models.Produto.bar_code == code).first()


def get_produtos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Produto).offset(skip).limit(limit).all()


def create_produto(db: Session, produto: schemas.ProdutoCreate):
    db_produto = models.Produto(name=produto.name, bar_code=produto.bar_code, image=produto.image)
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto


def get_compras(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Compra).offset(skip).limit(limit).all()


def create_compra(db: Session, compra: schemas.CompraCreate):
    db_compra = models.Compra(**compra.model_dump())
    db.add(db_compra)
    db.commit()
    db.refresh(db_compra)
    return db_compra