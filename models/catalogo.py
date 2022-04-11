from db.db import db

class catalogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sabor = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(50), nullable=False)
    base = db.Column(db.String(50), nullable=False)
    tamaño = db.Column(db.Integer, nullable=False)
    nic = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __init__(self, sabor, descripcion, base, tamaño, nic, stock) -> None:
        self.sabor = sabor
        self.descripcion = descripcion
        self.base = base
        self.tamaño = tamaño
        self.nic = nic
        self.stock = stock

    def __repr__(self) -> str:
        return f"Order({self.id}, {self.sabor}, '{self.descripcion}', '{self.nic}', '{self.base}', '{self.stock}', '{self.tamaño}')"
