import os

print('=========================================================================')
origin = str(input('====    origin      = '))
destination = str(input('====    destination = '))
depart_date = str(input('====    depart_date = '))
return_date = str(input('====    return_date = '))
print('=========================================================================')

os.system('scrapy crawl expedia_spider -o output.json -a origin='+origin+' -a destination='+destination+' -a depart_date='+depart_date+' -a return_date='+return_date)

