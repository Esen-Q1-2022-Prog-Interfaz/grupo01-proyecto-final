from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.catalogoform import CatalogoForm
from models.catalogo import Catalogo
from db.db import db


admin = Blueprint("admin", __name__, url_prefix='/admin')


@admin.route("/")
def home():
    return render_template("admin/dashboard.html")

@admin.route("/CRUD_Catalogo", methods=["GET", "POST"])
@login_required
def create():
    form = CatalogoForm()
    if form.validate_on_submit():
        comprador = form.comprador.data
        vendedor = form.vendedor.data
        impuesto = form.impuesto.data
        descuento = form.descuento.data
        newOrder = Order(comprador, vendedor, impuesto, descuento)
        db.session.add(newOrder)
        db.session.commit()
        return redirect(url_for("orders.home"))
    return render_template("orders/create.html", form=form)