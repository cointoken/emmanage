# import os
# import csv
# from coins import Coins


# class Utils():

#     @classmethod
#     def check_dir(cls):
#         csv_path = 'D:\\Doc\\csv\\'
#         if os.path.exists(csv_path):
#             pdirs = os.listdir(csv_path)
#             for p in pdirs:
#                 if p == 'btc.csv':
#                     with open(csv_path+p,'r') as f:
#                         items = csv.reader(f)
#                         for item in items:
#                             txid =  Coins.btc_transactions(item[0],float(item[1]))
#                             if not txid or txid=='error':
#                                return ''
#                             else:
                                
                                
                                    
#                 elif p == 'usdt.csv':
#                     pass
#                 elif p == 'bch.csv':
#                     pass
#                 elif p == 'ltc.csv':
#                     pass
#                 elif p == 'eth.csv':
#                     pass
#                 elif p == 'etc.csv':
#                     pass


# if __name__ =='__main__':
#     Utils.check_dir()