import requests
import sys

coinpair = sys.argv[1]

#------------------------------------------
baseurl = "https://api.bitpreco.com/"
url = baseurl + coinpair + "/trades"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
