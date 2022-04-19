from db.db import db
from datetime import date
ahora = date.today()

class Reporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    pago = db.Column(db.String(50), nullable=False)
    sabor = db.Column(db.String(50), nullable=False)
    base = db.Column(db.String(50), nullable=False)
    tamaño = db.Column(db.Integer, nullable=False)
    nic = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.String(50), nullable=False)

    def __init__(self, direccion, nombre, pago, sabor, base, tamaño, nic, fecha) -> None:
        
        self.direccion = direccion
        self.nombre = nombre
        self.pago = pago
        self.sabor = sabor
        self.base = base
        self.tamaño = tamaño
        self.nic = nic
        self.fecha = ahora

    def __repr__(self) -> str:
        return f"Order({self.id}, '{self.sabor}', {self.nic}, '{self.base}', {self.tamaño}, {self.nombre}, '{self.direccion}',{self.pago}, '{self.fecha}')" 