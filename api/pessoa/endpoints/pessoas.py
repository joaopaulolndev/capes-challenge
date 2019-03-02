import logging

from flask import request
from flask_restplus import Resource
from api.pessoa.business import create_pessoa, update_pessoa, delete_pessoa
from api.pessoa.serializers import pessoa, page_of_pessoas
from api.pessoa.parsers import pagination_arguments
from api.restplus import api
from database.models import Pessoa

# log = logging.getLogger(__name__)

ns = api.namespace('pessoa/pessoas', description='Operações relacionadas a pessoa')


@ns.route('/')
class PessoasCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_pessoas)
    def get(self):
        """
        Retorna a lista de pessoas.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        pessoas_query = Pessoa.query
        pessoas_page = pessoas_query.paginate(page, per_page, error_out=False)

        return pessoas_page

    @api.expect(pessoa)
    def post(self):
        """
        Cria nova pessoa
        """
        create_pessoa(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Pessoa not found.')
class PessoaItem(Resource):

    @api.marshal_with(pessoa)
    def get(self, id):
        """
        Retorna uma pessoa
        """
        return Pessoa.query.filter(Pessoa.id == id).one()

    @api.expect(pessoa)
    @api.response(204, 'Pessoa successfully updated.')
    def put(self, id):
        """
        Altera uma pessoa
        """
        data = request.json
        update_pessoa(id, data)
        return None, 204

    @api.response(204, 'Pessoa successfully deleted.')
    def delete(self, id):
        """
        Apaga uma pessoa
        """
        delete_pessoa(id)
        return None, 204
