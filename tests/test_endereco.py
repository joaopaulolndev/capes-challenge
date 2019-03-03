import unittest

from app import app
import settings
from flask_sqlalchemy import SQLAlchemy
from database.models import Pessoa, Endereco


class TestEndereco(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

        self.db = SQLAlchemy(app)

    def test_all_endereco(self):
        self.db.session.query(Pessoa).all()

    def test_create_endereco(self):
        pessoa = self.db.session.query(Pessoa).order_by(Pessoa.id.desc()).first()

        end = Endereco(endereco="teste 123", cidade="Brasilia", estado="DF", cep="123456987", pessoa_id=pessoa.id)
        self.db.session.add(end)
        self.db.session.commit()
        self.db.session.refresh(end)
        self.assertTrue(isinstance(end.id, int))

    def test_update_endereco(self):
        pessoa = self.db.session.query(Pessoa).order_by(Pessoa.id.desc()).first()
        end = self.db.session.query(Endereco).order_by(Endereco.id.desc()).first()
        end.endereco = "Rua 8"
        end.cidade = "Taguatinga"
        end.estado = "GO"
        end.cep = "09831891031"
        end.pessoa_id = pessoa.id
        self.db.session.add(end)
        self.db.session.commit()

    def test_delete_endereco(self):
        e = self.db.session.query(Endereco).order_by(Endereco.id.desc()).first()
        self.db.session.delete(e)
        self.db.session.commit()


if __name__ == '__main__':
    unittest.main()
