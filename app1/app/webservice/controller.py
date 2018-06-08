# Author: Junior Tada
from flask import Blueprint, request, render_template, jsonify
from app.webservice.db import DaoCliente
from app import log
from app.db import session_scope


# Define the blueprint
webservice = Blueprint('webservice', __name__)


@webservice.route('/consultar_cpf', methods=['POST'])
def consultar_cpf():
    """ 
    Método que retorna dados do cliente buscando pelo cpf informado.
    :return: json com dados do cliente
    """
    dados = request.get_json()
    if dados:
        with session_scope() as session:
            dao = DaoCliente(session)
            cliente = dao.buscar_cpf(dados['cpf'])
            dic = {'id':cliente.id, 'nome':cliente.nome}
            return jsonify(cliente=dic)


@webservice.route('/consultar_dividas', methods=['POST'])
def consultar_dividas():
    """ 
    Método que retorna dados da dívida do cliente.
    :return: json com lista de dívidas. 
    """
    dados = request.get_json()
    if dados:
        with session_scope() as session:
            dao = DaoCliente(session)
            cliente = dao.buscar_cpf(dados['cpf'])
            if cliente.lista_dividas:
                lista_dividas = [{
                    "id":i.id, 
                    "vencimento":i.vencimento,
                    "valor":i.valor,
                    "pago":i.pago} for i in cliente.lista_dividas]
            return jsonify(lista_dividas=lista_dividas)