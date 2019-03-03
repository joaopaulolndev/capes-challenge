from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from database.models import Pessoa, Endereco  # noqa
    db.drop_all()
    db.create_all()
