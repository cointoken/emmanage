#! /usr/bin/env python
from app import app
from app.api.transfer import TransferDatas
from datetime import datetime
from sqlalchemy import create_engine
from app.mydb import MyDb
from app.models import Transfer
from app.models import Members

app.run(debug=True,host="0.0.0.0",port=8080)

# if __name__=='__main__':
#     #datas = TransferDatas.get_transfer_data()
#     # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost/exchange'
#     # engine = create_engine(SQLALCHEMY_DATABASE_URI)

#     # db = MyDb(engine)
#     # m = Members('test123@163.com','test123','python18')
#     # db.members_insert(m)
#     # # db.transfer_update('3KVXgn44vYAcA7P4ADZNV4H6e31GGJC1vN','Bdueieu3KVXgn44vYAcA7P4ADZNV4H6e31GGJC1vN')
#     # print(db.transfer_query_not_status())
#     # for d in datas:
#     #     t = Transfer(d['id'],d['email'],d['phone_number'],d['currency'],float(d['amount']),float(d['fee']),d['fund_uid'],datetime.strptime(d['created_at'],'%Y-%m-%d %H:%M:%S'),datetime.strptime(d['audit_time'],'%Y-%m-%d %H:%M:%S'))
#     #     db.transfer_insert(t)
#     app.run(debug=True,host="0.0.0.0",port=8080)
    