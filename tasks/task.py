from task import worker,create_engine,SQLALCHEMY_DATABASE_URI,MyDb,TransferDatas,Transfer


@worker.task
def datas_get():
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    db = MyDb(engine)
    datas = TransferDatas.get_transfer_data()

    if datas is not None:
        for d in datas:
            t = Transfer(d['id'],d['email'],d['phone_number'],d['currency'],float(d['amount']),float(d['fee']),d['fund_uid'],datetime.strptime(d['created_at'],'%Y-%m-%d %H:%M:%S'),datetime.strptime(d['audit_time'],'%Y-%m-%d %H:%M:%S'))
            db.transfer_insert(t)