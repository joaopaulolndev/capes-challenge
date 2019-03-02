# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from database import db


class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    cpf = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    def __init__(self, nome, cpf, pub_date=None):
        self.nome = nome
        self.cpf = cpf
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

    def __repr__(self):
        return '<Pessoa %r>' % self.nome


class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(255))
    cidade = db.Column(db.String(80))
    estado = db.Column(db.String(2))
    cep = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime)

    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'))
    pessoas = db.relationship('Pessoa', backref=db.backref('endereco', lazy='dynamic'))

    def __init__(self, endereco, cidade, estado, cep, pessoa_id, pub_date=None):
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.pessoa_id = pessoa_id

        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

    def __repr__(self):
        return '<Endereco %r>' % self.nome
