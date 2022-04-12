import email
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length

class messageForm(FlaskForm):
    name = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=50),
        ],
        render_kw={"placeholder": "Name"},
    )

    email = EmailField(
        validators=[
            InputRequired(),
            Length(min=3, max=50),
        ],
        render_kw={"placeholder": "Email"},
    )

    subject = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=50)
        ],
        render_kw={"placeholder": "Subject"},
    )

    message = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=200)
        ],
        render_kw={"placeholder": "Message"},
    )

    submit = SubmitField("Send")