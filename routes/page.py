from flask import Blueprint, render_template, redirect, url_for



page = Blueprint("page", __name__)


@page.route("/")
def home():
    return "page"