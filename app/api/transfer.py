import requests
import json

class TransferDatas():
    def __init__(self):
        pass


    @staticmethod
    def get_transfer_data():
        url = 'http://192.168.1.143:3000/admin/audit_withdraws'
        r = requests.get(url)
        js = json.loads(r.content.decode('utf-8'))
        if js:
            if js['status'] == 200:
                return js['data']
        return ''
