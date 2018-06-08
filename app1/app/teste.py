from app import get_uri
from app.db import session_scope, Dao
from app.webservice.model import Cidade, Endereco, Divida, Cliente, Telefone
from datetime import datetime
from decimal import Decimal
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import json


def criar_db():
    """ 
    Cria o banco de dados caso ele não exista.
    O nome do banco será o definido no config DB_URI. 
    """
    dados = get_uri()
    con = psycopg2.connect("dbname='postgres' user='"+dados['user']+"' host='localhost' password='"+dados['password']+"'")
    cur = con.cursor()
    cur.execute("select datname from pg_catalog.pg_database where datname='"+dados['db']+"'")
    if not bool(cur.rowcount):
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur.execute('CREATE DATABASE ' + dados['db'])
    cur.close()
    con.close()


def alterar_config():
    "Muda config CRIAR_DB para False"
    filel = __file__.replace('teste.py','')+'config.json'
    cfg = None
    with open(filel, 'r') as arq:
        cfg = json.loads(arq.read())
    if cfg is not None:
        cfg['CRIAR_DB'] = False
        with open(filel, 'w') as arq:
            arq.write(json.dumps(cfg, indent=2))


def criar_exemplos():
    """
    Método que cria dados fictícios para exemplo do desafio.
    """
    try:
        with session_scope() as session:
            dao = Dao(session)

            ## exemplo 1
            cidade1 = Cidade()
            cidade1.uf = 'PR'
            cidade1.nome = 'Paranavaí'

            end1 = Endereco()
            end1.rua = 'Rua da Paz'
            end1.numero = '666'
            end1.bairro = 'Sossego'
            end1.cep = '87704-000'
            end1.cidade = cidade1

            tel1 = Telefone()
            tel1.numero = '+55 (44) 9 9177-7070'

            div1 = Divida()
            div1.vencimento = datetime.now()
            div1.valor = Decimal(150.99)

            cli1 = Cliente()
            cli1.nome = 'João das Neves'
            cli1.cpf = '123456789-01'
            cli1.rg = '123456'
            cli1.nascimento = datetime.strptime('10-06-1991', "%d-%m-%Y")
            cli1.profissao = 'Analista de Sistemas'
            cli1.email = 'joao@neves.com'
            cli1.enderecos.append(end1)
            cli1.telefones.append(tel1)
            cli1.lista_dividas.append(div1)
            dao.salvar(cli1)

            ## exemplo 2
            cidade2 = Cidade()
            cidade2.uf = 'SC'
            cidade2.nome = 'Blumenau'

            end2 = Endereco()
            end2.rua = 'Rua da Paz'
            end2.numero = '666'
            end2.bairro = 'Sossego'
            end2.cep = '87704-000'
            end2.cidade = cidade2

            tel2 = Telefone()
            tel2.numero = '+55 (47) 9 9700-1234'

            div2 = Divida()
            div2.vencimento = datetime.now()
            div2.valor = Decimal(400)

            cli2 = Cliente()
            cli2.nome = 'Sonsa Stark'
            cli2.cpf = '987654321-98'
            cli2.rg = '654321'
            cli2.nascimento = datetime.strptime('11-08-1992', "%d-%m-%Y")
            cli2.profissao = 'Analista de Sistemas'
            cli2.email = 'sonsa@stark.com'
            cli2.enderecos.append(end2)
            cli2.telefones.append(tel2)
            cli2.lista_dividas.append(div2)
            dao.salvar(cli2)


    except Exception as e:
        raise e