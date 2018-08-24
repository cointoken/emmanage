import csv
import requests
import json 
import transfer


class Mycsv():
    def __init__(self,filename):
        self.filename = filename


    def write_csv(self,content):
        if content and self.filename:
            with open(self.filename,'w',newline ='') as f:
                w = csv.writer(f,dialect='excel')
                for c in content:
                    if c['fund_uid']:
                        w.writerow([c['fund_uid'],c['amount']])


# if __name__=='__main__':
    
#    datas = transfer.TransferDatas.get_transfer_data()
#    c = Mycsv('11.csv')
#    c.write_csv(datas)
