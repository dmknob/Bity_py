import requests

url = "https://api.bitpreco.com/all-brl/ticker"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

import json

markets_dic = json.loads(response.text)

for i in markets_dic:
    if markets_dic[i] != True:
        print(markets_dic[i])
        #print(markets_dic[i]["market"])
        #print(markets_dic[i]["last"])
        #print(markets_dic[i]["market"]["buy"])
        #print(markets_dic[i]["market"]["sell"])

#print(markets_dic["USDT-BRL"]["last"])
#print(markets_dic["USDT-BRL"]["buy"])
#print(markets_dic["USDT-BRL"]["sell"])

#markets_dic_new = ""

#for i in markets_dic:
#    markets_dic_new = markets_dic_new + i
    #print(i)

#with open("markets.json", 'w') as file:
#    json.dump(markets_dic["BTC-BRL"]["market"], file)
#print(len(y["success"]))

#print(markets_dic_new)