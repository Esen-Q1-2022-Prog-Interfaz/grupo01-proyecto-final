from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.orderCreateForm import OrderCreateForm
from db.db import db
from models.order import Order
from datetime import date

orders = Blueprint("orders", __name__, url_prefix="/orders")

@orders.route("/create")
@login_required
def CreateOrder():
    return render_template("orders/create.html")