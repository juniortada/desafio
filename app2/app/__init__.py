# Author: Junior Tada
from sanic import Sanic
from sanic.response import json
import re

# Define app Sanic
app = Sanic()
__version__ = '0.1'
__author__ = 'Junior Tada'

# Config
from .config import config

# Log

# Principal
from app.controller import main

# Blueprints
from app.webservice.controller import webservice

# Registra blueprints
app.blueprint(webservice, url_prefix='/webservice')

def get_uri():
    """
    Método que retorna um dicionario com os dados da URI de conexão com o banco de dados.
    :return: dict com informações user, password, host e db_name
    """
    uri = config['DB_URI']
    user, password = re.search('//(.*)@', uri).group(1).split(':')
    host, db = re.search('@(.*)', uri).group(1).split('/')
    return {'user': user, 'password': password, 'host': host, 'db': db}

def _conecta():
    from app.db import conecta
    conecta()

# Cria o banco de dados e gera dados fictícios para exemplo do desafio.

if config['CRIAR_DB'] == "True":
    from app.db import Dao
    from app.teste import criar_exemplos, criar_db, alterar_config
    criar_db()
    _conecta()
    Dao.criar_tabelas()
    criar_exemplos()
    alterar_config()
else:
    _conecta()