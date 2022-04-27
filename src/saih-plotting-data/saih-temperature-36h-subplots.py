import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def GetSubPlotTittle(place, hours, array):
    title = place + ' ' + \
            '(In the last ' + \
            str(hours) + 'h: '+ \
            "{:.2f}".format(sum(array)) + ' l/m²)'

    return title

nombres = [
        'Temperature-Velilla de La Valduerna',  # A
        'Temperature-Morla de la Valderia',     # B
        'Temperature-Nogarejas',                # C
        'Temperature-Castrocalbon',             # D
        'Temperature-Corporales',               # E
        'Temperature-Truchillas'                # F
    ]

nHours = 36
nColPlot = 3
nRowPlot = 2

now = datetime.now()
dataframes = []

for i in range(len(nombres)):
    csv_fileName = './data/saih-data-scraper/temperature/' + nombres[i].replace(' ','-') + '.csv'

    dataframes.append(pd.read_csv(csv_fileName))

x = []

xDateTime = dataframes[0]['Datetime'].tail(nHours).values
for i in range(len(xDateTime)):
    date = datetime.strptime(xDateTime[i], '%d/%m/%Y %H:%M')
    x.append(date.strftime("%d/%m %HH"))

yA = dataframes[0]['Temperatura ambiente (ºC)'].tail(nHours).values
yB = dataframes[1]['Temperatura ambiente (ºC)'].tail(nHours).values
yC = dataframes[2]['Temperatura ambiente (ºC)'].tail(nHours).values
yD = dataframes[3]['Temperatura ambiente (ºC)'].tail(nHours).values
yE = dataframes[4]['Temperatura ambiente (ºC)'].tail(nHours).values
yF = dataframes[5]['Temperatura ambiente (ºC)'].tail(nHours).values

# Plot
fig, axs = plt.subplots(2, 3, figsize=(28, 12), sharey=True)
plotTittle = 'Temperatura ambiente (ºC) - Sistema Automático de Información Hidrológica (SAIH) (Generation Time: ' \
    + str(now.strftime("%d/%m/%y, %H:%M:%S")) + ') ' + 'Author: @JaviKarra94'
fig.suptitle(plotTittle, fontsize=16)

axs[0,0].plot(x, yA)
axs[0,0].grid(axis='y')
axs[0,0].set_xlabel(GetSubPlotTittle('Velilla de La Valduerna', nHours, yA), fontsize=13)
axs[0,0].set_ylabel('ºC', fontsize=15)
axs[0,0].set_xticklabels(x,rotation=80, ha = 'center')
for i in range(nHours):
    axs[0,0].text(x=x[i], y=yA[i] + 0.05, s=yA[i], fontsize=10,
                    horizontalalignment='center')

axs[0,1].plot(x, yB)
axs[0,1].grid(axis='y')
axs[0,1].set_xlabel(GetSubPlotTittle('Morla de La Valederia', nHours, yB), fontsize=13)
axs[0,1].set_ylabel('ºC', fontsize=15)
axs[0,1].set_xticklabels(x, rotation=80, ha = 'center')
for i in range(nHours):
    axs[0,1].text(x=x[i], y=yB[i] + 0.05, s=yB[i], fontsize=10, 
                    horizontalalignment='center')

axs[0,2].plot(x, yC)
axs[0,2].grid(axis='y')
axs[0,2].set_xlabel(GetSubPlotTittle('Nogarejas', nHours, yC), fontsize=13)
axs[0,2].set_ylabel('ºC', fontsize=15)
axs[0,2].set_xticklabels(x, rotation=80, ha = 'center')
for i in range(nHours):
    axs[0,2].text(x=x[i],y=yC[i] + 0.05, s=yC[i], fontsize=10, 
                    horizontalalignment='center')

axs[1,0].plot(x, yD)
axs[1,0].grid(axis='y')
axs[1,0].set_xlabel(GetSubPlotTittle('Castrocalbon', nHours, yD), fontsize=13)
axs[1,0].set_ylabel('ºC', fontsize=15)
axs[1,0].set_xticklabels(x,rotation=80, ha = 'center')
for i in range(nHours):
    axs[1,0].text(x=x[i],y=yD[i] + 0.05, s=yD[i], fontsize=10, 
                horizontalalignment='center')

axs[1,1].plot(x, yE)
axs[1,1].grid(axis='y')
axs[1,1].set_xlabel(GetSubPlotTittle('Corporales', nHours, yE), fontsize=13)
axs[1,1].set_ylabel('ºC', fontsize=15)
axs[1,1].set_xticklabels(x,rotation=80, ha = 'center')
for i in range(nHours):
    axs[1,1].text(x=x[i],y=yE[i] + 0.05, s=yE[i], fontsize=10, 
                horizontalalignment='center')

axs[1,2].plot(x, yF)
axs[1,2].grid(axis='y')
axs[1,2].set_xlabel(GetSubPlotTittle('Truchillas', nHours, yF), fontsize=13)
axs[1,2].set_ylabel('ºC', fontsize=15)
axs[1,2].set_xticklabels(x,rotation=80, ha = 'center')
for i in range(nHours):
    axs[1,2].text(x=x[i],y=yF[i] + 0.05, s=yF[i], fontsize=10, 
                horizontalalignment='center')

fig.tight_layout()
fig.savefig('./images/saih-temperature-36h-'+ now.strftime("%d-%m-%y_%Hh") +'.png')