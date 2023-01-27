import os

from datetime import datetime
from random import randrange
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

conn = create_engine(
    os.getenv('AIRFLOW__DATABASE__SQL_ALCHEMY_CONN')).connect()
Base = declarative_base()

meta = MetaData(conn).reflect()
dwhConnection = conn.connect()
SessionDwh = sessionmaker(bind=dwhConnection)
sessionDwh = SessionDwh()


class factLocations(Base):
    __tablename__ = 'factLocations'
    id = Column(Integer, autoincrement=True, primary_key=True)
    location = Column(String(), nullable=False)
    cep_min = Column(String(), nullable=False)
    cep_max = Column(String(), nullable=False)
    situation_id = Column(Integer, ForeignKey("dimSituations.id"))
    situation = relationship("dimSituations", backref='situation')
    type_id = Column(Integer, ForeignKey("dimTypes.id"))
    type = relationship("dimTypes", backref="type")
    uf_id = Column(Integer, ForeignKey("dimUFs.id"))
    uf = relationship("dimUFs", backref="uf")



class dimSituations(Base):
    __tablename__ = 'dimSituations'
    id = Column(Integer, autoincrement=True, primary_key=True)
    label = Column(String(), unique=True)


class dimTypes(Base):
    __tablename__ = 'dimTypes'
    id = Column(Integer, autoincrement=True, primary_key=True)
    label = Column(String(), unique=True)


class dimUFs(Base):
    __tablename__ = 'dimUFs'
    id = Column(Integer, autoincrement=True, primary_key=True)
    label = Column(String(), unique=True)


def create():
    isRun = False
    Base.metadata.drop_all(bind=conn)
    Base.metadata.create_all(bind=conn)
    sessionDwh.commit()
    sessionDwh.close()
    dwhConnection.close()