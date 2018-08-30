from tasks import worker,create_engine,SQLALCHEMY_DATABASE_URI,MyDb,Transfer
from app.api.coins import Coins
import os
import csv


@worker.task
def check_transactions():
    csv_path = '/home/coins/csv/'
    if os.path.exists(csv_path):
        pdirs = os.listdir(csv_path)
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        for p in pdirs:
            if p == 'btc.csv':
                with open(csv_path+p,'r') as f:
                    items = csv.reader(f)
                    for item in items:
                        txid =  Coins.btc_transactions(item[0],float(item[1]))
                        if not txid or txid=='error':
                            return ''
                        else:
                            db = MyDb(engine)  
                            db.transfer_update(item[0],txid)
            elif p == 'usdt.csv':
                with open(csv_path+p,'r') as f:
                    items = csv.reader(f)
                    for item in items:
                        txid =  Coins.usdt_get_transaction(item[0],float(item[1]))
                        if not txid or txid=='error':
                            return ''
                        else:
                            db = MyDb(engine)  
                            db.transfer_update(item[0],txid)
            elif p == 'ltc.csv':
                with open(csv_path+p,'r') as f:
                    items = csv.reader(f)
                    for item in items:
                        txid =  Coins.ltc_get_transactions(item[0],float(item[1]))
                        if not txid or txid=='error':
                            return ''
                        else:
                            db = MyDb(engine)  
                            db.transfer_update(item[0],txid)
            elif p == 'eth.csv':
                with open(csv_path+p,'r') as f:
                    items = csv.reader(f)
                    for item in items:
                        txid =  Coins.eth_get_transaction(item[0],float(item[1]))
                        if not txid or txid=='error':
                            return ''
                        else:
                            db = MyDb(engine)  
                            db.transfer_update(item[0],txid)
            elif p == 'etc.csv':
                with open(csv_path+p,'r') as f:
                    items = csv.reader(f)
                    for item in items:
                        txid =  Coins.etc_get_transaction(item[0],float(item[1]))
                        if not txid or txid=='error':
                            return ''
                        else:
                            db = MyDb(engine)  
                            db.transfer_update(item[0],txid)

        
