from flask import Blueprint, render_template, redirect, url_for
from db.db import db


admin = Blueprint("admin", __name__, url_prefix='/admin')


@admin.route("/")
def home():
    return render_template("admin/dashboard.html")