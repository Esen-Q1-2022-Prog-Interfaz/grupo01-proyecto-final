from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from forms.registerForm import RegisterForm
from forms.loginForm import LoginForm
from forms.contactForm import messageForm
from db.bcryptService import bcrypt
from models.contact import Message
from models.ordenActual import ordenActual
from models.user import User
from db.db import db
from models.ordenPendiente import ordenPendiente
from routes.admin import admin
from models.ordenActual import ordenActual
from models.order import Order

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():
    return render_template("home.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        global current_user
        currentUser = User.query.filter_by(username=username).first()
        if currentUser:
            if bcrypt.check_password_hash(currentUser.password, password):
                login_user(currentUser)
                if currentUser.rank == 'admin':
                    return redirect(url_for("admin.home"))
                else:
                    return redirect(url_for("auth.home"))
    return render_template("login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password)
        newUser = User(username, hashed_password, "active", "user")
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.home"))


@auth.route("/dashboard")
@login_required
def dashboard():
    print(f"current_user: {current_user}")
    return render_template("dashboard.html", user=current_user)

@auth.route("/catalogo")
@login_required
def catalogo():
    return render_template("page/catalogo.html")

@auth.route("/contact", methods=["GET", "POST"])
def contact():
    form = messageForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        date = form.date.data
        newMessage = Message(name, email, subject, message, date)
        db.session.add(newMessage)
        db.session.commit()
        return redirect(url_for("auth.home"))
    return render_template("page/contact.html", form=form)

@auth.route("/cart", methods=["GET", "POST"])
@login_required
def cart():
    Orden = ordenActual.query.all()
    precio = 0
    for item in Orden:
        if item.base == "Free":
            precio += 25
        elif item.base == "Salt Nic":
            precio += 15

    return render_template("page/carrito.html", ordenes=Orden, precio=precio)

@auth.route("/deleteCartItem/<int:Id>")
@login_required
def deleteCartItem(Id):
    currentCartItem = ordenActual.query.filter_by(id=Id).first()
    db.session.delete(currentCartItem)
    db.session.commit()
    return redirect(url_for("auth.cart"))

@admin.route("/EnviarOrden")
@login_required
def enviar():
    keys = db.inspect(ordenActual).columns.keys()
    llaves = len(keys)
    llaves -= 2
    info = Order.query.order_by(Order.id).first()
    for key in range(llaves):
        prod = ordenActual.query.order_by(ordenActual.id).first()
        todo = ordenPendiente(info.nombre, info.direccion, info.pago, prod.sabor, prod.base, prod.tamaño, prod.nic)
        db.session.add(todo)
        db.session.delete(prod)
        db.session.commit()
        
    db.session.delete(info)
    db.session.commit()
    return  redirect(url_for("auth.home"))