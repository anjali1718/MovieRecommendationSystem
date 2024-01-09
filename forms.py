from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    fav_movie_name = StringField('MOVIE NAME', validators=[DataRequired()])
    submit = SubmitField('Submit')