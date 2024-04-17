import requests
import os
from dotenv import load_dotenv

load_dotenv()
auth_token = os.getenv("auth_token")

#------------------------------------------
url = "https://api.bitpreco.com/v1/trading"

payload={'cmd': 'balance',
'auth_token': auth_token}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
