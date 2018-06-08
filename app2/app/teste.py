from app import get_uri
from app.db import session_scope, Dao
from app.webservice.model import Info
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
    filel = __file__.replace('teste.py','')+'config.py'
    cfg = {
        'DEBUG': str(True),
        'CRIAR_DB': str(False),
        'DB_URI': 'postgresql+psycopg2://postgres:1234@localhost/base_b'
    }
    with open(filel, 'w') as arq:
        arq.write('config = '+json.dumps(cfg, indent=2))


def criar_exemplos():
    """
    Método que cria dados fictícios para exemplo do desafio.
    """
    try:
        with session_scope() as session:
            dao = Dao(session)

            # dados cliente 1
            info1 = Info()
            info1.cpf = '123456789-01'
            info1.json = {
                'idade': '33',
                'fonte_renda': '10000.00',
                'endereco':{
                    'rua': 'Rua da Paz',
                    'numero': '666',
                    'bairro': 'Sussego',
                    'cep': '87704-000',
                    'cidade': 'Paranavaí',
                    'uf': 'PR'
                },
                'bens': {
                    'imoveis': {
                        '1': {
                            'tipo': 'casa',
                            'valor': '300000.00'
                        },
                        '2': {
                            'tipo': 'apartamento',
                            'valor': '150000.00'
                        }
                    },
                    'moveis':{
                        '1': {
                            'tipo': 'carro',
                            'valor': '55000.00'
                        }
                    }
                }
            }
            dao.salvar(info1)

            # Dados cliente 2
            info2 = Info()
            info2.cpf = '987654321-98'
            info2.json = {
                'idade': '27',
                'fonte_renda': '6000.00',
                'endereco':{
                    'rua': 'Rua da Paz',
                    'numero': '666',
                    'bairro': 'Sussego',
                    'cep': '87704-000',
                    'cidade': 'Paranavaí',
                    'uf': 'PR'
                },
                'bens': {
                    'imoveis': {
                        '1': {
                            'tipo': 'casa',
                            'valor': '100000.00'
                        }
                    },
                    'moveis':{
                        '1': {
                            'tipo': 'moto',
                            'valor': '5500.00'
                        }
                    }
                }
            }
            dao.salvar(info2)
    except Exception as e:
        raise e