from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class Search(FlaskForm):
    search_text = StringField('Input a word, words or hastags', validators=[DataRequired()])
    submit = SubmitField('Search')
