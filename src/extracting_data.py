import threading
import requests
import pandas as pd
from bs4 import BeautifulSoup

class ControlPoint:
    
    def __init__(self, tipo_, description_, provincia_, rio_, localizacion_, subcuenca_, url_):
        self.tipo = tipo_
        self.description = description_
        self.provincia = provincia_
        self.rio = rio_
        self.localizacion = localizacion_
        self.subcuenca = subcuenca_
        self.url = url_
    
    def to_dict(self):
        return {
            'tipo': self.tipo,
            'description': self.description,
            'provincia': self.provincia,
            'rio': self.rio,
            'localizacion': self.localizacion,
            'subcuenca': self.subcuenca,
            'url': f'https://www.saihduero.es/{self.url}'
        }
        
    def __str__(self):
        
        tipo_str = f'Tipo: {self.tipo}'
        description_str = f'Description: {self.description}'
        provincia_str = f'Provincia: {self.provincia}'
        rio_str = f'Rio: {self.rio}'
        localization = f'Localizacion: {self.localizacion}'
        subcuenca_str = f'Subcuenca: {self.subcuenca}'
        url_str = f'URL: https://www.saihduero.es/{self.url}'
        
        return  tipo_str + ', ' \
                + description_str + ', ' \
                + provincia_str + ', ' \
                + rio_str + ', ' \
                + localization + ', ' \
                + subcuenca_str + ', ' \
                + url_str

def print_info(url:str):
    
    url_control_point = f'https://www.saihduero.es/{url}'
    # response = requests.get(url_control_point)
    
    
    print(f'\'https://www.saihduero.es/{url}\',')
    
def get_tipo(tipo:str):
    
    value = 'NONE'
    
    match tipo:
        case 'Aforo':
            value = 'Aforo'
        case 'Emb.':
            value = 'Embalse'
        case 'Pluv.':
            value = 'Pluviometro'
        case _:
            value = 'NOT_FOUND'
    
    return value
        
if __name__ == "__main__":

    URL = 'https://www.saihduero.es/resultados-risr?q=&tipo=TT'

    response = requests.get(URL)

    soup = BeautifulSoup(response.content.decode(), "html.parser")

    BACKSLASH = "\n"
    table = soup.find('table', id="table-estaciones-pagination")

    control_points = []

    for column in table.find_all('tr'):
        rows = column.find_all('td')
        
        if len(rows) == 6:
            control_points.append(ControlPoint(
                tipo_ = get_tipo(rows[0].text),
                description_ = str(rows[1].text).replace(BACKSLASH,""),
                provincia_ = str(rows[2].text).replace(BACKSLASH,""),
                rio_ = str(rows[3].text).replace(BACKSLASH,""),
                localizacion_ = str(rows[4].text).replace(BACKSLASH,""),
                subcuenca_ = str(rows[5].text).replace(BACKSLASH,""),
                url_ = str(rows[1].a["href"]).replace(BACKSLASH,"")))
    
    count = 0 
    
    ## Example: Print all data.
    # for control_point in control_points:
    #     print(f'{count} - {control_point}')
    #     count += 1  
        
    ## Example: Print different types of control
    # print(len(control_points))
    # print(f'Num. aforos = {sum(contro_point.tipo == "Aforo" for contro_point in control_points)}')
    # print(f'Num. pluviometros = {sum(contro_point.tipo == "Pluv." for contro_point in control_points)}')
    # print(f'Num. embalses = {sum(contro_point.tipo == "Emb." for contro_point in control_points)}')
    
    data = []
    
    # Example
    for contro_point in control_points:
        if contro_point.tipo == "Aforo" and contro_point.rio == "Cea":
            data.append(contro_point)
            
    ## Example
    # for contro_point in control_points:
    #     if contro_point.tipo == "Aforo" and contro_point.rio not in data:
    #         data.append(contro_point.rio)

    for item in data:
        print(item)
    print(len(data))
    
    dataframe = pd.DataFrame.from_records([item.to_dict() for item in control_points])
    
    print(dataframe)
    dataframe.to_csv('./data/saih_data_tmp.csv', index=False)
        
    ##################################
    
    threads = []
    
    for item in control_points:
        threads.append(threading.Thread(target=print_info(url=item.url)))
        
    for item in threads:
        item.start()
    
    for item in threads:
        item.join()
        
    print("The end!")
        