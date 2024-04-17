import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()
auth_token = os.getenv("auth_token")

orderid = sys.argv[1]

#------------------------------------------
url = "https://api.bitpreco.com/v1/trading"

payload={'cmd': 'order_cancel',
'auth_token': auth_token,
'order_id': orderid}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
