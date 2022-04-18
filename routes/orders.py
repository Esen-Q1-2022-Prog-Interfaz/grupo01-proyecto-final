from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.orderCreateForm import OrderCreateForm
from db.db import db
from models.order import Order
from datetime import date
from models.catalogo import Catalogo
from models.ordenActual import ordenActual
from forms.OrderResumme import OrderRessume
from models.ordenPendiente import ordenPendiente
from routes.auth import auth

orders = Blueprint("orders", __name__, url_prefix="/orders")

@orders.route("/createOrder")
@login_required
def CreateOrder():
    return render_template("orders/create.html")

@orders.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = OrderCreateForm()
    if form.validate_on_submit():
        usuario = current_user
        nombre = form.nombre.data
        direccion = form.direccion.data
        pago = form.pago.data
        newOrder = Order(usuario, nombre, direccion, pago)
        db.session.add(newOrder)
        db.session.commit()
        return redirect(url_for("admin.enviar"))
    return render_template("orders/create.html", form=form)


@orders.route("/OrderDetails", methods=["GET", "POST"])
@login_required
def OrderDetails():
    productList = Catalogo.query.all()
    TodasOrdenes = ordenActual.query.all()
    form = OrderRessume()
    return render_template("orders/orderDetails.html", form=form, items=productList, ordenes=TodasOrdenes)

@orders.route("/add/<int:Id>")
@login_required
def add(Id):
    currentProduct = Catalogo.query.filter_by(id=Id).first()
    form = OrderRessume()
    sabor = currentProduct.sabor
    base = currentProduct.base
    tamano = currentProduct.tamaño
    nic = currentProduct.nic
    producto = ordenActual(sabor,base,tamano,nic)
    db.session.add(producto)
    db.session.commit()
    return redirect(url_for("orders.OrderDetails", id=id))


@orders.route("/delete/<int:Id>")
@login_required
def delete(Id):
    currentProduct = ordenActual.query.filter_by(id=Id).first()
    db.session.delete(currentProduct)
    db.session.commit()
    return redirect(url_for("orders.OrderDetails", id=id))

