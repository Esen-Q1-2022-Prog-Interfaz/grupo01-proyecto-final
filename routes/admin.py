from flask import Blueprint, render_template, redirect, url_for
from db.db import db


admin = Blueprint("page", __name__)


@admin.route("/")
def home():
    return render_template("admin/dashboard.html")