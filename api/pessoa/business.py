from database import db
from database.models import Pessoa, Endereco

'''
Pessoa
'''


def create_pessoa(data):
    nome = data.get('nome')
    cpf = data.get('cpf')

    pessoa = Pessoa(nome, cpf)
    db.session.add(pessoa)
    db.session.commit()


def update_pessoa(pessoa_id, data):
    pessoa = Pessoa.query.filter(Pessoa.id == pessoa_id).one()
    pessoa.nome = data.get('nome')
    pessoa.cpf = data.get('cpf')
    # endereco_id = data.get('endereco_id')
    # pessoa.endereco = Endereco.query.filter(Endereco.id == endereco_id).one()
    db.session.add(pessoa)
    db.session.commit()


def delete_pessoa(pessoa_id):
    pessoa = Pessoa.query.filter(Pessoa.id == pessoa_id).one()
    db.session.delete(pessoa)
    db.session.commit()


'''
Endereco
'''


def create_endereco(data):
    endereco = data.get('endereco')
    cidade = data.get('cidade')
    estado = data.get('estado')
    cep = data.get('cep')
    pessoa_id = data.get('pessoa_id')
    #pessoa = Endereco.query.filter(Pessoa.id == pessoa_id).one()

    endereco = Endereco(endereco, cidade, estado, cep, pessoa_id)
    db.session.add(endereco)
    db.session.commit()


def update_endereco(endereco_id, data):
    endereco = Endereco.query.filter(Endereco.id == endereco_id).one()

    endereco.endereco = data.get('endereco')
    endereco.cidade = data.get('cidade')
    endereco.estado = data.get('estado')
    endereco.cep = data.get('cep')
    endereco.pessoa_id = data.get('pessoa_id')

    # endereco_id = data.get('endereco_id')
    # pessoa.endereco = Endereco.query.filter(Endereco.id == endereco_id).one()
    db.session.add(endereco)
    db.session.commit()


def delete_endereco(endereco_id):
    endereco = Endereco.query.filter(Endereco.id == endereco_id).one()
    db.session.delete(endereco)
    db.session.commit()