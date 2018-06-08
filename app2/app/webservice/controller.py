# Author: Junior Tada
from sanic import Blueprint
from sanic.response import json
from app.db import session_scope
from app.webservice.db import DaoInfo

# Define o blueprint
webservice = Blueprint('webservice')

@webservice.route('/consultar_dados_cliente', methods=['POST'])
async def consultar_dados_cliente(request):
    dados = request.json
    if dados:
        with session_scope() as session:
            dao = DaoInfo(session)
            cliente = dao.buscar_cpf(dados['cpf'])
            dic = cliente.json
            return json(dic)

@webservice.route('/consultar_fonte_renda', methods=['POST'])
async def consultar_fonte_renda(request):
    dados = request.json
    if dados:
        with session_scope() as session:
            dao = DaoInfo(session)
            fonte_renda = dao.buscar_fonte_renda(dados['cpf'])
            return json(fonte_renda)