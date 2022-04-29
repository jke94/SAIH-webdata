#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import pandas
from models.RainGauge import RainGauge
from models.RainGaugeStatistics import RainGaugeStatistics

def RenameDfColumns(df):
    '''
        Rename dataframe columns.
    '''
    if ('Fecha y hora' in df.columns):
            df.columns = df.columns.str.replace(
                    'Fecha y hora', 'Datetime', regex=False)

    if ('Pluviometría (l/m²)' in df.columns):
            df.columns = df.columns.str.replace(
                    'Pluviometría (l/m²)', 'Pluviometry (l/m2)', regex=False)

    if ('Pluviometría (l/m2)' in df.columns):
            df.columns = df.columns.str.replace(
                    'Pluviometría (l/m2)', 'Pluviometry (l/m2)', regex=False)

    if ('Temperatura ambiente (°C)' in df.columns):
            df.columns = df.columns.str.replace(
                    'Temperatura ambiente (°C)', 'Temperatura ambiente (ºC)', regex=False)

    if ('Temperatura ambiente (oC)' in df.columns):
        df.columns = df.columns.str.replace(
                    'Temperatura ambiente (oC)', 'Temperatura ambiente (ºC)', regex=False)


    return df

def GetTypeOfStatistics(statisticsType):
    '''
        Returns an string about the type of statistics that we want.
    '''
    return {
        0: 'Level',
        1: 'Caudal',
        2: 'Temperature',
        3: 'Pluviometry',
    }.get(statisticsType, 'None')

def GetStatistics(option, rainGaugesList):
    '''
        Lambda function to extact the data for the differents urls
        depending of the different parameters.
    '''
    return {
            RainGaugeStatistics.LEVEL: lambda: None,    # TODO: Implement in the future.
            RainGaugeStatistics.CAUDAL: lambda: None,   # TODO: Implement in the future.
            RainGaugeStatistics.TEMPERATURE: lambda: GetTemperatureStatistics(rainGaugesList),
            RainGaugeStatistics.PLUVIOMETRY: lambda: GetPluviometryStatistics(rainGaugesList),
    }.get(option, lambda: None)

def GetPluviometryStatistics(rainGauges):
    '''
        Using dataframes from pandas library, data requesting in the different URLs and 
        save each dataframe with the data in a csv file. 

        Pluviometric data from a Rain Gauge.
    '''

    # Crete the folder to save the csv data.
    pathFolder = './data/saih-data-scraper/pluviometry/'

    os.makedirs(pathFolder, exist_ok=True)

    # Url on which to extract the data.
    url = ''
    typeOfStatistics = GetTypeOfStatistics(int(RainGaugeStatistics.PLUVIOMETRY))

    # Wrapping data
    try:
            for index in range(len(rainGauges)):

                    url = rainGauges[index].urlPluviometry

                    # Returns a list with one dataframes.
                    dataframe = pandas.read_html(
                            url,
                            decimal=',',
                            thousands='.')[0]

                    RenameDfColumns(dataframe)

                    # Print information about dataframe.
                    print("Data from: ", rainGauges[index].place)
                    print(dataframe)

                    # Sava dataframe as csv file.
                    fileName = pathFolder + typeOfStatistics + '-' + \
                    rainGauges[index].place.replace(' ','-') + '.csv'
                    dataframe.to_csv(fileName, index=False)

    except Exception as e:
            print('ERROR!:', e)
            print('ERROR with url', url)

def GetTemperatureStatistics(rainGauges):
    '''
        Using dataframes from pandas library, data requesting in the different URLs and 
        save each dataframe with the data in a csv file. 

        Temperature data from a Rain Gauge.
    '''

    # Crete the folder to save the csv data.
    pathFolder = './data/saih-data-scraper/temperature/'

    os.makedirs(pathFolder, exist_ok=True)

    # Url on which to extract the data.
    url = ''
    typeOfStatistics = GetTypeOfStatistics(int(RainGaugeStatistics.TEMPERATURE))

    # Wrapping data
    try:
            for index in range(len(rainGauges)):

                    url = rainGauges[index].urlTemperature

                    # Returns a list with one dataframes.
                    dataframe = pandas.read_html(
                            url,
                            decimal=',',
                            thousands='.')[0]

                    RenameDfColumns(dataframe)

                    # Print information about dataframe.
                    print("Data from: ", rainGauges[index].place)
                    print(dataframe)

                    # Sava dataframe as csv file.
                    fileName = pathFolder + typeOfStatistics + '-' + \
                    rainGauges[index].place.replace(' ','-') + '.csv'
                    dataframe.to_csv(fileName, index=False)

    except Exception as e:
            print('ERROR!:', e)
            print('ERROR with url', url)

if __name__ == "__main__":

    rainGauges = []

    rainGauges.append(RainGauge(
                    place='Velilla de La Valduerna',
                    urlPluviometry='http://www.saihduero.es/risr/EA520/historico/xADTQNURfBjM1EUR',
                    urlTemperature='http://www.saihduero.es/risr/EA520/historico/xATRUFURfBjM1EUR'))

    rainGauges.append(RainGauge(
                    place='Morla de la Valderia',
                    urlPluviometry='http://www.saihduero.es/risr/EA089/historico/xADTQNURflDOwEUR',
                    urlTemperature='http://www.saihduero.es/risr/EA089/historico/xATRUFURflDOwEUR'))

    rainGauges.append(RainGauge(
                    place='Nogarejas',
                    urlPluviometry='http://www.saihduero.es/risr/PL283/historico/xADTQNURfNDOywEU',
                    urlTemperature='http://www.saihduero.es/risr/PL283/historico/xATRUFURfNDOywEU'))

    rainGauges.append(RainGauge(
                    place='Castrocalbon',
                    urlPluviometry='http://www.saihduero.es/risr/PL284/historico/xADTQNURfRDOywEU',
                    urlTemperature='http://www.saihduero.es/risr/PL284/historico/xATRUFURfRDOywEU'))

    rainGauges.append(RainGauge(
                    place='Corporales',
                    urlPluviometry='http://www.saihduero.es/risr/PL282/historico/xADTQNURfJDOywEU',
                    urlTemperature='http://www.saihduero.es/risr/PL282/historico/xATRUFURfJDOywEU'))

    rainGauges.append(RainGauge(
                    place='Truchillas',
                    urlPluviometry='http://www.saihduero.es/risr/PL281/historico/xADTQNURfFDOywEU',
                    urlTemperature='http://www.saihduero.es/risr/PL281/historico/xATRUFURfFDOywEU'))


    GetStatistics(option=int(RainGaugeStatistics.PLUVIOMETRY),rainGaugesList=rainGauges)()
    GetStatistics(option=int(RainGaugeStatistics.TEMPERATURE),rainGaugesList=rainGauges)()