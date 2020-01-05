import time
import csv
from darksky import forecast as fc
import geocoder
#####fcc.temperature,fcc.humidity,fcc.windSpeed,fcc.apparentTemperature
lat = 41.479309
lng = -81.497841
def getloc(cityname):
    g = geocoder.osm(cityname)
    print(g.country)
    return(g)


def fcur (g,t):
    api_key = "d1407217196848e8bc7f7a2d815bafa6"
    fcc = fc(api_key, g.lat, g.lng,time = t,units = 'us').currently
    return fcc
def fall (g,t):
    api_key = "d1407217196848e8bc7f7a2d815bafa6"
    fa = fc(api_key, g.lat, g.lng,time = t,units = 'us')
    return fa
'''
with open('ex2.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    t=1577750400
    for i in range(1):  
        fcc = fcur('')
        spamwriter.writerow([fcc.temperature,fcc.humidity,fcc.windSpeed,fcc.apparentTemperature])
        t = t - 43200
        fcc = fcur('')
        spamwriter.writerow([fcc.temperature,fcc.humidity,fcc.windSpeed,fcc.apparentTemperature])
        t = t-216000
        print(i)'''
if __name__ == "__main__":
    g=getloc('44122, us')
    print(fcur(g, 1577750000))
    print(str('done'))

