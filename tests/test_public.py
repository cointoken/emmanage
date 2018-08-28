
from datetime import datetime
from copy import deepcopy,copy
from collections import OrderedDict

def test_status(status):
    if status in range(0,2):
        print(status)

def test_bool(status):
    if status:
        print('true')
    else:
        print('false')

dic = OrderedDict()
dic1 = deepcopy(dic)
dic2 =  copy(dic1)

print(id(dic),id(dic1),id(dic2))
print(dic is dic2)