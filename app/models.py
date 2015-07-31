from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey,DateTime
from sqlalchemy.orm import relationship
import datetime
from app import appbuilder,db


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class Terminal(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    serialNo = Column(Integer, unique=True, nullable=False)
    simNo = Column(Integer, unique=True, nullable=False)
    tdate = Column(DateTime , nullable = False)

class Army(Model):
     id = Column(Integer, primary_key=True)
