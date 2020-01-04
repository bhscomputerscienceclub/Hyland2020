import algorithm as al
import weathertest as wt
import numpy as np
import csv

cityname = '44122 us' #input("What is the (city, state) you're in? ")
g = wt.getloc(cityname)
time = int(wt.time.time())
fcc = wt.fcur(g,time)

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


if temp < tempBorders[0]:
	print('error too cold go get you nobel prize')
elif temp < tempBorders[1]:
	print('You need a winter coat, scarf, hat, gloves, and boots')
elif temp < tempBorders[2]:
	print("You should wear a jacket")
elif temp < tempBorders[3]:
	print('You should wear a t-shirt')
else:
	print("error too hot this computer shouldn't be working")

print("{}F {}MPH {}% {}".format(fcc.temperature,fcc.windSpeed,fcc.humidity*100,wt.time.ctime(fcc.time)))
	
with open('data.csv', 'a', newline='') as csvfile2:		
	writer = csv.writer(csvfile2, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
	writer.writerows(fcc._data.items())
	'''writer.writerow([time, g.lat, g.lng])#timeplac    w.writerows(somedict.items())e
	listWriter = csv.DictWriter('data.csv', fieldnames=fcc._data.keys(), delimiter=',', quotechar="'", quoting=csv.QUOTE_NONNUMERIC
    )
	for i in fcc._data:
		listwriter.writerow(i)#fcc'''
