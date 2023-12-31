from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'GodfreyMukira'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        create_database(app)

    return app
    


def jls_extract_def(jls_extract_var):
    return jls_extract_var

def create_database(app):
    if not path.exists('GDSCKIRINYAGA/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')