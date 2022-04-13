from unicodedata import name
from db.db import db

class Carrito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.String(50), nullable=False)
    nic = db.Column(db.Integer, nullable=True)
    quantity = db.Column(db.Integer, nullable=False)
    unitCost = db.Column(db.Integer, nullable=False)
    totalCost = db.Column(db.Integer, nullable=False)

    def __init__(self, flavor, nic, quantity, unitCost, totalCost) -> None:
        self.flavor = flavor
        self.nic = nic
        self.quantity = quantity
        self.unitCost = unitCost
        self.totalCost = unitCost * quantity

    def __repr__(self) -> str:
        return f"Order({self.id}, '{self.flavor}', '{self.nic}', '{self.quantity}', '{self.unitCost}', '{self.totalCost}')"