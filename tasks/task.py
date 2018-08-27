from tasks import worker,create_engine,SQLALCHEMY_DATABASE_URI,MyDb,TransferDatas,Transfer
from datetime import datetime


@worker.task
def datas_get():
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    db = MyDb(engine)
    datas = TransferDatas.get_transfer_data('data')
    if datas == 'error':
        return ''
    if datas:
        for d in datas:
            t = Transfer(d['id'],d['email'],d['phone_number'],d['currency'],float(d['amount']),float(d['fee']),d['fund_uid'],datetime.strptime(d['created_at'],'%Y-%m-%d %H:%M:%S'),datetime.strptime(d['audit_time'],'%Y-%m-%d %H:%M:%S'))
            db.transfer_insert(t)

    ids = TransferDatas.get_transfer_data('ids')
    if ids == 'error':
        return ''
    if len(ids)>0:
         for i in ids:
             db = MyDb(engine)
             db.tratransfer_update_tran_status(i)
