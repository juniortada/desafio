from app.db import Dao
from .model import Cliente

class DaoCliente(Dao):
    """ 
    Classe Data Access Object para Cliente
    :param session: Sessão para realizar uma transação no DB.
    """

    def __init__(self, session):
        super().__init__(session)

    def buscar_cpf(self, cpf):
        """
        Método que busca um cliente pelo cpf informado.
        :param cpf: CPF do cliente. Ex: '123456789-01'
        :return: Instancia de um model Cliente.
        """
        try:
            return self.session.query(Cliente).filter_by(cpf=cpf).first()
        except Exception as e:
            self._erro('Erro ao Buscar por CPF!', e)