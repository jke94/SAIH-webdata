import requests
from lxml import html
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
                tipo_ = rows[0].text,
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
        if contro_point.tipo == "Aforo" and contro_point.rio == "Truchillas":
            data.append(contro_point)
            
    ## Example
    # for contro_point in control_points:
    #     if contro_point.tipo == "Aforo" and contro_point.rio not in data:
    #         data.append(contro_point.rio)

    for item in data:
        print(item)
    print(len(data))