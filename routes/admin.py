from turtle import update
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.catalogoForm import CatalogoForm
from forms.catalogoFormUpdate import CatalogoFormUpdate
from forms.contactForm import messageForm
from models.ordenPendiente import ordenPendiente
from models.catalogo import Catalogo
from models.contact import Message
from models.ordenActual import ordenActual
from db.db import db
from models.order import Order
from models.reporte import Reporte
from datetime import date


admin = Blueprint("admin", __name__, url_prefix='/admin')

#Home del dashboard
@admin.route("/")
def home():
    return render_template("admin/dashboard.html")


#Añadir nuevos productos al catalogo
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

#Borrar productos del catalogo
@admin.route("/delete/<int:Id>")
@login_required
def delete(Id):
    currentProduct = Catalogo.query.filter_by(id=Id).first()
    db.session.delete(currentProduct)
    db.session.commit()
    return redirect(url_for("admin.create"))

#Update productos del catalogo
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
    return render_template("admin/update.html", Id=Id ,form=form, item=currentProduct)

#Ver mensajes
@admin.route("/contact", methods=["GET", "POST"])
@login_required
def mensajes():
    Mensaje = Message.query.all()
    return render_template("admin/contacto.html", mensajes=Mensaje)

#Borrar mensajes
@admin.route("/leido/<int:Id>")
@login_required
def deleteMessage(Id):
    currentMessage = Message.query.filter_by(id=Id).first()
    db.session.delete(currentMessage)
    db.session.commit()
    return redirect(url_for("admin.mensajes"))

#Ver pedidos por entregar/completar
@admin.route("/pedidos", methods=["GET", "POST"])
@login_required
def pedidos():
    ordenes = ordenPendiente.query.all()
    return render_template("admin/pedidos.html", ordenes=ordenes)

#Finalizar orden/reservar orden
@admin.route("/EnviarOrden")
@login_required
def enviar():
    import sqlalchemy as dbe

    # engine = dbe.create_engine("mysql://b1dfe25bebd0d5:babacb3a@us-cdbr-east-05.cleardb.net/heroku_653f8e9ae84c59d")
    engine = dbe.create_engine("mysql://root:root@127.0.0.1:3306/american")
    meta_data = dbe.MetaData(bind=engine)
    dbe.MetaData.reflect(meta_data)
    actor_table = meta_data.tables['orden_actual']
    result = dbe.select([dbe.func.count()]).select_from(actor_table).scalar()
    info = Order.query.order_by(Order.id).first()

    for row in range(result):
        prod = ordenActual.query.order_by(ordenActual.id).first()
        todo = ordenPendiente(info.nombre, info.direccion, info.pago, prod.sabor, prod.base, prod.tamaño, prod.nic)
        db.session.add(todo)
        db.session.delete(prod)
        db.session.commit()
        
    db.session.delete(info)
    db.session.commit()
    return  redirect(url_for("auth.home"))


#Marcar orden/pedido como finalizado
@admin.route("/finalizar/<int:Id>")
@login_required
def finalizar(Id):
    ahora = date.today()
    product = ordenPendiente.query.filter_by(id=Id).first()
    rep = Reporte(product.direccion, product.nombre, product.pago, product.sabor, product.base, product.tamaño, product.nic, ahora)
    db.session.add(rep)
    db.session.delete(product)
    db.session.commit()
    ordenes = ordenPendiente.query.all()
    return render_template("admin/pedidos.html", ordenes=ordenes)

#Ver historial de compras/reporte
@admin.route("/reporte")
@login_required
def reporte():
    ordenes = Reporte.query.all()
    return render_template("admin/reporte.html", ordenes=ordenes)
