from operator import le
import pandas as pd
import os
# import matplotlib

nombres = [
        'Velilla de La Valduerna',
        'Morla de la Valderia',
        'Nogarejas',
        'Castrocalbon',
        'Corporales',
        'Truchillas']

temperatura = [
        'http://www.saihduero.es/risr/EA520/historico/xATRUFURfBjM1EUR', #Velilla de La Valduerna      
        'http://www.saihduero.es/risr/EA089/historico/xATRUFURflDOwEUR', # Morla de la Valderia
        'http://www.saihduero.es/risr/PL283/historico/xATRUFURfNDOywEU', # Nogarejas
        'http://www.saihduero.es/risr/PL284/historico/xATRUFURfRDOywEU', # Castrocalbon
        'http://www.saihduero.es/risr/PL282/historico/xATRUFURfJDOywEU', # Corporales
        'http://www.saihduero.es/risr/PL281/historico/xATRUFURfFDOywEU'  # Truchillas
]

publiometria = [
        'http://www.saihduero.es/risr/EA520/historico/xADTQNURfBjM1EUR', #Velilla de La Valduerna
        'http://www.saihduero.es/risr/EA089/historico/xADTQNURflDOwEUR', # Morla de la Valderia
        'http://www.saihduero.es/risr/PL283/historico/xADTQNURfNDOywEU', # Nogarejas
        'http://www.saihduero.es/risr/PL284/historico/xADTQNURfRDOywEU', # Castrocalbon
        'http://www.saihduero.es/risr/PL282/historico/xADTQNURfJDOywEU', # Corporales
        'http://www.saihduero.es/risr/PL281/historico/xADTQNURfFDOywEU'  # Truchillas
]

os.makedirs('../data/rain', exist_ok=True)

for index in range(len(publiometria)):
        print("Data from: ", nombres[index])
        dataframes = pd.read_html(publiometria[index],
                decimal=',',thousands='.') # Three dataframes.
        
        fileName = '../data/rain/' + nombres[index].replace(' ','-') + '.csv'

        dataframes[0].to_csv(fileName, index=False)

        print('Dataframe len():', len(dataframes), 'type(dataframses):', type(dataframes))
        for i in range(len(dataframes)):
                print(dataframes[i])

