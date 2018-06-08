# Author: Junior Tada
from app.db import Base
from sqlalchemy import Integer, Column, String, ForeignKey, DateTime, \
    Boolean, DECIMAL
from sqlalchemy.orm import relationship


class Cidade(Base):
    __tablename__ = 'cidade'

    nome = Column(String)
    uf = Column(String(2))

    def __repr__(self):
        return self.nome


class Endereco(Base):
    __tablename__ = 'endereco'

    rua = Column(String)
    numero = Column(String)
    bairro = Column(String)
    complemento = Column(String)
    cep = Column(String)
    # many-to-one endereços-cidade
    cidade_id = Column(Integer, ForeignKey('cidade.id'))
    cidade = relationship('Cidade', backref='enderecos')
    # one-to-may cliente-endereços
    cliente_id = Column(Integer, ForeignKey('cliente.id'))


class Telefone(Base):
    __tablename__ = 'telefone'

    numero = Column(String)
    descricao = Column(String)
    # one-to-may cliente-telefones
    cliente_id = Column(Integer, ForeignKey('cliente.id'))


class Divida(Base):
    __tablename__ = 'divida'

    vencimento = Column(DateTime)
    valor = Column(DECIMAL(10,2))
    juros = Column(DECIMAL(10,2))
    pago = Column(Boolean, default=False)
    # one-to-may cliente-lista_dividas
    cliente_id = Column(Integer, ForeignKey('cliente.id'))


class Cliente(Base):
    __tablename__ = 'cliente'

    nome = Column(String)
    cpf = Column(String)
    rg = Column(String)
    nascimento = Column(DateTime)
    profissao = Column(String)
    email = Column(String)
    # many-to-one endereços-cliente
    enderecos = relationship("Endereco", back_populates="cliente")
    # many-to-one telefones-cliente
    telefones = relationship("Telefone", back_populates="cliente")
    # many-to-one lista_dividas-cliente
    lista_dividas = relationship("Divida", back_populates="cliente")
