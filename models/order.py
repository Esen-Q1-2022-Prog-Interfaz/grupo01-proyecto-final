from db.db import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), nullable=True)
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    pago = db.Column(db.String(50), nullable=False)

    def __init__(self, usuario, direccion,nombre, pago) -> None:
        self.usuario = usuario
        self.direccion = direccion
        self.pago = pago
        self.nombre = nombre

    def __repr__(self) -> str:
        return f"Order({self.id}, {self.usuario}, '{self.direccion}','{self.pago}', '{self.nombre}')"