#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import numpy as np

def GetSubPlotTittle(place, hours, array):
    title = place + ' ' + \
            '(In the last ' + \
            str(hours) + 'h: '+ \
            "{:.2f}".format(sum(array)) + ' l/m²)'

    return title

nombres = [
        'Pluviometry-Morla de la Valderia',     # B
        'Pluviometry-Nogarejas',                # C
        'Pluviometry-Corporales',               # E
        'Pluviometry-Truchillas'                # F
    ]

nHours = 48
now = datetime.now()
dataframes = []

for i in range(len(nombres)):
    csv_fileName = './data/saih-data-scraper/pluviometry/' + nombres[i].replace(' ','-') + '.csv'

    dataframes.append(pd.read_csv(csv_fileName))

x = []

xDateTime = dataframes[0]['Datetime'].tail(nHours).values
for i in range(len(xDateTime)):
    date = datetime.strptime(xDateTime[i], '%d/%m/%Y %H:%M')
    x.append(date.strftime("%d/%m %HH"))

yA = dataframes[0]['Pluviometry (l/m2)'].tail(nHours).values
yA_acumulative = np.cumsum(yA)

yB = dataframes[1]['Pluviometry (l/m2)'].tail(nHours).values
yB_acumulative = np.cumsum(yB)

yC = dataframes[2]['Pluviometry (l/m2)'].tail(nHours).values
yC_acumulative = np.cumsum(yC)

yD = dataframes[3]['Pluviometry (l/m2)'].tail(nHours).values
yD_acumulative = np.cumsum(yD)

# Plot
fig, axs = plt.subplots(2, 2, figsize=(26, 12), sharey=True)
plotTittle = 'Rain (l/m²) - Sistema Automático de Información Hidrológica (SAIH) (Generation Time: ' \
    + str(now.strftime("%d/%m/%y, %H:%M:%S")) + ') ' + 'Author: @JaviKarra94'
fig.suptitle(plotTittle, fontsize=16)

axs[0,0].bar(x, yA)
axs[0,0].plot(x,yA_acumulative)
axs[0,0].grid(axis='y')
axs[0,0].set_xlabel(GetSubPlotTittle(nombres[0].replace('Pluviometry-',''), nHours, yA), fontsize=13)
axs[0,0].set_ylabel('(l/m2)', fontsize=15)
axs[0,0].set_xticklabels(x,rotation=80, ha = 'center')
for i in range(nHours):
    axs[0,0].text(x=x[i], y=yA[i] + 0.5, s=yA[i], fontsize=10,
                    horizontalalignment='center')

axs[0,1].bar(x, yB)
axs[0,1].plot(x,yB_acumulative)
axs[0,1].grid(axis='y')
axs[0,1].set_xlabel(GetSubPlotTittle(nombres[1].replace('Pluviometry-',''), nHours, yB), fontsize=13)
axs[0,1].set_ylabel('(l/m2)', fontsize=15)
axs[0,1].set_xticklabels(x, rotation=80, ha = 'center')
for i in range(nHours):
    axs[0,1].text(x=x[i], y=yB[i] + 0.5, s=yB[i], fontsize=10, 
                    horizontalalignment='center')

axs[1,0].bar(x, yC)
axs[1,0].plot(x,yC_acumulative)
axs[1,0].grid(axis='y')
axs[1,0].set_xlabel(GetSubPlotTittle(nombres[2].replace('Pluviometry-',''), nHours, yC), fontsize=13)
axs[1,0].set_ylabel('(l/m2)', fontsize=15)
axs[1,0].set_xticklabels(x, rotation=80, ha = 'center')
for i in range(nHours):
    axs[1,0].text(x=x[i],y=yC[i] + 0.5, s=yC[i], fontsize=10, 
                    horizontalalignment='center')

axs[1,1].bar(x, yD)
axs[1,1].plot(x,yD_acumulative)
axs[1,1].grid(axis='y')
axs[1,1].set_xlabel(GetSubPlotTittle(nombres[3].replace('Pluviometry-',''), nHours, yD), fontsize=13)
axs[1,1].set_ylabel('(l/m2)', fontsize=15)
axs[1,1].set_xticklabels(x,rotation=80, ha = 'center')
for i in range(nHours):
    axs[1,1].text(x=x[i],y=yD[i] + 0.5, s=yD[i], fontsize=10, 
                horizontalalignment='center')


fig.tight_layout()
fig.savefig('./images/saih-rain-and-acum-48h' + now.strftime("%d-%m-%y_%Hh") +'.png')