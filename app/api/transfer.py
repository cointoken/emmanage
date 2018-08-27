import requests
import json


class TransferDatas():
    def __init__(self):
        pass


    @staticmethod
    def get_transfer_data(name):
        result = ''
        url = 'http://192.168.1.143:3000/admin/audit_withdraws'
        try:
            r = requests.get(url)
            js = json.loads(r.content.decode('utf-8'))
            if js:
                if js['status'] == 200:
                    return js[name]
        except:
            result = 'error'
        return result


