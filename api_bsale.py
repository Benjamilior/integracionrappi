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
# skus = ["V100771", "V100787", "V100782", "V100784", "V100774", "V100785", "V100786", "V100773", "756605", "756625",
#     "756266", "756256", "B212A123", "100582", "100584", "100581", "100586", "100903", "B212A163-B", "A121A034",
#     "A121A084", "B212A123", "B212A165-B", "B212A124", "B211A123", "DPHFIT60160", "K11101", "K11111", "K12500",
#     "K13111", "K13121", "K13131", "K11143", "K11149", "K11155", "1710012", "1710015", "1710006", "1002163",
#     "1003160", "1003161", "EHLPHILI050", "PETIT000002", "K11121", "K11131", "DPHMASUR132", "4.0005E+12",
#     "4.0005E+12", "DPHMASNA083", "roy3375015", "COOLPET3", "VITSIL00004", "DPHMASDI028", "TRMCANCO001",
#     "CHECLACM057", "CHECLACM056", "vtqalcki133", "dphfit60200", "coolpet1", "petit000004", "cheotiso034",
#     "ehlkercm019", "100584", "100582", "100581", "B-DAC3273-12KG", "100586", "100897", "VTQALCKI134",
#     "CHEENRCP025", "CHEENRCP026", "AGRMAS00057", "AGRMAS00060", "DPHMASDE027", "GABMASHE001", "hil61001660",
#     "hil61002600", "cheoxtcm028", "pficercm018", "b-dac3273-02kg", "f2b200431k01800", "100585", "100776",
#     "100777", "100778", "100404", "100583", "vtqdogpa097", "bayadvpe044", "ehlehlcm009", "roy2070020",
#     "agrnatcm053", "roy5377015", "roy5376015", "hil61007000", "roy3653015", "roy0044725", "vtqalcki136",
#     "dphmasme074", "vtqalcki135", "3apoq16mg", "3apoq54mg", "cevamas00002", "3apoq36mg", "cevamas00001",
#     "vitsil00002", "gabmashe002", "cheotiso015", "gabmasgli04", "pficercm019", "dphmasdi029", "dphmasde232",
#     "checipof006", "dphmastr131", "dphmaspe093", "dphmasit148", "dphmasot243", "dphmascl020", "roy00044785",
#     "dphmasha054", "dphmasme251", "chesucin048", "100903", "100147", "100146", "100417", "100416", "100402",
#     "100401", "100144", "100143", "100130", "100129", "100136", "100135", "100898", "100901", "100906", "100408",
#     "100407", "100411", "100410", "PWBIOBAG16", "1002512", "1000897", "1000775", "1000774", "CEVAMAS00004",
#     "PWBIOBAGDIS", "756246", "756206", "756146", "756106", "B-DAC3263-12KG", "ROY00BW14W", "ROY00AK05Y",
#     "ROY00CC64P", "B-DAC3271-12KG", "1710091", "1710015", "1710012", "1710006", "DPHMASDO037", "DPHMASDO036",
#     "VEGABOHM6804", "F2B200631K04500", "F2B200631K01800", "B-DAT3010-35G", "PFIAPOCM043", "PFIAPOCM042",
#     "PFIAPOCM044", "DPHMASGA053", "VEGABFAD3207", "HIL61001661", "VEGABCAD5909", "VEGABCAD0426", "B-DAC3255-12KG",
#     "B-DAC3255-06KG", "B-DAC3261-12KG", "B-DAC3261-06KG", "B-DAC3261-02KG", "B-DAC2273-12", "B-DAC2273-06",
#     "B-DAC2273-02", "B-DAC2271-12", "B-DAC2271-06", "B-DAC2271-02", "B-CAC3110-05", "B-CAC3110-02",
#     "B-CAC3100-05", "B-CAC3100-02", "VTQMALPA034", "VTQGELDE101", "VTQDOGPA079", "VTQDOGPA078", "CHEFLOJE054",
#     "BAYADVPE045", "BAYADVGA041", "BAYADVGA040", "CA-04S-01", "DA-02S-01", "DB-16", "MA-04S", "FA-31", "VA-01H",
#     "DA-02S", "LA-03S", "CENPEDSP017", "CENPEDSP022", "DPHFIT00920", "ROY3683015", "CEVAMAS00003", "CEVAMAS00009",
#     "CEVAMAS00010", "CEVAMAS00011", "ROY5801015", "CEVAMAS00007", "ROY5101105", "CEVAMAS00008", "ROY3673015",
#     "CEVCORAL022", "CEVCORAL023", "CEVACC00029", "PFIREVPI054", "PFIREVPI055", "PROMAS00006", "AGRARTCM043",
#     "ANAMAS00055", "LUDMAS00003", "LUDMAS00007", "LUDMAS00008", "LUDMAS00010", "LUDMAS00011", "LUDMAS00012"]

skus2 = [
 {
   "Id": 39638174,
   "SKU": "V100771",
   "Stock": ""
 },
 {
   "Id": 39638169,
   "SKU": "V100787",
   "Stock": ""
 },
 {
   "Id": 39638162,
   "SKU": "V100782",
   "Stock": ""
 },
 {
   "Id": 39638172,
   "SKU": "V100784",
   "Stock": ""
 },
 {
   "Id": 39638167,
   "SKU": "V100774",
   "Stock": ""
 },
 {
   "Id": 39638168,
   "SKU": "V100785",
   "Stock": ""
 },
 {
   "Id": 39638163,
   "SKU": "V100786",
   "Stock": ""
 },
 {
   "Id": 39638166,
   "SKU": "V100773",
   "Stock": ""
 },
 {
   "Id": 39638164,
   "SKU": "756605",
   "Stock": ""
 },
 {
   "Id": 39638171,
   "SKU": "756625",
   "Stock": ""
 },
 {
   "Id": 39638175,
   "SKU": "756266",
   "Stock": ""
 },
 {
   "Id": 39638170,
   "SKU": "756256",
   "Stock": ""
 },
 {
   "Id": 39553116,
   "SKU": "B212A123",
   "Stock": ""
 },
 {
   "Id": 39458030,
   "SKU": "100582",
   "Stock": ""
 },
 {
   "Id": 39458031,
   "SKU": "100584",
   "Stock": ""
 },
 {
   "Id": 39458032,
   "SKU": "100581",
   "Stock": ""
 },
 {
   "Id": 39458033,
   "SKU": "100586",
   "Stock": ""
 },
 {
   "Id": 39458034,
   "SKU": "100903",
   "Stock": ""
 },
 {
   "Id": 39458038,
   "SKU": "B212A163-B",
   "Stock": ""
 },
 {
   "Id": 39458039,
   "SKU": "A121A034",
   "Stock": ""
 },
 {
   "Id": 39458040,
   "SKU": "A121A084",
   "Stock": ""
 },
 {
   "Id": 39458041,
   "SKU": "B212A123",
   "Stock": ""
 },
 {
   "Id": 39458044,
   "SKU": "B212A165-B",
   "Stock": ""
 },
 {
   "Id": 39458045,
   "SKU": "B212A124",
   "Stock": ""
 },
 {
   "Id": 39458046,
   "SKU": "B211A123",
   "Stock": ""
 },
 {
   "Id": 39458051,
   "SKU": "DPHFIT60160",
   "Stock": ""
 },
 {
   "Id": 39638173,
   "SKU": "K11101",
   "Stock": ""
 },
 {
   "Id": 39458052,
   "SKU": "K11111",
   "Stock": ""
 },
 {
   "Id": 39458053,
   "SKU": "K12500",
   "Stock": ""
 },
 {
   "Id": 39458054,
   "SKU": "K13111",
   "Stock": ""
 },
 {
   "Id": 39458055,
   "SKU": "K13121",
   "Stock": ""
 },
 {
   "Id": 39458061,
   "SKU": "K13131",
   "Stock": ""
 },
 {
   "Id": 39458065,
   "SKU": "K11143",
   "Stock": ""
 },
 {
   "Id": 39458066,
   "SKU": "K11149",
   "Stock": ""
 },
 {
   "Id": 39458068,
   "SKU": "K11155",
   "Stock": ""
 },
 {
   "Id": 39458070,
   "SKU": "1710012",
   "Stock": ""
 },
 {
   "Id": 39458089,
   "SKU": "1710015",
   "Stock": ""
 },
 {
   "Id": 39458093,
   "SKU": "1710006",
   "Stock": ""
 },
 {
   "Id": 39458094,
   "SKU": "1002163",
   "Stock": ""
 },
 {
   "Id": 39458095,
   "SKU": "1003160",
   "Stock": ""
 },
 {
   "Id": 39458096,
   "SKU": "1003161",
   "Stock": ""
 },
 {
   "Id": 39458097,
   "SKU": "EHLPHILI050",
   "Stock": ""
 },
 {
   "Id": 39458099,
   "SKU": "PETIT000002",
   "Stock": ""
 },
 {
   "Id": 39458100,
   "SKU": "K11121",
   "Stock": ""
 },
 {
   "Id": 39458101,
   "SKU": "K11131",
   "Stock": ""
 },
 {
   "Id": 39458029,
   "SKU": "DPHMASUR132",
   "Stock": ""
 },
 {
   "Id": 39458104,
   "SKU": "4.0005E+12",
   "Stock": ""
 },
 {
   "Id": 39458105,
   "SKU": "4.0005E+12",
   "Stock": ""
 },
 {
   "Id": 39458108,
   "SKU": "DPHMASNA083",
   "Stock": ""
 },
 {
   "Id": 24858254,
   "SKU": "roy3375015",
   "Stock": ""
 },
 {
   "Id": 24667617,
   "SKU": "COOLPET3",
   "Stock": ""
 },
 {
   "Id": 24667614,
   "SKU": "VITSIL00004",
   "Stock": ""
 },
 {
   "Id": 24858242,
   "SKU": "DPHMASDI028",
   "Stock": ""
 },
 {
   "Id": 24858247,
   "SKU": "TRMCANCO001",
   "Stock": ""
 },
 {
   "Id": 24858245,
   "SKU": "CHECLACM057",
   "Stock": ""
 },
 {
   "Id": 24858256,
   "SKU": "CHECLACM056",
   "Stock": ""
 },
 {
   "Id": 24858252,
   "SKU": "vtqalcki133",
   "Stock": ""
 },
 {
   "Id": 24858241,
   "SKU": "dphfit60200",
   "Stock": ""
 },
 {
   "Id": 24858238,
   "SKU": "coolpet1",
   "Stock": ""
 },
 {
   "Id": 24858257,
   "SKU": "petit000004",
   "Stock": ""
 },
 {
   "Id": 24858243,
   "SKU": "cheotiso034",
   "Stock": ""
 },
 {
   "Id": 24858240,
   "SKU": "ehlkercm019",
   "Stock": ""
 },
 {
   "Id": 24583944,
   "SKU": "100584",
   "Stock": ""
 },
 {
   "Id": 24583949,
   "SKU": "100582",
   "Stock": ""
 },
 {
   "Id": 24583936,
   "SKU": "100581",
   "Stock": ""
 },
 {
   "Id": 24583935,
   "SKU": "B-DAC3273-12KG",
   "Stock": ""
 },
 {
   "Id": 24583921,
   "SKU": "100586",
   "Stock": ""
 },
 {
   "Id": 24583939,
   "SKU": "100897",
   "Stock": ""
 },
 {
   "Id": 24583957,
   "SKU": "VTQALCKI134",
   "Stock": ""
 },
 {
   "Id": 24583947,
   "SKU": "CHEENRCP025",
   "Stock": ""
 },
 {
   "Id": 24583951,
   "SKU": "CHEENRCP026",
   "Stock": ""
 },
 {
   "Id": 24583940,
   "SKU": "AGRMAS00057",
   "Stock": ""
 },
 {
   "Id": 24583932,
   "SKU": "AGRMAS00060",
   "Stock": ""
 },
 {
   "Id": 24583942,
   "SKU": "DPHMASDE027",
   "Stock": ""
 },
 {
   "Id": 24583959,
   "SKU": "GABMASHE001",
   "Stock": ""
 },
 {
   "Id": 24583928,
   "SKU": "hil61001660",
   "Stock": ""
 },
 {
   "Id": 24583960,
   "SKU": "hil61002600",
   "Stock": ""
 },
 {
   "Id": 24583952,
   "SKU": "cheoxtcm028",
   "Stock": ""
 },
 {
   "Id": 24583938,
   "SKU": "pficercm018",
   "Stock": ""
 },
 {
   "Id": 24583941,
   "SKU": "b-dac3273-02kg",
   "Stock": ""
 },
 {
   "Id": 24583927,
   "SKU": "f2b200431k01800",
   "Stock": ""
 },
 {
   "Id": 24583929,
   "SKU": "100585",
   "Stock": ""
 },
 {
   "Id": 24583943,
   "SKU": "100776",
   "Stock": ""
 },
 {
   "Id": 24583954,
   "SKU": "100777",
   "Stock": ""
 },
 {
   "Id": 24583926,
   "SKU": "100778",
   "Stock": ""
 },
 {
   "Id": 24583958,
   "SKU": "100404",
   "Stock": ""
 },
 {
   "Id": 24583964,
   "SKU": "100583",
   "Stock": ""
 },
 {
   "Id": 24583965,
   "SKU": "vtqdogpa097",
   "Stock": ""
 },
 {
   "Id": 24583963,
   "SKU": "bayadvpe044",
   "Stock": ""
 },
 {
   "Id": 24583962,
   "SKU": "ehlehlcm009",
   "Stock": ""
 },
 {
   "Id": 24583961,
   "SKU": "roy2070020",
   "Stock": ""
 },
 {
   "Id": 23412452,
   "SKU": "agrnatcm053",
   "Stock": ""
 },
 {
   "Id": 23412453,
   "SKU": "roy5377015",
   "Stock": ""
 },
 {
   "Id": 23412454,
   "SKU": "roy5376015",
   "Stock": ""
 },
 {
   "Id": 23412450,
   "SKU": "hil61007000",
   "Stock": ""
 },
 {
   "Id": 23412451,
   "SKU": "roy3653015",
   "Stock": ""
 },
 {
   "Id": 23412456,
   "SKU": "roy0044725",
   "Stock": ""
 },
 {
   "Id": 23412462,
   "SKU": "vtqalcki136",
   "Stock": ""
 },
 {
   "Id": 23412448,
   "SKU": "dphmasme074",
   "Stock": ""
 },
 {
   "Id": 23412444,
   "SKU": "vtqalcki135",
   "Stock": ""
 },
 {
   "Id": 23412423,
   "SKU": "3apoq16mg",
   "Stock": ""
 },
 {
   "Id": 23412413,
   "SKU": "3apoq54mg",
   "Stock": ""
 },
 {
   "Id": 23412422,
   "SKU": "cevamas00002",
   "Stock": ""
 },
 {
   "Id": 23412442,
   "SKU": "3apoq36mg",
   "Stock": ""
 },
 {
   "Id": 23412421,
   "SKU": "cevamas00001",
   "Stock": ""
 },
 {
   "Id": 23412449,
   "SKU": "vitsil00002",
   "Stock": ""
 },
 {
   "Id": 23412432,
   "SKU": "gabmashe002",
   "Stock": ""
 },
 {
   "Id": 23412415,
   "SKU": "cheotiso015",
   "Stock": ""
 },
 {
   "Id": 23412417,
   "SKU": "gabmasgli04",
   "Stock": ""
 },
 {
   "Id": 23412416,
   "SKU": "pficercm019",
   "Stock": ""
 },
 {
   "Id": 23412420,
   "SKU": "dphmasdi029",
   "Stock": ""
 },
 {
   "Id": 23412427,
   "SKU": "dphmasde232",
   "Stock": ""
 },
 {
   "Id": 23412430,
   "SKU": "checipof006",
   "Stock": ""
 },
 {
   "Id": 23412434,
   "SKU": "dphmastr131",
   "Stock": ""
 },
 {
   "Id": 23412425,
   "SKU": "dphmaspe093",
   "Stock": ""
 },
 {
   "Id": 23412412,
   "SKU": "dphmasit148",
   "Stock": ""
 },
 {
   "Id": 23412418,
   "SKU": "dphmasot243",
   "Stock": ""
 },
 {
   "Id": 23412431,
   "SKU": "dphmascl020",
   "Stock": ""
 },
 {
   "Id": 23412447,
   "SKU": "roy00044785",
   "Stock": ""
 },
 {
   "Id": 23412437,
   "SKU": "dphmasha054",
   "Stock": ""
 },
 {
   "Id": 23412419,
   "SKU": "dphmasme251",
   "Stock": ""
 },
 {
   "Id": 23412441,
   "SKU": "chesucin048",
   "Stock": ""
 },
 {
   "Id": 21147112,
   "SKU": "100903",
   "Stock": ""
 },
 {
   "Id": 21147044,
   "SKU": "100147",
   "Stock": ""
 },
 {
   "Id": 21147037,
   "SKU": "100146",
   "Stock": ""
 },
 {
   "Id": 21147031,
   "SKU": "100417",
   "Stock": ""
 },
 {
   "Id": 21147023,
   "SKU": "100416",
   "Stock": ""
 },
 {
   "Id": 21147002,
   "SKU": "100402",
   "Stock": ""
 },
 {
   "Id": 21146989,
   "SKU": "100401",
   "Stock": ""
 },
 {
   "Id": 21146980,
   "SKU": "100144",
   "Stock": ""
 },
 {
   "Id": 21146944,
   "SKU": "100143",
   "Stock": ""
 },
 {
   "Id": 21146929,
   "SKU": "100130",
   "Stock": ""
 },
 {
   "Id": 21146916,
   "SKU": "100129",
   "Stock": ""
 },
 {
   "Id": 21146913,
   "SKU": "100136",
   "Stock": ""
 },
 {
   "Id": 21146901,
   "SKU": "100135",
   "Stock": ""
 },
 {
   "Id": 21146897,
   "SKU": "100898",
   "Stock": ""
 },
 {
   "Id": 21146888,
   "SKU": "100901",
   "Stock": ""
 },
 {
   "Id": 21146883,
   "SKU": "100906",
   "Stock": ""
 },
 {
   "Id": 21146665,
   "SKU": "100408",
   "Stock": ""
 },
 {
   "Id": 21146660,
   "SKU": "100407",
   "Stock": ""
 },
 {
   "Id": 21146659,
   "SKU": "100411",
   "Stock": ""
 },
 {
   "Id": 21146656,
   "SKU": "100410",
   "Stock": ""
 },
 {
   "Id": 21146655,
   "SKU": "PWBIOBAG16",
   "Stock": ""
 },
 {
   "Id": 21146055,
   "SKU": "1002512",
   "Stock": ""
 },
 {
   "Id": 21146052,
   "SKU": "1000897",
   "Stock": ""
 },
 {
   "Id": 21146050,
   "SKU": "1000775",
   "Stock": ""
 },
 {
   "Id": 21146048,
   "SKU": "1000774",
   "Stock": ""
 },
 {
   "Id": 21146002,
   "SKU": "CEVAMAS00004",
   "Stock": ""
 },
 {
   "Id": 21146000,
   "SKU": "PWBIOBAGDIS",
   "Stock": ""
 },
 {
   "Id": 21145995,
   "SKU": "756246",
   "Stock": ""
 },
 {
   "Id": 21145992,
   "SKU": "756206",
   "Stock": ""
 },
 {
   "Id": 21145991,
   "SKU": "756146",
   "Stock": ""
 },
 {
   "Id": 21145989,
   "SKU": "756106",
   "Stock": ""
 },
 {
   "Id": 21145985,
   "SKU": "B-DAC3263-12KG",
   "Stock": ""
 },
 {
   "Id": 21145976,
   "SKU": "ROY00BW14W",
   "Stock": ""
 },
 {
   "Id": 21145972,
   "SKU": "ROY00AK05Y",
   "Stock": ""
 },
 {
   "Id": 21145970,
   "SKU": "ROY00CC64P",
   "Stock": ""
 },
 {
   "Id": 21145964,
   "SKU": "B-DAC3271-12KG",
   "Stock": ""
 },
 {
   "Id": 21145963,
   "SKU": "1710091",
   "Stock": ""
 },
 {
   "Id": 21145961,
   "SKU": "1710015",
   "Stock": ""
 },
 {
   "Id": 21145959,
   "SKU": "1710012",
   "Stock": ""
 },
 {
   "Id": 21145956,
   "SKU": "1710006",
   "Stock": ""
 },
 {
   "Id": 19035784,
   "SKU": "DPHMASDO037",
   "Stock": ""
 },
 {
   "Id": 19035782,
   "SKU": "DPHMASDO036",
   "Stock": ""
 },
 {
   "Id": 19035773,
   "SKU": "VEGABOHM6804",
   "Stock": ""
 },
 {
   "Id": 18868155,
   "SKU": "F2B200631K04500",
   "Stock": ""
 },
 {
   "Id": 18868154,
   "SKU": "F2B200631K01800",
   "Stock": ""
 },
 {
   "Id": 18868148,
   "SKU": "B-DAT3010-35G",
   "Stock": ""
 },
 {
   "Id": 18868102,
   "SKU": "PFIAPOCM043",
   "Stock": ""
 },
 {
   "Id": 18868100,
   "SKU": "PFIAPOCM042",
   "Stock": ""
 },
 {
   "Id": 18868092,
   "SKU": "PFIAPOCM044",
   "Stock": ""
 },
 {
   "Id": 18868096,
   "SKU": "DPHMASGA053",
   "Stock": ""
 },
 {
   "Id": 18868085,
   "SKU": "VEGABFAD3207",
   "Stock": ""
 },
 {
   "Id": 18868076,
   "SKU": "HIL61001661",
   "Stock": ""
 },
 {
   "Id": 18868074,
   "SKU": "VEGABCAD5909",
   "Stock": ""
 },
 {
   "Id": 18868061,
   "SKU": "VEGABCAD0426",
   "Stock": ""
 },
 {
   "Id": 15710548,
   "SKU": "B-DAC3255-12KG",
   "Stock": ""
 },
 {
   "Id": 15116774,
   "SKU": "B-DAC3255-06KG",
   "Stock": ""
 },
 {
   "Id": 15116766,
   "SKU": "B-DAC3261-12KG",
   "Stock": ""
 },
 {
   "Id": 15116763,
   "SKU": "B-DAC3261-06KG",
   "Stock": ""
 },
 {
   "Id": 15116760,
   "SKU": "B-DAC3261-02KG",
   "Stock": ""
 },
 {
   "Id": 15116747,
   "SKU": "B-DAC2273-12",
   "Stock": ""
 },
 {
   "Id": 15116746,
   "SKU": "B-DAC2273-06",
   "Stock": ""
 },
 {
   "Id": 15116743,
   "SKU": "B-DAC2273-02",
   "Stock": ""
 },
 {
   "Id": 15116742,
   "SKU": "B-DAC2271-12",
   "Stock": ""
 },
 {
   "Id": 15116739,
   "SKU": "B-DAC2271-06",
   "Stock": ""
 },
 {
   "Id": 15116737,
   "SKU": "B-DAC2271-02",
   "Stock": ""
 },
 {
   "Id": 15116736,
   "SKU": "B-CAC3110-05",
   "Stock": ""
 },
 {
   "Id": 15116733,
   "SKU": "B-CAC3110-02",
   "Stock": ""
 },
 {
   "Id": 15116732,
   "SKU": "B-CAC3100-05",
   "Stock": ""
 },
 {
   "Id": 15116730,
   "SKU": "B-CAC3100-02",
   "Stock": ""
 },
 {
   "Id": 15116415,
   "SKU": "VTQMALPA034",
   "Stock": ""
 },
 {
   "Id": 15116411,
   "SKU": "VTQGELDE101",
   "Stock": ""
 },
 {
   "Id": 15116406,
   "SKU": "VTQDOGPA079",
   "Stock": ""
 },
 {
   "Id": 15116405,
   "SKU": "VTQDOGPA078",
   "Stock": ""
 },
 {
   "Id": 15116402,
   "SKU": "CHEFLOJE054",
   "Stock": ""
 },
 {
   "Id": 15116400,
   "SKU": "BAYADVPE045",
   "Stock": ""
 },
 {
   "Id": 15116397,
   "SKU": "BAYADVGA041",
   "Stock": ""
 },
 {
   "Id": 15116391,
   "SKU": "BAYADVGA040",
   "Stock": ""
 },
 {
   "Id": 13737455,
   "SKU": "CA-04S-01",
   "Stock": ""
 },
 {
   "Id": 13737490,
   "SKU": "DA-02S-01",
   "Stock": ""
 },
 {
   "Id": 13737487,
   "SKU": "DB-16",
   "Stock": ""
 },
 {
   "Id": 13737483,
   "SKU": "MA-04S",
   "Stock": ""
 },
 {
   "Id": 13737480,
   "SKU": "FA-31",
   "Stock": ""
 },
 {
   "Id": 13737477,
   "SKU": "VA-01H",
   "Stock": ""
 },
 {
   "Id": 13737458,
   "SKU": "DA-02S",
   "Stock": ""
 },
 {
   "Id": 13737469,
   "SKU": "LA-03S",
   "Stock": ""
 },
 {
   "Id": 13407285,
   "SKU": "CENPEDSP017",
   "Stock": ""
 },
 {
   "Id": 12167503,
   "SKU": "CENPEDSP022",
   "Stock": ""
 },
 {
   "Id": 11938848,
   "SKU": "DPHFIT00920",
   "Stock": ""
 },
 {
   "Id": 12167508,
   "SKU": "ROY3683015",
   "Stock": ""
 },
 {
   "Id": 7181144,
   "SKU": "CEVAMAS00003",
   "Stock": ""
 },
 {
   "Id": 6919101,
   "SKU": "CEVAMAS00009",
   "Stock": ""
 },
 {
   "Id": 6919100,
   "SKU": "CEVAMAS00010",
   "Stock": ""
 },
 {
   "Id": 6919102,
   "SKU": "CEVAMAS00011",
   "Stock": ""
 },
 {
   "Id": 6919112,
   "SKU": "ROY5801015",
   "Stock": ""
 },
 {
   "Id": 6919099,
   "SKU": "CEVAMAS00007",
   "Stock": ""
 },
 {
   "Id": 6919113,
   "SKU": "ROY5101105",
   "Stock": ""
 },
 {
   "Id": 6919098,
   "SKU": "CEVAMAS00008",
   "Stock": ""
 },
 {
   "Id": 6919114,
   "SKU": "ROY3673015",
   "Stock": ""
 },
 {
   "Id": 17365,
   "SKU": "CEVCORAL022",
   "Stock": ""
 },
 {
   "Id": 17594,
   "SKU": "CEVCORAL023",
   "Stock": ""
 },
 {
   "Id": 17908,
   "SKU": "CEVACC00029",
   "Stock": ""
 },
 {
   "Id": 17215,
   "SKU": "PFIREVPI054",
   "Stock": ""
 },
 {
   "Id": 17648,
   "SKU": "PFIREVPI055",
   "Stock": ""
 },
 {
   "Id": 17784,
   "SKU": "PROMAS00006",
   "Stock": ""
 },
 {
   "Id": 17812,
   "SKU": "AGRARTCM043",
   "Stock": ""
 },
 {
   "Id": 17466,
   "SKU": "ANAMAS00055",
   "Stock": ""
 },
 {
   "Id": 17810,
   "SKU": "LUDMAS00003",
   "Stock": ""
 },
 {
   "Id": 17208,
   "SKU": "LUDMAS00007",
   "Stock": ""
 },
 {
   "Id": 17796,
   "SKU": "LUDMAS00008",
   "Stock": ""
 },
 {
   "Id": 17406,
   "SKU": "LUDMAS00010",
   "Stock": ""
 },
 {
   "Id": 17879,
   "SKU": "LUDMAS00011",
   "Stock": ""
 },
 {
   "Id": 17801,
   "SKU": "LUDMAS00012",
   "Stock": ""
 },
 {
   "Id": 17863,
   "SKU": "LUDMAS00014",
   "Stock": ""
 },
 {
   "Id": 17815,
   "SKU": "LUDMAS00015",
   "Stock": ""
 },
 {
   "Id": 17870,
   "SKU": "LUDMAS00016",
   "Stock": ""
 },
 {
   "Id": 17723,
   "SKU": "LUDMAS00017",
   "Stock": ""
 },
 {
   "Id": 17921,
   "SKU": "LUDMAS00024",
   "Stock": ""
 },
 {
   "Id": 17145,
   "SKU": "LUDMAS00025",
   "Stock": ""
 },
 {
   "Id": 17577,
   "SKU": "LUDMAS00026",
   "Stock": ""
 },
 {
   "Id": 17730,
   "SKU": "LUDMAS00027",
   "Stock": ""
 },
 {
   "Id": 17096,
   "SKU": "LUDMAS00028",
   "Stock": ""
 },
 {
   "Id": 17232,
   "SKU": "LUDMAS00029",
   "Stock": ""
 },
 {
   "Id": 17450,
   "SKU": "INTBRACM034",
   "Stock": ""
 },
 {
   "Id": 17862,
   "SKU": "INTBRACM035",
   "Stock": ""
 },
 {
   "Id": 17803,
   "SKU": "INTBRACM036",
   "Stock": ""
 },
 {
   "Id": 17395,
   "SKU": "HILL21002002",
   "Stock": ""
 },
 {
   "Id": 17226,
   "SKU": "HILL21002003",
   "Stock": ""
 },
 {
   "Id": 17103,
   "SKU": "HILL21002024",
   "Stock": ""
 },
 {
   "Id": 17449,
   "SKU": "HILL21002017",
   "Stock": ""
 },
 {
   "Id": 17380,
   "SKU": "HILL21002057",
   "Stock": ""
 },
 {
   "Id": 17555,
   "SKU": "DPHFIT60220",
   "Stock": ""
 },
 {
   "Id": 17120,
   "SKU": "DPHFIT60180",
   "Stock": ""
 },
 {
   "Id": 17817,
   "SKU": "DPHFIT60100",
   "Stock": ""
 },
 {
   "Id": 17649,
   "SKU": "DPHFIT60140",
   "Stock": ""
 },
 {
   "Id": 17544,
   "SKU": "DPHFIT00450",
   "Stock": ""
 },
 {
   "Id": 17140,
   "SKU": "DPHFIT06000",
   "Stock": ""
 },
 {
   "Id": 17837,
   "SKU": "DPHFIT05500",
   "Stock": ""
 },
 {
   "Id": 17397,
   "SKU": "DPHFIT05000",
   "Stock": ""
 },
 {
   "Id": 17702,
   "SKU": "DPHFIT04000",
   "Stock": ""
 },
 {
   "Id": 17713,
   "SKU": "PFISIMCM040",
   "Stock": ""
 },
 {
   "Id": 17442,
   "SKU": "PFISIMCM049",
   "Stock": ""
 },
 {
   "Id": 17147,
   "SKU": "PFISIMCM036",
   "Stock": ""
 },
 {
   "Id": 17756,
   "SKU": "PFISIMCM045",
   "Stock": ""
 },
 {
   "Id": 17433,
   "SKU": "PFISIMCM039",
   "Stock": ""
 },
 {
   "Id": 17851,
   "SKU": "PFISIMCM048",
   "Stock": ""
 },
 {
   "Id": 17475,
   "SKU": "PFISIMCM038",
   "Stock": ""
 },
 {
   "Id": 17919,
   "SKU": "PFISIMCM047",
   "Stock": ""
 },
 {
   "Id": 17479,
   "SKU": "PFISIMCM041",
   "Stock": ""
 },
 {
   "Id": 17434,
   "SKU": "PFISIMCM050",
   "Stock": ""
 },
 {
   "Id": 17443,
   "SKU": "PFISIMCM037",
   "Stock": ""
 },
 {
   "Id": 17393,
   "SKU": "PFISIMCM046",
   "Stock": ""
 },
 {
   "Id": 17598,
   "SKU": "PFISYNCM010",
   "Stock": ""
 },
 {
   "Id": 17755,
   "SKU": "PFIRIMCM008",
   "Stock": ""
 },
 {
   "Id": 17427,
   "SKU": "PFIRIMCM023",
   "Stock": ""
 },
 {
   "Id": 17609,
   "SKU": "PFIRIMCM007",
   "Stock": ""
 },
 {
   "Id": 17528,
   "SKU": "PFIREVPI035",
   "Stock": ""
 },
 {
   "Id": 17875,
   "SKU": "PFIREVPI030",
   "Stock": ""
 },
 {
   "Id": 17741,
   "SKU": "PFIREVPI022",
   "Stock": ""
 },
 {
   "Id": 17911,
   "SKU": "PFIREVPI021",
   "Stock": ""
 },
 {
   "Id": 17248,
   "SKU": "PFIREVPI020",
   "Stock": ""
 },
 {
   "Id": 17850,
   "SKU": "PFIREVPI025",
   "Stock": ""
 },
 {
   "Id": 17464,
   "SKU": "VTQSPRDE102",
   "Stock": ""
 },
 {
   "Id": 17200,
   "SKU": "VTQOFTSO017",
   "Stock": ""
 },
 {
   "Id": 17356,
   "SKU": "VTQLAVTA011",
   "Stock": ""
 },
 {
   "Id": 17508,
   "SKU": "VTQLAVCA010",
   "Stock": ""
 },
 {
   "Id": 17485,
   "SKU": "VTQCALTR101",
   "Stock": ""
 },
 {
   "Id": 17418,
   "SKU": "VTQCALTA095",
   "Stock": ""
 },
 {
   "Id": 17166,
   "SKU": "VTQCALCO098",
   "Stock": ""
 },
 {
   "Id": 17617,
   "SKU": "VTQCALPI086",
   "Stock": ""
 },
 {
   "Id": 17933,
   "SKU": "VTQCALPI087",
   "Stock": ""
 },
 {
   "Id": 17223,
   "SKU": "VTQCALCO094",
   "Stock": ""
 },
 {
   "Id": 17871,
   "SKU": "VTQCALCO093",
   "Stock": ""
 },
 {
   "Id": 17665,
   "SKU": "ROY2057015",
   "Stock": ""
 },
 {
   "Id": 17160,
   "SKU": "ROY5430025",
   "Stock": ""
 },
 {
   "Id": 17732,
   "SKU": "ROY5437010",
   "Stock": ""
 },
 {
   "Id": 17689,
   "SKU": "ROY5201025",
   "Stock": ""
 },
 {
   "Id": 17695,
   "SKU": "ROY5101205",
   "Stock": ""
 },
 {
   "Id": 17398,
   "SKU": "ROY5901020",
   "Stock": ""
 },
 {
   "Id": 17463,
   "SKU": "ROY5600015",
   "Stock": ""
 },
 {
   "Id": 17113,
   "SKU": "ROY3653015",
   "Stock": ""
 },
 {
   "Id": 17144,
   "SKU": "INTBRACM026",
   "Stock": ""
 },
 {
   "Id": 17616,
   "SKU": "INTBRACM025",
   "Stock": ""
 },
 {
   "Id": 17785,
   "SKU": "INTBRACM024",
   "Stock": ""
 },
 {
   "Id": 17486,
   "SKU": "INTBRACM028",
   "Stock": ""
 },
 {
   "Id": 17591,
   "SKU": "INTBRACM027",
   "Stock": ""
 },
 {
   "Id": 17556,
   "SKU": "KIMBOD00011",
   "Stock": ""
 },
 {
   "Id": 17400,
   "SKU": "KIMBOD00010",
   "Stock": ""
 },
 {
   "Id": 17861,
   "SKU": "KIMBOD00009",
   "Stock": ""
 },
 {
   "Id": 17437,
   "SKU": "KIMBOD00008",
   "Stock": ""
 },
 {
   "Id": 17392,
   "SKU": "KIMBOD00007",
   "Stock": ""
 },
 {
   "Id": 17384,
   "SKU": "KIMBOD00006",
   "Stock": ""
 },
 {
   "Id": 17592,
   "SKU": "KIMBOD00005",
   "Stock": ""
 },
 {
   "Id": 17436,
   "SKU": "KIMBOD00004",
   "Stock": ""
 },
 {
   "Id": 17694,
   "SKU": "KIMBOD00015",
   "Stock": ""
 },
 {
   "Id": 17857,
   "SKU": "KIMBOD00014",
   "Stock": ""
 },
 {
   "Id": 17764,
   "SKU": "KIMBOD00013",
   "Stock": ""
 },
 {
   "Id": 17786,
   "SKU": "KIMBOD00012",
   "Stock": ""
 },
 {
   "Id": 17611,
   "SKU": "KIMBOD00003",
   "Stock": ""
 },
 {
   "Id": 17624,
   "SKU": "KIMBOD00001",
   "Stock": ""
 },
 {
   "Id": 17820,
   "SKU": "KIMBOD00002",
   "Stock": ""
 },
 {
   "Id": 17881,
   "SKU": "DPHMASSU143",
   "Stock": ""
 },
 {
   "Id": 17748,
   "SKU": "DPHMASSU142",
   "Stock": ""
 },
 {
   "Id": 17412,
   "SKU": "DPHMASSU127",
   "Stock": ""
 },
 {
   "Id": 17401,
   "SKU": "DPHMASSU126",
   "Stock": ""
 },
 {
   "Id": 17584,
   "SKU": "DPHMASSK245",
   "Stock": ""
 },
 {
   "Id": 17164,
   "SKU": "DPHMASSK107",
   "Stock": ""
 },
 {
   "Id": 17188,
   "SKU": "DPHMASSI246",
   "Stock": ""
 },
 {
   "Id": 17167,
   "SKU": "DPHMASSE242",
   "Stock": ""
 },
 {
   "Id": 17202,
   "SKU": "DPHMASSE247",
   "Stock": ""
 },
 {
   "Id": 17913,
   "SKU": "DPHMASRO102",
   "Stock": ""
 },
 {
   "Id": 17724,
   "SKU": "DPHMASRO101",
   "Stock": ""
 },
 {
   "Id": 17552,
   "SKU": "DPHMASRE099",
   "Stock": ""
 },
 {
   "Id": 17379,
   "SKU": "DPHMASPE095",
   "Stock": ""
 },
 {
   "Id": 17423,
   "SKU": "DPHMASPE200",
   "Stock": ""
 },
 {
   "Id": 17131,
   "SKU": "DPHMASPA092",
   "Stock": ""
 },
 {
   "Id": 17213,
   "SKU": "DPHMASPA205",
   "Stock": ""
 },
 {
   "Id": 17181,
   "SKU": "DPHMASPA087",
   "Stock": ""
 },
 {
   "Id": 17775,
   "SKU": "DPHMASPA090",
   "Stock": ""
 },
 {
   "Id": 17896,
   "SKU": "DPHMASNA082",
   "Stock": ""
 },
 {
   "Id": 17451,
   "SKU": "DPHMASMI075",
   "Stock": ""
 },
 {
   "Id": 17187,
   "SKU": "DPHMASMI076",
   "Stock": ""
 },
 {
   "Id": 17178,
   "SKU": "DPHMASSI147",
   "Stock": ""
 },
 {
   "Id": 17916,
   "SKU": "DPHMASMA073",
   "Stock": ""
 },
 {
   "Id": 17929,
   "SKU": "DPHMASMA072",
   "Stock": ""
 },
 {
   "Id": 17894,
   "SKU": "DPHMASMA071",
   "Stock": ""
 },
 {
   "Id": 17661,
   "SKU": "DPHMASSI146",
   "Stock": ""
 },
 {
   "Id": 17228,
   "SKU": "DPHMASFL049",
   "Stock": ""
 },
 {
   "Id": 17807,
   "SKU": "DPHMASDO033",
   "Stock": ""
 },
 {
   "Id": 17456,
   "SKU": "DPHMASDO031",
   "Stock": ""
 },
 {
   "Id": 17480,
   "SKU": "DPHMASDO032",
   "Stock": ""
 },
 {
   "Id": 17824,
   "SKU": "DPHMASCO024",
   "Stock": ""
 },
 {
   "Id": 17619,
   "SKU": "DPHMASBI006",
   "Stock": ""
 },
 {
   "Id": 17476,
   "SKU": "CEVJERTA021",
   "Stock": ""
 },
 {
   "Id": 17788,
   "SKU": "EHLNUTPE169",
   "Stock": ""
 },
 {
   "Id": 17471,
   "SKU": "EHLNUTGA168",
   "Stock": ""
 },
 {
   "Id": 17768,
   "SKU": "EHLALLCA048",
   "Stock": ""
 },
 {
   "Id": 17749,
   "SKU": "SPANEXTA048",
   "Stock": ""
 },
 {
   "Id": 17826,
   "SKU": "SPANEXTA043",
   "Stock": ""
 },
 {
   "Id": 17404,
   "SKU": "SPANEXTA050",
   "Stock": ""
 },
 {
   "Id": 17886,
   "SKU": "SPANEXTA045",
   "Stock": ""
 },
 {
   "Id": 17163,
   "SKU": "SPANEXTA047",
   "Stock": ""
 },
 {
   "Id": 17854,
   "SKU": "SPANEXTA042",
   "Stock": ""
 },
 {
   "Id": 17580,
   "SKU": "SPANEXTA046",
   "Stock": ""
 },
 {
   "Id": 17238,
   "SKU": "SPANEXTA041",
   "Stock": ""
 },
 {
   "Id": 17211,
   "SKU": "SPANEXTA049",
   "Stock": ""
 },
 {
   "Id": 17484,
   "SKU": "SPANEXTA044",
   "Stock": ""
 },
 {
   "Id": 17586,
   "SKU": "BAY80339942",
   "Stock": ""
 },
 {
   "Id": 17183,
   "SKU": "BAY81408662",
   "Stock": ""
 },
 {
   "Id": 17585,
   "SKU": "BAYADVGA007",
   "Stock": ""
 },
 {
   "Id": 17197,
   "SKU": "BAYADVGA031",
   "Stock": ""
 },
 {
   "Id": 17704,
   "SKU": "ANAMAS00025",
   "Stock": ""
 },
 {
   "Id": 17897,
   "SKU": "ANAMAS00024",
   "Stock": ""
 },
 {
   "Id": 17731,
   "SKU": "ANAMAS00031",
   "Stock": ""
 },
 {
   "Id": 17787,
   "SKU": "ANAMAS00021",
   "Stock": ""
 },
 {
   "Id": 17625,
   "SKU": "ANAMAS00013",
   "Stock": ""
 },
 {
   "Id": 17618,
   "SKU": "ANAMAS00042",
   "Stock": ""
 },
 {
   "Id": 17776,
   "SKU": "ANAMAS00005",
   "Stock": ""
 },
 {
   "Id": 17843,
   "SKU": "ANAMAS00035",
   "Stock": ""
 },
 {
   "Id": 17779,
   "SKU": "ANAMAS00044",
   "Stock": ""
 },
 {
   "Id": 17198,
   "SKU": "ANAMAS00048",
   "Stock": ""
 },
 {
   "Id": 17838,
   "SKU": "ANAMAS00047",
   "Stock": ""
 },
 {
   "Id": 17800,
   "SKU": "ANAMAS00046",
   "Stock": ""
 },
 {
   "Id": 17589,
   "SKU": "ANAMAS00045",
   "Stock": ""
 },
 {
   "Id": 17816,
   "SKU": "ANAMAS00041",
   "Stock": ""
 },
 {
   "Id": 17745,
   "SKU": "ANAMAS00004",
   "Stock": ""
 },
 {
   "Id": 17931,
   "SKU": "ANAMAS00003",
   "Stock": ""
 },
 {
   "Id": 17227,
   "SKU": "CHELABTE041",
   "Stock": ""
 }
]
skus = [{
   "Id": 17816,
   "SKU": "ANAMAS00041",
   "Stock": ""
 }]
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'abc.json'
creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
 
SPREADSHEET_ID = '1CHkQo1hxYcy1kJgQNHuQxDQIWldZIachwPv08nU84FE'
 
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
     
#SKU
for sku in skus2:
     params2={
           'code': sku['SKU'],
           'limit': 2
           }
     #Peticion a la API
     response = requests.get(url=url, headers=headers, params=params2)
     json_response = response.json()
     
      #Sacar la cantidad de stock 
     for item in json_response['items']:
        quantity = item['quantity']
        print(quantity)
        sku['Stock'] = quantity
        
        
end_time = time.time()  # Tiempo de finalización de la ejecución

execution_time = end_time - start_time
print(execution_time)

print(skus2)
                                