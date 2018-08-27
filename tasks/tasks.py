from celery import Celery
from app.api.transfer import TransferDatas
from datetime import datetime
from sqlalchemy import create_engine
from app.mydb import MyDb
from app.models import Transfer
import app

myapp = Celery('tasks','redis://localhost')

@myapp.task
def datas_get():
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db = MyDb(engine)
    datas = TransferDatas.get_transfer_data()

    if datas is not None:
        for d in datas:
            t = Transfer(d['id'],d['email'],d['phone_number'],d['currency'],float(d['amount']),float(d['fee']),d['fund_uid'],datetime.strptime(d['created_at'],'%Y-%m-%d %H:%M:%S'),datetime.strptime(d['audit_time'],'%Y-%m-%d %H:%M:%S'))
            db.transfer_insert(t)