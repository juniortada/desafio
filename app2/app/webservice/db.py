from app.db import Dao
from .model import Info

class DaoInfo(Dao):
    """ 
    Classe Data Access Object para Cliente
    :param session: Sessão para realizar uma transação no DB.
    """

    def __init__(self, session):
        super().__init__(session)

    def buscar_cpf(self, cpf):
        """
        Método que busca dados por cpf.
        :param cpf: CPF do cliente. Ex: '123456789-01'
        :return: Instancia de um model Info.
        """
        try:
            return self.session.query(Info).filter_by(cpf=cpf).first()
        except Exception as e:
            raise e

    def buscar_fonte_renda(self, cpf):
        """
        Método que retorna a fonte de renda do cliente.
        :param cpf: CPF do cliente. Ex: '123456789-01'
        :return: Valor da fonte de renda do cliente.
        """
        try:
            cliente = self.buscar_cpf(cpf)
            return cliente.json['fonte_renda']
        except Exception as e:
            raise e