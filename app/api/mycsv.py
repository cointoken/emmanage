import csv
from copy import deepcopy

class Mycsv():
    def __init__(self,filename):
        self.filename = filename


    def write_csv(self,content):
        result = ''
        if content and self.filename:
            try:
                with open(self.filename,'w',newline ='') as f:
                    w = csv.writer(f,dialect='excel')
                    for c in content:
                        if c['fund_uid']:
                            w.writerow([c['fund_uid'],c['amount']])
            except:
                result = 'error'
        return result
