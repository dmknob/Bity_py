import requests
import os
from dotenv import load_dotenv

load_dotenv()
auth_token = os.getenv("auth_token")

#------------------------------------------
url = "https://api.bitpreco.com/v1/trading"

payload={'cmd': 'buy',
'auth_token': auth_token,
'market': 'btc-brl',
'price': '316001',
'volume': '',
'amount': '0.00210000',
'limited': 'true'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
