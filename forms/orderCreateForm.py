from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from models.user import User


class OrderCreateForm(FlaskForm):
    
    nombre = StringField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "Nombre"},
    )

    direccion = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "Dirección de entrega"},
    )

    pago = StringField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "Método de pago"},
    )



    submit = SubmitField("Create")