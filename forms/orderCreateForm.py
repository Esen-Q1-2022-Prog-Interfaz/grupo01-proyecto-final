from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from models.user import User


class OrderCreateForm(FlaskForm):
    comprador = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "comprador"},
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
        render_kw={"placeholder": "metodo de pago"},
    )



    submit = SubmitField("create")