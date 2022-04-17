from operator import le
import pandas as pd
# import matplotlib

nombres = [
        'Morla de la Valderia',
        'Nogarejas',
        'Castrocalbon',
        'Corporales',
        'Truchillas']

temperatura = [      
        'http://www.saihduero.es/risr/EA089/historico/xATRUFURflDOwEUR', # Morla de la Valderia
        'http://www.saihduero.es/risr/PL283/historico/xATRUFURfNDOywEU', # Nogarejas
        'http://www.saihduero.es/risr/PL284/historico/xATRUFURfRDOywEU', # Castrocalbon
        'http://www.saihduero.es/risr/PL282/historico/xATRUFURfJDOywEU', # Corporales
        'http://www.saihduero.es/risr/PL281/historico/xATRUFURfFDOywEU'  # Truchillas
]

publiometria = [
        'http://www.saihduero.es/risr/EA089/historico/xADTQNURflDOwEUR', # Morla de la Valderia
        'http://www.saihduero.es/risr/PL283/historico/xADTQNURfNDOywEU', # Nogarejas
        'http://www.saihduero.es/risr/PL284/historico/xADTQNURfRDOywEU', # Castrocalbon
        'http://www.saihduero.es/risr/PL282/historico/xADTQNURfJDOywEU', # Corporales
        'http://www.saihduero.es/risr/PL281/historico/xADTQNURfFDOywEU'  # Truchillas
]

for index in range(len(temperatura)):
        print("Data from: ", nombres[index])
        dataframes = pd.read_html(temperatura[index],
                decimal=',',thousands='.') # Three dataframes.
        print('Dataframe len():', len(dataframes), 'type(dataframses):', type(dataframes))
        for i in range(len(dataframes)):
                print(dataframes[i])

