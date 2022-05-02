from config import *
import requests
import json

ENDPOINT_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = f"{ENDPOINT_URL}/v2/account"
ORDERS_URL = f"{ENDPOINT_URL}/v2/orders"
HEADERS = {
    'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}


def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)  # convert json msg -> dict


def create_order(symbol, qty, side, type, time_in_force):
    data = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': time_in_force
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return json.loads(r.content)


def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)
    return json.loads(r.content)


# response = create_order('AAPL', 100, 'buy', 'market',
#                        'gtc')  # gtc = good till cancelled
response = create_order('MSFT', 100, 'buy', 'market', 'gtc')


orders = get_orders()

print(orders)
