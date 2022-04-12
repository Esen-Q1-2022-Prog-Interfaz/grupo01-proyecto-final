from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError
from models.catalogo import Catalogo

class OrderRessume(FlaskForm):
    submit = SubmitField("Añadir")