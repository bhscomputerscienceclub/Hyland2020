import algorithm as al
import weathertest as wt
import numpy as np
import csv

cityname = input("What is the (city, state) you're in? ")
g = wt.getloc(cityname)
fcc = wt.fcur(g,int(wt.time.time()))





with open('data.csv', 'r', newline='') as csvfile:
	arr=[]
	spamreader = csv.reader(csvfile, delimiter=',', quotechar="'",quoting= csv.QUOTE_NONNUMERIC)
	for i in spamreader:
		arr.append(i)
	
	tempBorders = arr[0]
	lowCounterBoi = int(arr[1][0])
	medCounterBoi = int(arr[1][1])
	highCounterBoi = int(arr[1][2])
	out = al.algo(tempBorders,lowCounterBoi,medCounterBoi,highCounterBoi,fcc)
temp = fcc.temperature
if fcc.temperature <tempBorders[0]:
	print('error too cold')
elif fcc.temperature

print("{}F {}MPH {}% {}".format(fcc.temperature,fcc.windSpeed,fcc.humidity*100,wt.time.ctime(fcc.time)))
	
with open('data.csv', 'w', newline='') as csvfile2:		
	writer = csv.writer(csvfile2, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
	tempBorders = out[0]
	lowCounterBoi=out[1]
	medCounterBoi=out[2]
	highCounterBoi=out[3]
	writer.writerow(tempBorders)
	writer.writerow([lowCounterBoi,medCounterBoi,highCounterBoi])
