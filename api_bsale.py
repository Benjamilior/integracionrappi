import requests
import datetime
import json
import time

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

start_time = time.time()  # Tiempo de inicio de la ejecución

    
url = "https://api.bsale.cl/v1/stocks.json" #Url de Acesso 
datos = '6cc26c07ec782ca618620c30c1e7afdeab5b165a.json'#Token de Acesso
    
headers = {
                   'Content-Type': 'application/json',
                   "access_token":"6cc26c07ec782ca618620c30c1e7afdeab5b165a"
                   }
# skus = ["100135", 'B-DAC2271-12', "100146", 'B-DAC3261-12KG', "100143", 'DPHFIT60200', 'B-DAC3255-12KG', 'DPHFIT60160', 'LA-03S', "100129", "100416", "100401", 'PETIT000004', 'VA-01H', 'DPHMASME074', "100410", 'DA-02S', 'EHLALLCA048', "100407", 'MA-04S', 'B-CAC3100-05', 'DB-16', 'DPHMASME251', 'DPHMASDE232']
skus = ["V100771", "V100787", "V100782", "V100784", "V100774", "V100785", "V100786", "V100773", "756605", "756625",
    "756266", "756256", "B212A123", "100582", "100584", "100581", "100586", "100903", "B212A163-B", "A121A034",
    "A121A084", "B212A123", "B212A165-B", "B212A124", "B211A123", "DPHFIT60160", "K11101", "K11111", "K12500",
    "K13111", "K13121", "K13131", "K11143", "K11149", "K11155", "1710012", "1710015", "1710006", "1002163",
    "1003160", "1003161", "EHLPHILI050", "PETIT000002", "K11121", "K11131", "DPHMASUR132", "4.0005E+12",
    "4.0005E+12", "DPHMASNA083", "roy3375015", "COOLPET3", "VITSIL00004", "DPHMASDI028", "TRMCANCO001",
    "CHECLACM057", "CHECLACM056", "vtqalcki133", "dphfit60200", "coolpet1", "petit000004", "cheotiso034",
    "ehlkercm019", "100584", "100582", "100581", "B-DAC3273-12KG", "100586", "100897", "VTQALCKI134",
    "CHEENRCP025", "CHEENRCP026", "AGRMAS00057", "AGRMAS00060", "DPHMASDE027", "GABMASHE001", "hil61001660",
    "hil61002600", "cheoxtcm028", "pficercm018", "b-dac3273-02kg", "f2b200431k01800", "100585", "100776",
    "100777", "100778", "100404", "100583", "vtqdogpa097", "bayadvpe044", "ehlehlcm009", "roy2070020",
    "agrnatcm053", "roy5377015", "roy5376015", "hil61007000", "roy3653015", "roy0044725", "vtqalcki136",
    "dphmasme074", "vtqalcki135", "3apoq16mg", "3apoq54mg", "cevamas00002", "3apoq36mg", "cevamas00001",
    "vitsil00002", "gabmashe002", "cheotiso015", "gabmasgli04", "pficercm019", "dphmasdi029", "dphmasde232",
    "checipof006", "dphmastr131", "dphmaspe093", "dphmasit148", "dphmasot243", "dphmascl020", "roy00044785",
    "dphmasha054", "dphmasme251", "chesucin048", "100903", "100147", "100146", "100417", "100416", "100402",
    "100401", "100144", "100143", "100130", "100129", "100136", "100135", "100898", "100901", "100906", "100408",
    "100407", "100411", "100410", "PWBIOBAG16", "1002512", "1000897", "1000775", "1000774", "CEVAMAS00004",
    "PWBIOBAGDIS", "756246", "756206", "756146", "756106", "B-DAC3263-12KG", "ROY00BW14W", "ROY00AK05Y",
    "ROY00CC64P", "B-DAC3271-12KG", "1710091", "1710015", "1710012", "1710006", "DPHMASDO037", "DPHMASDO036",
    "VEGABOHM6804", "F2B200631K04500", "F2B200631K01800", "B-DAT3010-35G", "PFIAPOCM043", "PFIAPOCM042",
    "PFIAPOCM044", "DPHMASGA053", "VEGABFAD3207", "HIL61001661", "VEGABCAD5909", "VEGABCAD0426", "B-DAC3255-12KG",
    "B-DAC3255-06KG", "B-DAC3261-12KG", "B-DAC3261-06KG", "B-DAC3261-02KG", "B-DAC2273-12", "B-DAC2273-06",
    "B-DAC2273-02", "B-DAC2271-12", "B-DAC2271-06", "B-DAC2271-02", "B-CAC3110-05", "B-CAC3110-02",
    "B-CAC3100-05", "B-CAC3100-02", "VTQMALPA034", "VTQGELDE101", "VTQDOGPA079", "VTQDOGPA078", "CHEFLOJE054",
    "BAYADVPE045", "BAYADVGA041", "BAYADVGA040", "CA-04S-01", "DA-02S-01", "DB-16", "MA-04S", "FA-31", "VA-01H",
    "DA-02S", "LA-03S", "CENPEDSP017", "CENPEDSP022", "DPHFIT00920", "ROY3683015", "CEVAMAS00003", "CEVAMAS00009",
    "CEVAMAS00010", "CEVAMAS00011", "ROY5801015", "CEVAMAS00007", "ROY5101105", "CEVAMAS00008", "ROY3673015",
    "CEVCORAL022", "CEVCORAL023", "CEVACC00029", "PFIREVPI054", "PFIREVPI055", "PROMAS00006", "AGRARTCM043",
    "ANAMAS00055", "LUDMAS00003", "LUDMAS00007", "LUDMAS00008", "LUDMAS00010", "LUDMAS00011", "LUDMAS00012"]

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'abc.json'
creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
 
SPREADSHEET_ID = '1CHkQo1hxYcy1kJgQNHuQxDQIWldZIachwPv08nU84FE'
 
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
     
#SKU
for sku in skus:
     params2={
           'code': sku,
           'limit': 2
           }
     #Peticion a la API
     response = requests.get(url=url, headers=headers, params=params2)
     json_response = response.json()
     
      #Sacar la cantidad de stock 
     for item in json_response['items']:
        quantity = item['quantity']
        print(quantity)
        
        
end_time = time.time()  # Tiempo de finalización de la ejecución

execution_time = end_time - start_time
print(execution_time)
    

                                