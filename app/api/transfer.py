import requests
import json


class TransferDatas():
    def __init__(self):
        pass


    @staticmethod
    def get_transfer_data(name):
        result = ''
        url = 'http://47.52.209.94:3030/admin/audit_withdraws'
        try:
            r = requests.get(url)
            js = json.loads(r.content.decode('utf-8'))
            if js:
                if js['status'] == 200:
                    return js[name]
        except:
            result = 'error'
        return result


