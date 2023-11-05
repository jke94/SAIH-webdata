import requests
from lxml import html
from threading import Thread


class HttpRequestThread(Thread):
    
    def __init__(self, url: str) -> None:
        
        super().__init__()
        
        self.url = url
        self.http_status_code = None
        self.reason = None
        self.response = None

    def run(self) -> None:
        
        try:
            
            self.response = extracting_cuenca_vertiente(url=self.url)
            
        except requests.exceptions.HTTPError as e:
            self.http_status_code = e.code
        except Exception as e:
            self.reason = e.reason

urls = [
'https://www.saihduero.es/risr/EA153',
'https://www.saihduero.es/risr/EA046',
'https://www.saihduero.es/risr/EA500',
'https://www.saihduero.es/risr/EA158',
'https://www.saihduero.es/risr/EA167',
'https://www.saihduero.es/risr/EA056',
'https://www.saihduero.es/risr/EA501',
'https://www.saihduero.es/risr/EA502',
'https://www.saihduero.es/risr/EA503',
'https://www.saihduero.es/risr/EA092',
'https://www.saihduero.es/risr/EA137',
'https://www.saihduero.es/risr/EA505',
'https://www.saihduero.es/risr/EA155',
'https://www.saihduero.es/risr/EA712',
'https://www.saihduero.es/risr/EA719',
'https://www.saihduero.es/risr/EA165',
'https://www.saihduero.es/risr/EA166',
'https://www.saihduero.es/risr/EA028',
'https://www.saihduero.es/risr/EA030',
'https://www.saihduero.es/risr/EA507',
'https://www.saihduero.es/risr/EA031',
'https://www.saihduero.es/risr/EA036',
'https://www.saihduero.es/risr/EA508',
'https://www.saihduero.es/risr/EA109',
'https://www.saihduero.es/risr/EA032',
'https://www.saihduero.es/risr/EA139',
'https://www.saihduero.es/risr/EA116',
'https://www.saihduero.es/risr/EA098',
'https://www.saihduero.es/risr/EA510',
'https://www.saihduero.es/risr/EA115',
'https://www.saihduero.es/risr/EA119',
'https://www.saihduero.es/risr/EA034',
'https://www.saihduero.es/risr/EA035',
'https://www.saihduero.es/risr/EA182',
'https://www.saihduero.es/risr/EA131',
'https://www.saihduero.es/risr/EA511',
'https://www.saihduero.es/risr/EA512',
'https://www.saihduero.es/risr/EA108',
'https://www.saihduero.es/risr/EA037',
'https://www.saihduero.es/risr/EA134',
'https://www.saihduero.es/risr/EA023',
'https://www.saihduero.es/risr/EA040',
'https://www.saihduero.es/risr/EA042',
'https://www.saihduero.es/risr/EA514',
'https://www.saihduero.es/risr/EA181',
'https://www.saihduero.es/risr/EA717',
'https://www.saihduero.es/risr/EA104',
'https://www.saihduero.es/risr/EA073',
'https://www.saihduero.es/risr/EA516',
'https://www.saihduero.es/risr/EA016',
'https://www.saihduero.es/risr/EA517',
'https://www.saihduero.es/risr/EA518',
'https://www.saihduero.es/risr/EA063',
'https://www.saihduero.es/risr/EA068',
'https://www.saihduero.es/risr/EA147',
'https://www.saihduero.es/risr/EA151',
'https://www.saihduero.es/risr/EA519',
'https://www.saihduero.es/risr/EA520',
'https://www.saihduero.es/risr/EA713',
'https://www.saihduero.es/risr/EA101',
'https://www.saihduero.es/risr/EA001',
'https://www.saihduero.es/risr/EA002',
'https://www.saihduero.es/risr/EA162',
'https://www.saihduero.es/risr/EA163',
'https://www.saihduero.es/risr/EA004',
'https://www.saihduero.es/risr/EA017',
'https://www.saihduero.es/risr/EA522',
'https://www.saihduero.es/risr/EA013',
'https://www.saihduero.es/risr/EA132',
'https://www.saihduero.es/risr/EA015',
'https://www.saihduero.es/risr/EA054',
'https://www.saihduero.es/risr/EA062',
'https://www.saihduero.es/risr/EA121',
'https://www.saihduero.es/risr/EA524',
'https://www.saihduero.es/risr/EA012',
'https://www.saihduero.es/risr/EA161',
'https://www.saihduero.es/risr/EA525',
'https://www.saihduero.es/risr/EA526',
'https://www.saihduero.es/risr/EA050',
'https://www.saihduero.es/risr/EA053',
'https://www.saihduero.es/risr/EA527',
'https://www.saihduero.es/risr/EA089',
'https://www.saihduero.es/risr/EA082',
'https://www.saihduero.es/risr/EA049',
'https://www.saihduero.es/risr/EA528',
'https://www.saihduero.es/risr/EA025',
'https://www.saihduero.es/risr/EA044',
'https://www.saihduero.es/risr/EA529',
'https://www.saihduero.es/risr/EA102',
'https://www.saihduero.es/risr/EA103',
'https://www.saihduero.es/risr/EA111',
'https://www.saihduero.es/risr/EA710',
'https://www.saihduero.es/risr/EA711',
'https://www.saihduero.es/risr/EA074',
'https://www.saihduero.es/risr/EA530',
'https://www.saihduero.es/risr/EA129',
'https://www.saihduero.es/risr/EA094',
'https://www.saihduero.es/risr/EA531',
'https://www.saihduero.es/risr/EA718',
'https://www.saihduero.es/risr/EA136',
'https://www.saihduero.es/risr/EA532',
'https://www.saihduero.es/risr/EA122',
'https://www.saihduero.es/risr/EA075',
'https://www.saihduero.es/risr/EA168',
'https://www.saihduero.es/risr/EA533',
'https://www.saihduero.es/risr/EA051',
'https://www.saihduero.es/risr/EA055',
'https://www.saihduero.es/risr/EA052',
'https://www.saihduero.es/risr/EA113',
'https://www.saihduero.es/risr/EA018',
'https://www.saihduero.es/risr/EA138',
'https://www.saihduero.es/risr/EA076',
'https://www.saihduero.es/risr/EA061',
'https://www.saihduero.es/risr/EA060',
'https://www.saihduero.es/risr/EA145',
'https://www.saihduero.es/risr/EA079',
'https://www.saihduero.es/risr/EA535',
'https://www.saihduero.es/risr/EA123',
'https://www.saihduero.es/risr/EA141',
'https://www.saihduero.es/risr/EA057',
'https://www.saihduero.es/risr/EA536',
'https://www.saihduero.es/risr/EA106',
'https://www.saihduero.es/risr/EA019',
'https://www.saihduero.es/risr/EA020',
'https://www.saihduero.es/risr/EA024',
'https://www.saihduero.es/risr/EA133',
'https://www.saihduero.es/risr/EA029',
'https://www.saihduero.es/risr/EA043',
'https://www.saihduero.es/risr/EA097',
'https://www.saihduero.es/risr/EA078',
'https://www.saihduero.es/risr/EA011',
'https://www.saihduero.es/risr/EA112',
'https://www.saihduero.es/risr/EA716',
'https://www.saihduero.es/risr/EA157',
'https://www.saihduero.es/risr/EA537',
'https://www.saihduero.es/risr/EA000',
'https://www.saihduero.es/risr/EA009',
'https://www.saihduero.es/risr/EA538',
'https://www.saihduero.es/risr/EA552',
'https://www.saihduero.es/risr/EA010',
'https://www.saihduero.es/risr/EA539',
'https://www.saihduero.es/risr/EA107',
'https://www.saihduero.es/risr/EA022',
'https://www.saihduero.es/risr/EA169',
'https://www.saihduero.es/risr/EA124',
'https://www.saihduero.es/risr/EA160',
'https://www.saihduero.es/risr/EA818',
'https://www.saihduero.es/risr/EA080',
'https://www.saihduero.es/risr/EA541',
'https://www.saihduero.es/risr/EA099',
'https://www.saihduero.es/risr/EA164',
'https://www.saihduero.es/risr/EA542',
'https://www.saihduero.es/risr/EA150',
'https://www.saihduero.es/risr/EA006',
'https://www.saihduero.es/risr/EA085',
'https://www.saihduero.es/risr/EA081',
'https://www.saihduero.es/risr/EA140',
'https://www.saihduero.es/risr/EA545',
'https://www.saihduero.es/risr/EA087',
'https://www.saihduero.es/risr/EA546',
'https://www.saihduero.es/risr/EA547',
'https://www.saihduero.es/risr/EA077',
'https://www.saihduero.es/risr/EA156',
'https://www.saihduero.es/risr/EA159',
'https://www.saihduero.es/risr/EA154',
'https://www.saihduero.es/risr/EA005',
'https://www.saihduero.es/risr/EA041',
'https://www.saihduero.es/risr/EA026',
'https://www.saihduero.es/risr/EA135',
'https://www.saihduero.es/risr/EA105',
'https://www.saihduero.es/risr/EA126',
'https://www.saihduero.es/risr/EA548',
'https://www.saihduero.es/risr/EA549',
'https://www.saihduero.es/risr/EA047',
'https://www.saihduero.es/risr/EA114',
'https://www.saihduero.es/risr/EA550',
'https://www.saihduero.es/risr/EA551',
'https://www.saihduero.es/risr/EM551',
'https://www.saihduero.es/risr/EM602',
'https://www.saihduero.es/risr/EM601',
'https://www.saihduero.es/risr/EM042',
'https://www.saihduero.es/risr/EM041',
'https://www.saihduero.es/risr/EM102',
'https://www.saihduero.es/risr/EM101',
'https://www.saihduero.es/risr/EM003',
'https://www.saihduero.es/risr/EM006',
'https://www.saihduero.es/risr/EM002',
'https://www.saihduero.es/risr/EM005',
'https://www.saihduero.es/risr/EM008',
'https://www.saihduero.es/risr/EM001',
'https://www.saihduero.es/risr/EM004',
'https://www.saihduero.es/risr/EM007',
'https://www.saihduero.es/risr/EM521',
'https://www.saihduero.es/risr/EM522',
'https://www.saihduero.es/risr/EM541',
'https://www.saihduero.es/risr/EM171',
'https://www.saihduero.es/risr/EM172',
'https://www.saihduero.es/risr/EM231',
'https://www.saihduero.es/risr/EM232',
'https://www.saihduero.es/risr/EM062',
'https://www.saihduero.es/risr/EM061',
'https://www.saihduero.es/risr/EM181',
'https://www.saihduero.es/risr/EM511',
'https://www.saihduero.es/risr/EM091',
'https://www.saihduero.es/risr/EM292',
'https://www.saihduero.es/risr/EM294',
'https://www.saihduero.es/risr/EM293',
'https://www.saihduero.es/risr/EM574',
'https://www.saihduero.es/risr/EM572',
'https://www.saihduero.es/risr/EM571',
'https://www.saihduero.es/risr/EM261',
'https://www.saihduero.es/risr/PL551',
'https://www.saihduero.es/risr/PL601',
'https://www.saihduero.es/risr/PL602',
'https://www.saihduero.es/risr/PL031',
'https://www.saihduero.es/risr/PL042',
'https://www.saihduero.es/risr/PL041',
'https://www.saihduero.es/risr/PL211',
'https://www.saihduero.es/risr/PL214',
'https://www.saihduero.es/risr/PL213',
'https://www.saihduero.es/risr/PL212',
'https://www.saihduero.es/risr/PL065',
'https://www.saihduero.es/risr/PL101',
'https://www.saihduero.es/risr/PL102',
'https://www.saihduero.es/risr/PL222',
'https://www.saihduero.es/risr/PL192',
'https://www.saihduero.es/risr/PL191',
'https://www.saihduero.es/risr/PL273',
'https://www.saihduero.es/risr/PL272',
'https://www.saihduero.es/risr/PL271',
'https://www.saihduero.es/risr/PL002',
'https://www.saihduero.es/risr/PL001',
'https://www.saihduero.es/risr/PL542',
'https://www.saihduero.es/risr/PL283',
'https://www.saihduero.es/risr/PL282',
'https://www.saihduero.es/risr/PL281',
'https://www.saihduero.es/risr/PL284',
'https://www.saihduero.es/risr/PL173',
'https://www.saihduero.es/risr/PL172',
'https://www.saihduero.es/risr/PL171',
'https://www.saihduero.es/risr/PL581',
'https://www.saihduero.es/risr/PL232',
'https://www.saihduero.es/risr/PL231',
'https://www.saihduero.es/risr/PL234',
'https://www.saihduero.es/risr/PL233',
'https://www.saihduero.es/risr/PL295',
'https://www.saihduero.es/risr/PL043',
'https://www.saihduero.es/risr/PL253',
'https://www.saihduero.es/risr/PL251',
'https://www.saihduero.es/risr/PL255',
'https://www.saihduero.es/risr/PL254',
'https://www.saihduero.es/risr/PL174',
'https://www.saihduero.es/risr/PL532',
'https://www.saihduero.es/risr/PL063',
'https://www.saihduero.es/risr/PL061',
'https://www.saihduero.es/risr/PL064',
'https://www.saihduero.es/risr/PL181',
'https://www.saihduero.es/risr/PL512',
'https://www.saihduero.es/risr/PL511',
'https://www.saihduero.es/risr/PL293',
'https://www.saihduero.es/risr/PL292',
'https://www.saihduero.es/risr/PL004',
'https://www.saihduero.es/risr/PL003',
'https://www.saihduero.es/risr/PL201',
'https://www.saihduero.es/risr/PL204',
'https://www.saihduero.es/risr/PL202',
'https://www.saihduero.es/risr/PL573',
'https://www.saihduero.es/risr/PL576',
'https://www.saihduero.es/risr/PL571',
'https://www.saihduero.es/risr/PL575',
'https://www.saihduero.es/risr/PL574',
'https://www.saihduero.es/risr/PL577',
'https://www.saihduero.es/risr/PL261',
'https://www.saihduero.es/risr/PL265',
'https://www.saihduero.es/risr/PL263',
'https://www.saihduero.es/risr/PL262',
'https://www.saihduero.es/risr/PL051',
'https://www.saihduero.es/risr/PL045',
'https://www.saihduero.es/risr/PL044',
'https://www.saihduero.es/risr/PL052',
'https://www.saihduero.es/risr/PL543',
'https://www.saihduero.es/risr/PL175' 
]

ulrs_mini = [
    'https://www.saihduero.es/risr/EA165',
    'https://www.saihduero.es/risr/EA166',
    'https://www.saihduero.es/risr/EA500',
    'https://www.saihduero.es/risr/EA158',
    'https://www.saihduero.es/risr/PL175' 
]

xpath_cuenca = '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/p//text()'
xpath_nombre = '/html/body/div[2]/div/div/div[1]/div[1]/h3//text()'
xpath_tipo = '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]/strong//text()'

def extracting_cuenca_vertiente(url:str):
    
    value = 'NONE'
    nombre = 'NONE_NOMBRE'
    tipo = 'NONE_tipo'
    
    response = requests.get(url)
    
    tree = html.fromstring(response.content)
    results = tree.xpath(xpath_cuenca)

    if 'km2' in results and len(results) == 2:
        value = results[0]
        
    tree = html.fromstring(response.content)
    results_nombre = tree.xpath(xpath_nombre)
    
    if len(results_nombre) == 1:
        nombre = results_nombre[0]
        
    tree = html.fromstring(response.content)
    results_tipo = tree.xpath(xpath_tipo)
    
    if len(results_tipo) == 1:
        tipo = results_tipo[0]
    
    return url + '\t' + nombre + '\t' + value + '\t' + tipo

# A. Create new threads
threads = [HttpRequestThread(url) for url in urls]
# threads = [HttpRequestThread(url) for url in ulrs_mini]

# B. Start the threads
[t.start() for t in threads]

# C. Wait for the threads to complete
[t.join() for t in threads]

# D. Display the URLs with HTTP status codes
[print(f'{t.response}') for t in threads]

print("The end!")