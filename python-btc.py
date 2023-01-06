import time
import requests

def get_latest_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    data = response.json()
    return data['bpi']['USD']['rate_float']

for i in range(30):
    print(get_latest_price())
#TIMER IS SET TO 30 DAYS AND TO FETCH EACH 24HRS
    time.sleep(86400)  # pause for 2 minutes
