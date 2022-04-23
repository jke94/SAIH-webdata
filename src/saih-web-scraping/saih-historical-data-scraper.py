# WAY 1
import pandas as pd
import json
from bs4 import BeautifulSoup
import urllib3

with open('../data/gauging-station.json', 'r', encoding="utf8") as file:
    data = json.load(file)


http = urllib3.PoolManager()

for index in range(2):
    # df = pd.read_csv(data[index]['url'], skiprows=22)

    response = http.request('get', data[index]['url'])
    soup = BeautifulSoup(response.data, "html.parser")
    target_select = soup.find_all('select')
    #options = target_list.find_all("option")

    print(target_select[0])
    print(type(target_select))
    print(len(target_select))
    # for item in target_list:
    #     print(item.attrs["value"])



# df = pd.read_csv("http://www.saihduero.es/historico-risr-csv?f=2153_AH2020_HQ.csv", skiprows=22)
# print(df)

########################################################################################################### WAY 2

# import urllib3

# url = "http://www.saihduero.es/historico-risr-csv?f=2153_AH2020_HQ.csv"
# http = urllib3.PoolManager()
# response = http.request('get', url)


# print(response.data)