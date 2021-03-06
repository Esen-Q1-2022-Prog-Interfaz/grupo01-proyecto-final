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



auth = Blueprint("auth", __name__)

#Home de la página
@auth.route("/")
def home():
    return render_template("home.html")

#Login como usuario existente
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

# Register usuario nuevo
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

#Log out usuario actual
@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.home"))


#Renderiza el catalogo
@auth.route("/catalogo")
@login_required
def catalogo():
    return render_template("page/catalogo.html")


#Contact - Manda mensaje 
@auth.route("/contact", methods=["GET", "POST"])
def contact():
    from datetime import date
    today = date.today()
    form = messageForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        newMessage = Message(name, email, subject, message, today)
        db.session.add(newMessage)
        db.session.commit()
        return redirect(url_for("auth.home"))
    return render_template("page/contact.html", form=form)

#Carrito de compras

#Muestra Carrito 
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

#Elimina producto del carrito
@auth.route("/deleteCartItem/<int:Id>")
@login_required
def deleteCartItem(Id):
    currentCartItem = ordenActual.query.filter_by(id=Id).first()
    db.session.delete(currentCartItem)
    db.session.commit()
    return redirect(url_for("auth.cart"))