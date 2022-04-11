from db.db import db
from datetime import date 


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comprador = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    pago = db.Column(db.String(50), nullable=True)

    def __init__(self, comprador, direccion, pago, impuesto, totalSale=0, fecha=None) -> None:
        self.comprador = comprador
        self.direccion = direccion
        self.pago = pago


    def __repr__(self) -> str:
        return f"Order({self.id}, {self.comprador}, '{self.direccion}','{self.pago}')"