import requests
import sys

coinpair = sys.argv[1]

#------------------------------------------
baseurl = "https://api.bitpreco.com/"
url = baseurl + coinpair + "/ticker"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

import json

ticker_dic = json.loads(response.text)

last = ticker_dic["last"]
buy = ticker_dic["buy"]
sell = ticker_dic["sell"]

print(ticker_dic["buy"])
print(ticker_dic["sell"])

spread = sell/buy
print(spread)