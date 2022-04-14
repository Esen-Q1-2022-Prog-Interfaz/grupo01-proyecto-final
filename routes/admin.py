from turtle import update
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.catalogoform import CatalogoForm
from forms.catalogoFormUpdate import CatalogoFormUpdate

from models.catalogo import Catalogo
from db.db import db


admin = Blueprint("admin", __name__, url_prefix='/admin')


@admin.route("/")
def home():
    return render_template("admin/dashboard.html")

@admin.route("/create", methods=["GET", "POST"])
@login_required
def create():
    productList = Catalogo.query.all()
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
    return render_template("admin/catalogo.html", form=form, items=productList)

@admin.route("/delete/<int:Id>")
@login_required
def delete(Id):
    currentProduct = Catalogo.query.filter_by(id=Id).first()
    db.session.delete(currentProduct)
    db.session.commit()
    return redirect(url_for("admin.create"))


@admin.route("/update/<int:Id>", methods=['GET', 'POST'])
@login_required
def update(Id):
    currentProduct = Catalogo.query.filter_by(id=Id).first()
    producto = currentProduct.id
    form = CatalogoFormUpdate()
    if form.validate_on_submit():
        currentProduct.stock = form.stock.data
        db.session.add(currentProduct)
        db.session.commit()
        return redirect(url_for("admin.create"))
    return render_template("admin/update.html", Id=Id,form=form, item=currentProduct)