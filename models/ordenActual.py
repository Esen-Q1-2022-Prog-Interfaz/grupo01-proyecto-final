from db.db import db

class ordenActual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sabor = db.Column(db.String(50), nullable=False)
    base = db.Column(db.String(50), nullable=False)
    tamaño = db.Column(db.Integer, nullable=False)
    nic = db.Column(db.Float, nullable=False)

    def __init__(self, sabor, base, tamaño, nic) -> None:
        self.sabor = sabor
        self.base = base
        self.tamaño = tamaño
        self.nic = nic

    def __repr__(self) -> str:
        return f"Order({self.id}, '{self.sabor}', {self.nic}, '{self.base}',{self.tamaño})" 