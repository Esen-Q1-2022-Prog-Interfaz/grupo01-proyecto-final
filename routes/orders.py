from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.orderCreateForm import OrderCreateForm
from db.db import db
from models.order import Order
from datetime import date
from forms.DropdownForm import Nic
from models.catalogo import Catalogo

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
        nombre = form.nombre.data
        direccion = form.direccion.data
        pago = form.pago.data
        newOrder = Order(nombre, direccion, pago)
        db.session.add(newOrder)
        db.session.commit()
        return redirect(url_for("orders.CreateOrder"))
    return render_template("orders/create.html", form=form)

@orders.route("/OrderDetails", methods["GET", "POST"])
@login_required
def OrderDetails():
    form = Nic()
    form.sabor.choices = [(Catalogo.id, Catalogo.sabor) for sabor in Catalogo.query.filter_by(nic = '0.03').all()]
    return render_template('orders/orderDetails.html', form=form)