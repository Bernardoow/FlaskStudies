from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, HiddenField
from wtforms.validators import InputRequired

class IndexSearchForm(FlaskForm):
    name = StringField('Nome do Heroi', validators=[InputRequired()])
    is_flyer = BooleanField('Voa? ', validators=[])


class NewHeroForm(FlaskForm):
    name = StringField('Nome do Heroi', validators=[InputRequired()])
    is_flyer = BooleanField('Voa? ', validators=[])

class HeroCommentForm(FlaskForm):
    comment = StringField('Comentário', validators=[InputRequired()])
