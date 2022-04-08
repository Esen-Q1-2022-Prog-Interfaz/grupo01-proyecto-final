from flask import Blueprint, render_template, redirect, url_for



page = Blueprint("page", __name__, url_prefix="/page")


@page.route("/")
def home():
    return render_template("page/index.html")