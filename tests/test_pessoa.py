import unittest

from app import app
import settings
from flask_sqlalchemy import SQLAlchemy
from database.models import Pessoa


class TestPessoa(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

        self.db = SQLAlchemy(app)

    def test_all_pessoa(self):
        self.db.session.query(Pessoa).all()

    def test_create_pessoa(self):
        p1 = Pessoa(nome="Jose", cpf="99873213232")
        self.db.session.add(p1)
        self.db.session.commit()
        self.db.session.refresh(p1)
        self.assertTrue(isinstance(p1.id, int))

    def test_update_pessoa(self):
        p = self.db.session.query(Pessoa).order_by(Pessoa.id.desc()).first()
        # p = self.db.session.query(Pessoa).filter_by(id=10).first()
        p.nome = 'José Teste'
        p.cpf = '99999999999'
        self.db.session.add(p)
        self.db.session.commit()

    def test_delete_pessoa(self):
        p = self.db.session.query(Pessoa).order_by(Pessoa.id.desc()).first()
        # p = self.db.session.query(Pessoa).get(10)
        self.db.session.delete(p)
        self.db.session.commit()


if __name__ == '__main__':
    unittest.main()
