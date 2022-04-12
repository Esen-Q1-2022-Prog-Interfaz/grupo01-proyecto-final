from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.catalogoForm import CatalogoForm

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
        sabor = form.sabor.data
        descripcion = form.descripcion.data
        base = form.base.data
        tamaño = form.tamaño.data
        nic = form.nic.data
        stock = form.stock.data
        newProduct = Catalogo(sabor, descripcion, base, tamaño, nic, stock)
        db.session.add(newProduct)
        db.session.commit()
        return redirect(url_for("admin.create"))
    return render_template("admin/catalogo.html", form=form)