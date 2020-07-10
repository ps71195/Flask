from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, InputRequired

#hello
class Login(FlaskForm):
    username = StringField('Username', validators=[Length(min=2, max=30, message="not proper")])
    email = StringField('Email', validators=[DataRequired(), Email()])

    submit = SubmitField('Submit')