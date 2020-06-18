from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, InputRequired

class Login(FlaskForm):
    username = StringField('Username', validators=[Length(min=2, max=20, message="not proper")])
    email = StringField('Email', validators=[DataRequired(), Email()])

    submit = SubmitField('Submit')