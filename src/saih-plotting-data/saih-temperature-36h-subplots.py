import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def GetSubPlotTittle(place, hours, array):
    title = place + ' ' + \
            '(In the last ' + \
            str(hours) + 'h average: '+ \
            "{:.2f}".format(sum(array)/hours) + ' ºC)'

    return title

def CreatePlotTittle():

    tittle = 'Temperatura ambiente (ºC) - Sistema Automático de Información Hidrológica (SAIH) (Generation Time: ' \
        + str(now.strftime("%d/%m/%y, %H:%M:%S")) + ') ' + 'Author: @JaviKarra94'

    return tittle

if __name__ == "__main__":

    nombres = [
            'Temperature-Velilla de La Valduerna',
            'Temperature-Morla de la Valderia',
            'Temperature-Nogarejas',
            'Temperature-Castrocalbon',
            'Temperature-Corporales',
            'Temperature-Truchillas'
        ]

    places = [
        'Velilla de La Valduerna',
        'Morla de La Valederia',
        'Nogarejas',
        'Castrocalbon',
        'Corporales',
        'Truchillas'
    ]

    nHours = 36
    nColsPlot = 3
    nRowsPlot = 2
    x = []
    ys = []
    dataframes = []

    count = 0
    now = datetime.now()

    for i in range(len(nombres)):
        csv_fileName = './data/saih-data-scraper/temperature/' + nombres[i].replace(' ','-') + '.csv'

        dataframes.append(pd.read_csv(csv_fileName))

    xDateTime = dataframes[0]['Datetime'].tail(nHours).values

    for i in range(len(xDateTime)):
        date = datetime.strptime(xDateTime[i], '%d/%m/%Y %H:%M')
        x.append(date.strftime("%d/%m %HH"))

    for i in range(len(places)):
        ys.append(dataframes[count]['Temperatura ambiente (ºC)'].tail(nHours).values)
        count = count + 1

    # Plot
    fig, axs = plt.subplots(nrows=nRowsPlot, ncols=nColsPlot, figsize=(28, 12), sharey=True)

    fig.suptitle(CreatePlotTittle(), fontsize=16)

    for i in range (nRowsPlot):
        for j in range(nColsPlot):

            axs[i,j].plot(x, ys[i * nColsPlot + j], c='red')
            axs[i,j].grid(axis='y')
            axs[i,j].set_xlabel(GetSubPlotTittle(places[i * nColsPlot + j], nHours, ys[i * nColsPlot + j]), fontsize=13)
            axs[i,j].set_ylabel('ºC', fontsize=15)
            axs[i,j].set_xticklabels(x,rotation=80, ha = 'center')      
            for k in range(nHours):
                axs[i,j].text(  x=x[k], 
                                y=ys[i * nColsPlot + j][k] + 0.05, 
                                s=ys[i * nColsPlot + j][k], 
                                fontsize=10,
                                horizontalalignment='center')

    # Fix and save.
    fig.tight_layout()
    fig.savefig('./images/saih-temperature-36h-'+ now.strftime("%d-%m-%y_%Hh") +'.png')