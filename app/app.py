from flask import Flask, render_template, request, flash
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from models import *

# Создание БД
create_models(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    discounts = Discounts.query.all()
    user = {}
    if request.method == 'POST':
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        try:
            user = Users.query.filter_by(telephone=telephone).one()
        except NoResultFound:
            flash('Неверный телефон или пароль.', 'danger')
            return render_template('index.html', discounts = discounts, user = {}) 
        if user and user.password == password:
            flash('Пользователь успешно найден.', 'success')
            return render_template('index.html', discounts = discounts, user = user)     

    return render_template('index.html', discounts = discounts, user = {}) 
