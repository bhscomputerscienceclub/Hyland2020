import time
import csv
from darksky import forecast as fc
api_key = "d1407217196848e8bc7f7a2d815bafa6"
lat = 41.479309
lng = -81.497841


with open('ex.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    t=1577750400
    for i in range(75):
        
        fcc = fc(api_key, lat, lng,time = t, exclude = minutely, hourly, daily, alerts).currently
        spamwriter.writerow([fcc.temperature,fcc.humidity,fcc.windSpeed,fcc.apparentTemperature])
        t = t - 43200
        fcc = fc(api_key, lat, lng,time = t).currently
        spamwriter.writerow([fcc.temperature,fcc.humidity,fcc.windSpeed,fcc.apparentTemperature])
        t = t-216000
        print(i)

print(str('done'))