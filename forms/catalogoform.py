from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError


class CatalogoForm(FlaskForm):
    sabor = StringField(
        validators=[InputRequired(), Length(max = 50)],
        render_kw={'placeholder':'Sabor'})

    descripcion = StringField(
        validators=[InputRequired(), Length(max = 50)],
        render_kw={'placeholder':'Descripción'})

    base = StringField(
        validators=[InputRequired(), Length(max = 50)],
        render_kw={'placeholder':'Base'})

    tamaño = IntegerField(
        validators=[InputRequired()],
        render_kw={'placeholder':'Tamaño'})

    nic = FloatField(
        validators=[InputRequired()],
        render_kw={'placeholder':'Tamaño'})
    
    stock = IntegerField(
        validators=[InputRequired()],
        render_kw={'placeholder':'Stock'})
