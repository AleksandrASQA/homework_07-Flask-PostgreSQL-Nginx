from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'stepan_secret_key'

db = SQLAlchemy(app)

# Импортируем routes в конце, чтобы избежать циклического импорта
from . import routes

with app.app_context():
    db.create_all()