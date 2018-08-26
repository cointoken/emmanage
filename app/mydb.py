from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from datetime import datetime
from .models import Members
from .models import Transfer

class MyDb(object):
    def __init__(self,engine):
        self.engine = engine
        self.session = sessionmaker(bind=engine)()


    def members_insert(self,members):
        if isinstance(members,Members) and members is not None:
            self.session.add(members)
            self.session.commit()


    def transfer_insert(self,transfer):
        if isinstance(transfer,Transfer) and transfer is not None:
            r = self.session.query(Transfer).filter_by(address=transfer.address,status=0,currency=transfer.currency,withdraw_time=transfer.withdraw_time,audit_time=transfer.audit_time).first()
            if not r:
                self.session.add(transfer)
                self.session.commit()


    def transfer_query_all(self,is_transfer,currency,page_size,page_index):
        if currency:  #func.count(Transfer.id).label('count'),
            datas = ''
            if is_transfer:
                datas = self.session.query(Transfer).filter_by(status=1,currency=currency).order_by(Transfer.transfer_time.desc()).slice((page_index- 1) * page_size, page_index *page_size)
            else:
                datas = self.session.query(Transfer).filter_by(status=0,currency=currency).order_by(Transfer.audit_time.desc()).slice((page_index- 1) * page_size, page_index *page_size)
            return datas
        return ''
    

    def transfer_get_count(self,is_transfer,currency):
        count = 0
        if currency:
            if is_transfer:
                count = self.session.query(func.count(Transfer.id).label('count')).filter_by(status=1,currency=currency).first()[0]
            else:
                count = self.session.query(func.count(Transfer.id).label('count')).filter_by(status=0,currency=currency).first()[0]
        return count
                
        
    def transfer_update(self,address,txid):
        if address and txid:
            transfer = self.session.query(Transfer).filter_by(address=address,status=0).order_by(Transfer.audit_time.desc()).first()
            if transfer:
                transfer.txid = txid
                transfer.status = True
                transfer.transfer_time = datetime.now()
                self.session.commit()


    # def transfer_query_from_currtime(self):
    #     datas = self.session.query(Transfer).filter_by(status=1,transfer_time=).order_by(Transfer.transfer_time.desc()).all()
    # alembic init mymigrate
    # alembic revision --autogenerate -m "create tables"
    # alembic upgrade head