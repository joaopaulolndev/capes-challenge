from flask_restplus import fields
from api.restplus import api

pessoa = api.model('Pessoa', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a pessoa'),
    'nome': fields.String(required=True, description='Nome'),
    'cpf': fields.String(required=True, description='CPF'),
    'pub_date': fields.DateTime,
    # 'endereco_id': fields.Integer(attribute='endereco.id'),
    # 'endereco': fields.String(attribute='endereco.endereco'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_pessoas = api.inherit('Page of Pessoas', pagination, {
    'items': fields.List(fields.Nested(pessoa))
})

endereco = api.model('Endereco', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a endereco'),
    'endereco': fields.String(required=True, description='Endereço'),
    'cidade': fields.String(required=True, description='Cidade'),
    'estado': fields.String(required=True, description='Estado'),
    'cep': fields.Integer(required=True, description='Cep'),
    'pessoa_id': fields.Integer(required=True, description='Pessoa ID'),
    # 'pessoa': fields.String(attribute='pessoa.id'),
})

endereco_with_pessoa = api.inherit('Endereços de Pessoas', endereco, {
    'pessoas': fields.List(fields.Nested(pessoa))
})
