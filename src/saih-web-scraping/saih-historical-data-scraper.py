# WAY 1
from audioop import add
import pandas as pd
import json
from bs4 import BeautifulSoup
import urllib3

address = 'http://www.saihduero.es/historico-risr-csv?f='

with open('./data/gauging-station.json', 'r', encoding="utf8") as file:
    data = json.load(file)


http = urllib3.PoolManager()

for index in range(1):
    response = http.request('get', data[index]['url'])
    soup = BeautifulSoup(response.data, "html.parser")
    target_select = soup.find_all('select')[0]


    for item in target_select.find_all('option'):
        # print(item['value'], ':', item.getText()) # Use to name.csv
        
        url = address + item['value']
        print(url)
        df = pd.read_csv(url, skiprows=22)
        print(df)