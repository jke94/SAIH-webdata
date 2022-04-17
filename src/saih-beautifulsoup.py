from bs4 import BeautifulSoup
import urllib3
import json
import pandas as pd

def WebSiteDataScraping(target_list, data_title, data, urlSaih):
    for i in range(len(target_list)):
        print(data_title[i], ':', urlSaih + target_list[i].attrs["href"])
        print("Data from: ", data[index]['station'])
        
        GetAndPrintDataframe(urlSaih + target_list[i].attrs["href"])

def GetAndPrintDataframe(url, printDataframe=True):
    dataframes = pd.read_html(
            url,
            decimal=',',
            thousands='.') # Three dataframes.

    if(printDataframe):
        print(dataframes[0].describe())

def DataScraping(n_datasets, target_list, data, urlSaih):
    
    # Number of diferents metrics by URL.

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

if __name__ == "__main__":

    urlSAIH = "http://www.saihduero.es/"

    with open('gauging-station.json', 'r') as file:
        data = json.load(file)

    count = 1
    http = urllib3.PoolManager()

    for index in range(len(data)):  
        # Get URL and extract the 'href' attribute to build the URL for each dataset.
        response = http.request('get', data[index]['url'])
        soup = BeautifulSoup(response.data, "html.parser")
        target_list = soup.find_all("a", {"class": "mdi mdi-chart-histogram"})

        print(' - URL [', count, 'of', len(data),'] :', data[index]['url'],
        ' | DATASETS: ', len(target_list))
        
        DataScraping(
                n_datasets=len(target_list),
                target_list=target_list,
                data=data, 
                urlSaih=urlSAIH)()

        count = count + 1