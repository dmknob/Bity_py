import requests
import os
from dotenv import load_dotenv

load_dotenv()
auth_token = os.getenv("auth_token")

#------------------------------------------
url = "https://api.bitpreco.com/v1/trading"

payload={'cmd': 'sell',
'auth_token': auth_token,
'market': 'btc-brl',
'price': '380000',
'volume': '',
'amount': '0.00010000',
'limited': 'true'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
