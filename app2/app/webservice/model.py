# Author: Junior Tada
from app.db import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import JSON

class Info(Base):
    __tablename__ = 'info'

    cpf = Column(String)
    json = Column(JSON)