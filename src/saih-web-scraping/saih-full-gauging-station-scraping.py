from bs4 import BeautifulSoup
import urllib3
import json
import pandas as pd
import threading
import os 
import time

def WebSiteDataScraping(target_list, data_title, data, urlSaih):
    for i in range(len(target_list)):
        urlWrapping = urlSaih + target_list[i].attrs["href"]

        print("Data from: ", urlWrapping, data)
        
        fileName = data['id'] + '-' + data_title[i]
        GetAndPrintDataframe(urlWrapping, fileName)

def GetAndPrintDataframe(url, fileName, printDataframe=True):
    dataframes = pd.read_html(
            url,
            decimal=',',
            thousands='.') # Three dataframes.

    if(printDataframe):
        print(dataframes[0].describe())

    file = '../data/csv/' + fileName + '.csv'
    dataframes[0].to_csv(file, index=False)

def DataScraping(n_datasets, target_list, data, urlSaih):
    
    # Number of differents metrics by URL.

    dataSetA = ['Level', 'Caudal', 'Temperature', 'Pluviometry']
    dataSetB = ['Level', 'Caudal', 'Temperature']
    dataSetC = ['Level', 'Caudal']

    return {
        4: lambda: 
            WebSiteDataScraping(
            target_list=target_list,
            data_title=dataSetA,
            data=data, 
            urlSaih=urlSaih),
        3: lambda: 
            WebSiteDataScraping(
            target_list=target_list,
            data_title=dataSetB,
            data=data, 
            urlSaih=urlSaih),
        2: lambda: 
            WebSiteDataScraping(
            target_list=target_list,
            data_title=dataSetC,
            data=data, 
            urlSaih=urlSaih),
    }.get(n_datasets, lambda: None)

def worker(url, index):
    # Get URL and extract the 'href' attribute to build the URL for each dataset.
    response = http.request('get', url)
    soup = BeautifulSoup(response.data, "html.parser")
    target_list = soup.find_all("a", {"class": "mdi mdi-chart-histogram"})

    print(' - URL [', index, 'of', len(data),'] :', data[index]['url'],
    ' | DATASETS: ', len(target_list))
    
    DataScraping(
            n_datasets=len(target_list),
            target_list=target_list,
            data=data[index], 
            urlSaih=urlSAIH)()

if __name__ == "__main__":

    start = time.time()

    os.makedirs('../data/csv', exist_ok=True) 

    urlSAIH = "http://www.saihduero.es/"

    with open('../data/gauging-station.json', 'r', encoding="utf8") as file:
        data = json.load(file)

    count = 1
    threads = []

    http = urllib3.PoolManager()

    for index in range(len(data)):
        t = threading.Thread(target=worker, args=(data[index]['url'], index,))
        threads.append(t)
        t.start()

    for item in threads:
        item.join()

    end = time.time()

    print('Program execution time:' , end-start)