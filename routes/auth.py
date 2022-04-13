from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from forms.registerForm import RegisterForm
from forms.loginForm import LoginForm
from forms.contactForm import messageForm
from db.bcryptService import bcrypt
from models.contact import Message
from models.user import User
from db.db import db
from routes.admin import admin

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
        newMessage = Message(name, email, subject, message)
        db.session.add(newMessage)
        db.session.commit()
        return redirect(url_for("auth.home"))
    return render_template("page/contact.html", form=form)

@auth.route("/cart", methods=["GET", "POST"])
def cart():
    return render_template("page/carrito.html")