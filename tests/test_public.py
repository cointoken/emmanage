
from datetime import datetime

def test_status(status):
    if status in range(0,2):
        print(status)

def test_bool(status):
    if status:
        print('true')
    else:
        print('false')

test_bool(False)