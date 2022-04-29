#!/usr/bin/env python
# -*- coding: utf-8 -*- 

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
        'Pluviometry-Velilla de La Valduerna',  # A
        'Pluviometry-Morla de la Valderia',     # B
        'Pluviometry-Nogarejas',                # C
        'Pluviometry-Castrocalbon',             # D
        'Pluviometry-Corporales',               # E
        'Pluviometry-Truchillas'                # F
    ]

nHours = 36
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
yB = dataframes[1]['Pluviometry (l/m2)'].tail(nHours).values
yC = dataframes[2]['Pluviometry (l/m2)'].tail(nHours).values
yD = dataframes[3]['Pluviometry (l/m2)'].tail(nHours).values
yE = dataframes[4]['Pluviometry (l/m2)'].tail(nHours).values
yF = dataframes[5]['Pluviometry (l/m2)'].tail(nHours).values

# Plot
fig, axs = plt.subplots(2, 3, figsize=(28, 12), sharey=True)
plotTittle = 'Rain (l/m²) - Sistema Automático de Información Hidrológica (SAIH) (Generation Time: ' \
    + str(now.strftime("%d/%m/%y, %H:%M:%S")) + ') ' + 'Author: @JaviKarra94'
fig.suptitle(plotTittle, fontsize=16)

axs[0,0].bar(x, yA)
axs[0,0].grid(axis='y')
axs[0,0].set_xlabel(GetSubPlotTittle('Velilla de La Valduerna', nHours, yA), fontsize=13)
axs[0,0].set_ylabel('(l/m2)', fontsize=15)
axs[0,0].set_xticklabels(x,rotation=80, ha = 'center')
for i in range(nHours):
    axs[0,0].text(x=x[i], y=yA[i] + 0.05, s=yA[i], fontsize=10,
                    horizontalalignment='center')

axs[0,1].bar(x, yB)
axs[0,1].grid(axis='y')
axs[0,1].set_xlabel(GetSubPlotTittle('Morla de La Valederia', nHours, yB), fontsize=13)
axs[0,1].set_ylabel('(l/m2)', fontsize=15)
axs[0,1].set_xticklabels(x, rotation=80, ha = 'center')
for i in range(nHours):
    axs[0,1].text(x=x[i], y=yB[i] + 0.05, s=yB[i], fontsize=10, 
                    horizontalalignment='center')

axs[0,2].bar(x, yC)
axs[0,2].grid(axis='y')
axs[0,2].set_xlabel(GetSubPlotTittle('Nogarejas', nHours, yC), fontsize=13)
axs[0,2].set_ylabel('(l/m2)', fontsize=15)
axs[0,2].set_xticklabels(x, rotation=80, ha = 'center')
for i in range(nHours):
    axs[0,2].text(x=x[i],y=yC[i] + 0.05, s=yC[i], fontsize=10, 
                    horizontalalignment='center')

axs[1,0].bar(x, yD)
axs[1,0].grid(axis='y')
axs[1,0].set_xlabel(GetSubPlotTittle('Castrocalbon', nHours, yD), fontsize=13)
axs[1,0].set_ylabel('(l/m2)', fontsize=15)
axs[1,0].set_xticklabels(x,rotation=80, ha = 'center')
for i in range(nHours):
    axs[1,0].text(x=x[i],y=yD[i] + 0.05, s=yD[i], fontsize=10, 
                horizontalalignment='center')

axs[1,1].bar(x, yE)
axs[1,1].grid(axis='y')
axs[1,1].set_xlabel(GetSubPlotTittle('Corporales', nHours, yE), fontsize=13)
axs[1,1].set_ylabel('(l/m2)', fontsize=15)
axs[1,1].set_xticklabels(x,rotation=80, ha = 'center')
for i in range(nHours):
    axs[1,1].text(x=x[i],y=yE[i] + 0.05, s=yE[i], fontsize=10, 
                horizontalalignment='center')

axs[1,2].bar(x, yF)
axs[1,2].grid(axis='y')
axs[1,2].set_xlabel(GetSubPlotTittle('Truchillas', nHours, yF), fontsize=13)
axs[1,2].set_ylabel('(l/m2)', fontsize=15)
axs[1,2].set_xticklabels(x,rotation=80, ha = 'center')
for i in range(nHours):
    axs[1,2].text(x=x[i],y=yF[i] + 0.05, s=yF[i], fontsize=10, 
                horizontalalignment='center')

fig.tight_layout()
fig.savefig('./images/saih-rain-36h-'+ now.strftime("%d-%m-%y_%Hh") +'.png')