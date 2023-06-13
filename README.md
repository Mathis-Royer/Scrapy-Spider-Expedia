# Scrapy-Spider-Expedia
Projet de scraping du site web "http://expedia.fr/Flights-Search" utilisant le framework Scrapy.


## Installation des modules

pour une installation correct de scrapy :
```bash
pip3 uninstall lxml
pip3 install lxml --no-cache-dir
```
```bash
pip3 install scrapy
pip3 install scrapy scrapy-playwright : pour les page javascript
playwright install
```



## Settings.py

Modification déjà effectuée dans le fichier settings.py

```python
ROBOTSTXT_OBEY = False
```
Pour l'utilisation de playxright :
```python
DOWNLOAD HANDLERS = {
	"http": "scrapy playwright. handler. ScrapyPlaywrightDownloadHandler"
	"https": "scrapy playwright.handler .ScrapyPlaywrightDownloadHandler"
	}

	TWISTED_REACTOR = « twisted.internet.asyncioreactor.AsyncioSelectorReactor" 
```



## Execution
Éxécuter simplement le fichier main_expedia.py ainsi :
```bash
python3 main_expedia.py
```
Et complété les informations demandées de cette manière :
```python
=========================================================================
====    origin      = Paris 
====    destination = Montpellier
====    depart_date = 29/06/2023
====    return_date = 07/07/2023
=========================================================================
```

Le fichier main_expedia.py executera ensuite cette commande afin de retourner un le resulat dans un fichier au format json (qui peut être modifier au format csv si besoin) :
```bash
scrapy crawl expedia_spider -o output.json -a origin='+origin+' -a destination='+destination+' -a depart_date='+depart_date+' -a return_date='+return_date+' --nolog
```



## Resultats
```json
[
{"Flight_number": "", "Origin": "MPL", "Destination": "ORY", "Departure_time": "07 h 50", "Arrival_time": "09 h 20", "comfort_title": "", "price": "67 €"},
{"Flight_number": "", "Origin": "MPL", "Destination": "ORY", "Departure_time": "09 h 00", "Arrival_time": "10 h 30", "comfort_title": "", "price": "84 €"},
{"Flight_number": "", "Origin": "MPL", "Destination": "ORY", "Departure_time": "18 h 20", "Arrival_time": "19 h 50", "comfort_title": "", "price": "95 €"},
{"Flight_number": "", "Origin": "MPL", "Destination": "ORY", "Departure_time": "07 h 50", "Arrival_time": "09 h 20", "comfort_title": "", "price": "107 €"},
{"Flight_number": "", "Origin": "MPL", "Destination": "CDG", "Departure_time": "06 h 00", "Arrival_time": "07 h 30", "comfort_title": "", "price": "139 €"},
{"Flight_number": "", "Origin": "ORY", "Destination": "MPL", "Departure_time": "07 h 05", "Arrival_time": "08 h 25", "comfort_title": "", "price": "85 €"},
{"Flight_number": "", "Origin": "ORY", "Destination": "MPL", "Departure_time": "16 h 10", "Arrival_time": "17 h 30", "comfort_title": "", "price": "113 €"},
{"Flight_number": "", "Origin": "ORY", "Destination": "MPL", "Departure_time": "07 h 05", "Arrival_time": "08 h 25", "comfort_title": "", "price": "117 €"},
{"Flight_number": "", "Origin": "ORY", "Destination": "MPL", "Departure_time": "18 h 30", "Arrival_time": "19 h 50", "comfort_title": "", "price": "145 €"},
{"Flight_number": "", "Origin": "CDG", "Destination": "MPL", "Departure_time": "07 h 50", "Arrival_time": "09 h 15", "comfort_title": "", "price": "195 €"},
{"Flight_number": "", "Origin": "CDG", "Destination": "MPL", "Departure_time": "21 h 15", "Arrival_time": "22 h 40", "comfort_title": "", "price": "266 €"},
{"Flight_number": "", "Origin": "CDG", "Destination": "MPL", "Departure_time": "18 h 35", "Arrival_time": "20 h 00", "comfort_title": "", "price": "341 €"},
{"Flight_number": "", "Origin": "CDG", "Destination": "MPL", "Departure_time": "13 h 15", "Arrival_time": "14 h 40", "comfort_title": "", "price": "611 €"}
]
```
