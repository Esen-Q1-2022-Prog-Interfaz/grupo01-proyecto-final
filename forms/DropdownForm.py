from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField
from models.catalogo import Catalogo

class Nic(FlaskForm):
    nic = SelectField('nic', choices=[(0.03, '0.03'), (0.06, '0.06')])
    sabor = SelectField('sabor', choices=[])

