import logging

from flask import request
from flask_restplus import Resource
from api.pessoa.business import create_endereco, delete_endereco, update_endereco
from api.pessoa.serializers import endereco, endereco_with_pessoa
from api.restplus import api
from database.models import Endereco

log = logging.getLogger(__name__)

ns = api.namespace('pessoa/enderecos', description='Operações relacionadas a endereços')


@ns.route('/')
class EnderecoCollection(Resource):

    @api.marshal_list_with(endereco)
    def get(self):
        """
        Retorna a lista de endereços
        """
        enderecos = Endereco.query.all()
        return enderecos

    @api.response(201, 'Endereco successfully created.')
    @api.expect(endereco)
    def post(self):
        """
        Cria novo endereço
        """
        data = request.json
        create_endereco(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Endereco not found.')
class EnderecoItem(Resource):

    @api.marshal_with(endereco_with_pessoa)
    def get(self, id):
        """
        Retorna a lista de endereco com as pessoa.
        """
        return Endereco.query.filter(Endereco.id == id).one()

    @api.expect(endereco)
    @api.response(204, 'Endereco successfully updated.')
    def put(self, id):
        """
        Altera um endereço

        Use this method to change the name of a blog endereco.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "endereco": "Novo Endereco",
          "cep" : "Novo CEP"
        }
        ```

        * Specify the ID of the endereco to modify in the request URL path.
        """
        data = request.json
        update_endereco(id, data)
        return None, 204

    @api.response(204, 'Endereco successfully deleted.')
    def delete(self, id):
        """
        Apaga um endereço
        """
        delete_endereco(id)
        return None, 204
