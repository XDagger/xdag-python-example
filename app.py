# -*- coding=utf-8 -*-
# API doc https://explorer.xdag.io/api-docs

import os
import json
import requests
import time
import re
from urllib.parse import urljoin

API_URL = "https://explorer.xdag.io"

API_BLOCK = "/api/block/{block_address}"
API_BALANCE = "/api/balance/{address}"
API_STATUS = "/api/status"

# Check explorer is running or not
def get_status():
    resp = requests.get(urljoin(API_URL, API_STATUS))
    if resp.status_code == 200:
        result = json.loads(resp.content)
        if "error" in result:
            print("Error", result["message"])
            return False
        else:
            return True
    return True

# Get transactions for specified address
def get_transactions(_exchange_address):
    resp = requests.get(urljoin(API_URL, API_BLOCK.format(block_address=_exchange_address)))
    if resp.status_code == 200:
        result = json.loads(resp.content)
        if "error" in result:
            print("Error", result["message"])
            return None
        else:
            return result["block_as_address"]
    else:
        print("Network error")
        return None
    pass

# Get block info for specified block address
def get_block_info(_block_address):
    resp = requests.get(urljoin(API_URL, API_BLOCK.format(block_address=_block_address)))
    if resp.status_code == 200:
        result = json.loads(resp.content)
        if "error" in result:
            print("Error", result["message"])
            return None
        else:
            return result["block_as_transaction"]
    else:
        print("Network error")
        return None
    pass

# Check the charge sum of specified address in transactions
def check_balance_in_transactions(_transactions, _user_address, _from_time=None):
    balance = 0.0
    for tx in _transactions:
        if tx['direction'] == 'input':
            # skip last check
            if _from_time and _from_time >= time.strptime(re.sub(re.compile(r'\..*'), "", tx['time']), '%Y-%m-%d %H:%M:%S'):
                continue

            block_fields = get_block_info(tx['address'])
            if block_fields == None:
                continue
            for field in block_fields:
                if field['direction'] == 'input' and field['address'] == _user_address:
                    balance += float(field['amount'])
    return balance

# Check user charge amount
def check_user_balance(_exchange_address, _user_address, _last_check_time):
    transacations = get_transactions(_exchange_address)
    if transacations == None:
        print("Error: not transactions found.")
        return None
    
    return check_balance_in_transactions(transacations, _user_address, _last_check_time)

# xfer
def do_xfer(_user_address, _amount):
    
    pass

if __name__ == "__main__":
    my_wallet_address = "" # your wallet address
    user_wallet_address = "" # the specifed wallet address
    # last_check_time = time.strptime('2018-06-26 06:43:59', '%Y-%m-%d %H:%M:%S')
    last_check_time = 0 # your last check time

    if get_status():
        print(check_user_balance(my_wallet_address, user_wallet_address, last_check_time))
    else:
        print("Explorer is not running")
    pass