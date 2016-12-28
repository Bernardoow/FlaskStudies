
from flask import Flask, render_template, url_for, redirect

from forms import IndexSearchForm, NewHeroForm, HeroCommentForm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import exc

app = Flask(__name__)
app.secret_key = 's3cr3t'
WTF_CSRF_SECRET_KEY = "1234ABC"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/flaskr.db'
db = SQLAlchemy(app)

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    is_flyer = db.Column(db.Boolean(120))

    cases = db.relationship('Case', backref='hero',
                                lazy='dynamic')

    def __init__(self, name, is_flyer):
        self.name = name
        self.is_flyer = is_flyer

    def __repr__(self):
        return '<Hero %r>' % self.name

class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    information = db.Column(db.String(50))
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))

    def __init__(self, information, hero_id):
        self.information = information
        self.hero_id = hero_id

    def __repr__(self):
        return '<Case %r>' % self.information


@app.route('/')
def index():
    form = IndexSearchForm()
    return render_template('index.html',  form=form)

@app.route('/search-hero', methods=['POST'])
def search_hero():
    form = IndexSearchForm()
    message = ""
    if form.validate_on_submit():
        hero = Hero.query.filter_by(name= form.name.data).first()
        if hero:
            return redirect(url_for('hero_detail', hero_id=hero.id))
        else:
            message = "Hero não encontrado"

        return render_template('index.html',  form=form, message=message)


@app.route('/new-hero', methods=['GET', 'POST'])
def new_hero():
    form = NewHeroForm()
    if form.validate_on_submit():
        hero = Hero(name=form.name.data, is_flyer=form.is_flyer.data)
        try:
            db.session.add(hero)
            db.session.commit()
        except exc.IntegrityError as e:
            form.name.errors.append('Heroi já existe')
            return render_template('create_hero.html',  form=form)
        return redirect(url_for('hero_detail', hero_id=hero.id))
    else:
        return render_template('create_hero.html',  form=form)


@app.route('/hero-detail/<int:hero_id>', methods=['GET', 'POST'])
def hero_detail(hero_id):
    form = HeroCommentForm(hero_id=hero_id)
    if form.validate_on_submit():
        case_hero = Case(information=form.comment.data, hero_id=hero_id)
        db.session.add(case_hero)
        db.session.commit()

    return render_template('hero/detail.html', hero=Hero.query.get_or_404(hero_id), form=form)

