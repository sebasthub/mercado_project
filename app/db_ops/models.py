from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Double
from sqlalchemy.orm import relationship

from .database import Base


class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String, nullable=True)
    bar_code = Column(Integer, nullable=True)

    compras = relationship("Compra", back_populates="produto")


class Compra(Base):
    __tablename__ = "compra"

    id = Column(Integer, primary_key=True)
    price = Column(Double, nullable=False)
    qtd = Column(Integer, nullable=False)
    produto_id = Column(Integer, ForeignKey("produto.id"))

    produto = relationship("Produto", back_populates="compras")