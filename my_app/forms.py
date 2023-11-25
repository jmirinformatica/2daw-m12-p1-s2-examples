from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, InputRequired, Email

class ItemForm(FlaskForm):
    nom = StringField(
        validators = [DataRequired()]
    )
    unitats = IntegerField(
        validators = [DataRequired(), NumberRange(min=1)]
    )
    store_id = SelectField(
        validators = [InputRequired()]
    )
    submit = SubmitField()

# Formulari generic per esborrar i aprofitar la CSRF Protection
class DeleteForm(FlaskForm):
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField(
        validators = [Email(), DataRequired()]
    )
    password = PasswordField(
        validators=[ DataRequired()]
    )
    submit = SubmitField()

class ContactForm(FlaskForm):
    msg = TextAreaField(
        validators=[ DataRequired()]
    )
    submit = SubmitField()