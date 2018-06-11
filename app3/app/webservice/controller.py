# Author: Junior Tada
from sanic import Blueprint
from sanic.response import json
from app.db import db

# Define o blueprint
webservice = Blueprint('webservice')

@webservice.route('/ultima_consulta', methods=['POST'])
async def ultima_consulta(request):
    """ 
    Método que retorna os dados do Redis. 
    :return: json com dados do cliente.
    """
    dados = {}
    for key in db.keys():
        dados[key] = db.get(key)
    return json(dados)