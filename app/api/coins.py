import requests
import json
from datetime import datetime
import time

class Coins():
    
    @staticmethod
    def get_curr_seconds():
        return int(time.mktime(datetime.now().timetuple()))


    @staticmethod
    def btc_transactions(address,amount):
        result = ''
        if address and amount >0:
            btc_url = 'https://bitaps.com/api/address/transactions/{0}'.format(address)
            try:
                r = requests.get(btc_url)
                if r.content:
                    js = json.loads(r.content)
                    if js:
                        amount = amount * 100000000
                        now_seconds = Coins.get_curr_seconds()
                        for j in js:
                            if now_seconds-j[0]<1800 and j[3]=='received' and j[4]=='confirmed' and j[7]==amount:
                                return j[1]
            except:
                result = 'error'
        return result 


    @staticmethod
    def eth_get_transaction(address,amount):
        result = ''
        if address and amount>0:
            eth_url = 'http://api.ethplorer.io/getAddressTransactions/{0}'.format(address)
            params = {'apiKey':'freekey'}
            r = requests.get(eth_url,params=params)
            rc = r.content
            if rc :
                js = json.loads(rc)
                try:
                    if js:
                        now_seconds = Coins.get_curr_seconds() 
                        for j in js:
                            if now_seconds-j['timestamp']<1800 and j['to']==address.lower() and j['value']==amount and j['success']==True:
                                return j['hash']
                except:
                    result = 'error'
        return result

    
    @staticmethod
    def etc_get_transaction(address,amount):
        result = ''
        if address and amount>0:
            etc_url = 'https://api.gastracker.io/v1/addr/{0}/operations'.format(address)
            r = requests.get(etc_url)
            js = json.loads(r.content)
            if js:
                try:
                    js = js['items']
                    now_date = datetime.today().strftime('%Y-%m-%d')
                    for j in js:
                       if j['timestamp'].find(now_date)!=-1 and j['to']==address and j['value']['ether']==amount and j['isSend']==False and j['failed']==False:
                           return j['hash']
                except:
                    result = 'error'
        return result          


    @staticmethod
    def usdt_get_transaction(address,amount):
        result = ''
        deposit_url = 'https://api.omniexplorer.info/v1/transaction/address'
        post_data = {
            'addr': address,
            'page': 0
        }
        if address:
            r = requests.post(deposit_url,data=post_data)
            j = json.loads(r.content)
            try:
                toaddress = j['address']
                ts = j['transactions']
                if ts:
                    now_seconds = Coins.get_curr_seconds() 
                    for t in ts:
                        if toaddress == address and t['amount']==amount and now_seconds-t['blocktime']<1800 and t['valid']==True:
                            return t['txid']
            except:
                result = 'error'
        return result


    @staticmethod
    def ltc_get_transactions(address,amount):
        result = ''
        ltc_url = 'https://chain.so/api/v2/address/ltc/{0}'
        if address:
            r = requests.get(ltc_url.format(address))
            j = json.loads(r.content)
            try:
                txs =  j['data']['txs']
                for tx in txs:
                    if 'incoming' in tx:
                        if float(tx['incoming']['value'])==amount and  tx['confirmations']>0:
                            return tx['txid']
            except:
                result = 'error'
        return result


        
# if __name__=='__main__':
#     print(Coins.usdt_get_transaction('1Lsvv4Ucqe2yMByJJ7HY4ajP6H7B8k77jv',0))
#     # #Coins.btc_transactions('18cBEMRxXHqzWWCxZNtU91F5sbUNKhL5PX',12.53265359)
#     # #print(Coins.etc_get_transaction('0xad505C8e97F0E53C20f6b6D49f74c1ccB8EC998F',0.02))
#     # #print(int(time.mktime(datetime.now().timetuple())))
#     # today = datetime.today().strftime('%Y-%m-%d')
#     # cc = "2018-08-26T03:24:11"
#     # #@print(today)
#     # if cc.find(today)!=-1:
    #     print(today)