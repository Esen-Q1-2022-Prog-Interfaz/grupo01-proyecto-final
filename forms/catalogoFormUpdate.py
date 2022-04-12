from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError


class CatalogoFormUpdate(FlaskForm):
    stock = IntegerField(
        validators=[InputRequired()],
        render_kw={'placeholder':'Stock'})

    submit = SubmitField("Update")