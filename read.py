import algorithm as al
import weathertest as wt
import numpy as np
import csv

cityname = input("What is the (city, state) you're in? ")
g = wt.getloc(cityname)
time = int(wt.time.time())
fcc = wt.fcur(g,time)
fc = wt.fall(g,time)

#read prev
#recomend + give weather
#write fcc + time place



with open('data.csv', 'r', newline='') as csvfile:
	arr=[]
	spamreader = csv.reader(csvfile, delimiter=',', quotechar="'",quoting= csv.QUOTE_NONNUMERIC)
	for i in spamreader:
		arr.append(i)
	
	tempBorders = arr[0]

	temp = fcc.temperature

#sunset = fc.sunsetTime

if temp < tempBorders[0]:
	print('error too cold go get you nobel prize')
elif temp < tempBorders[1]:
	print('Wear a winter coat, scarf, hat, gloves, and boots')
elif temp < tempBorders[2]:
	print("Wear a light coat or jacket")
elif temp < tempBorders[3]:
	print('Wear a jacket or long sleeved shirt')
elif temp >= tempBorders[3]:
	print('Wear a T-shirt or tanktop')
else:
	print("error too hot this computer shouldn't be working")

if(fcc.precipType == "rain"):
	print("It's raining, you should bring an umbrella or a rainjacket")

if(fcc.uvIndex >= 3):
	print("You should wear sunscreen when going outside")

if((fcc.humidity <= .5 and temp >70) or temp >80):
	print("It is hot outside, you should bring a waterbottle")
	
if(fcc.visibility == 0):
	print("Be careful while driving")

print("{}F {}MPH {}% {}".format(fcc.temperature,fcc.windSpeed,fcc.humidity*100,wt.time.ctime(fcc.time)))
	
with open('data.csv', 'a', newline='') as csvfile2:		
	writer = csv.writer(csvfile2, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
	writer.writerows(fcc._data.items())
	'''writer.writerow([time, g.lat, g.lng])#timeplac    w.writerows(somedict.items())e
	listWriter = csv.DictWriter('data.csv', fieldnames=fcc._data.keys(), delimiter=',', quotechar="'", quoting=csv.QUOTE_NONNUMERIC
    )
	for i in fcc._data:
		listwriter.writerow(i)#fcc'''
