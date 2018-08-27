from celery import Celery
from app.api.transfer import TransferDatas
from datetime import datetime
from sqlalchemy import create_engine
from app.mydb import MyDb
from app.models import Transfer

worker = Celery('worker')
worker.config_from_object('tasks.celeryconfig')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost/exchange'
