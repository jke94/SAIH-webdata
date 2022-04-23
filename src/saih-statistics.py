import pandas
import os

class RainGauge:
        '''
           Device that gather information about temperature and pluviometry.
        '''

        def __init__(self, place, urlPluviometry, urlTemperature):
                self.place = place
                self.urlPluviometry = urlPluviometry
                self.urlTemperature = urlTemperature

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
        
        return df

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
        

        # Crete the folder to save the csv data.
        os.makedirs('../data/rain', exist_ok=True)

        # Url on which to extract the data.
        url = ''

        # Wrapping data
        try:
                for index in range(len(rainGauges)):
                        
                        url = rainGauges[index].urlPluviometry

                        # Returns a list with one dataframes.
                        dataframe = pandas.read_html(
                                rainGauges[index].urlPluviometry, 
                                decimal=',',
                                thousands='.')[0]
                        
                        RenameDfColumns(dataframe)

                        # Print information about dataframe.
                        print("Data from: ", rainGauges[index].place)
                        print(dataframe)

                        # Sava dataframe as csv file.
                        fileName = '../data/rain/' + rainGauges[index].place.replace(' ','-') + '.csv'
                        dataframe.to_csv(fileName, index=False)

        except Exception as e:
                print('ERROR!:', e)
                print('ERROR with url', url)