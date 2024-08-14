from pydantic import BaseModel


class ProdutoBase(BaseModel):
    name: str
    image: str | None = None
    bar_code: int | None = None


class ProdutoCreate(ProdutoBase):
    pass


class Produto(ProdutoBase):
    id: int



class CompraBase(BaseModel):
    price: float
    qtd: int
    produto_id: int


class CompraCreate(CompraBase):
    pass


class Compra(CompraBase):
    id: int
