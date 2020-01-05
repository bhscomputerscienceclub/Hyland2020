import algorithm as al
import weathertest as wt
import numpy as np
import csv


#read prev
#recomend + give weather
#write fcc + time place


def goread(cityname):
	out = []
	g = wt.getloc(cityname)
	time = int(wt.time.time())
	fcc = wt.fcur(g,time)
	fc = wt.fall(g,time)

	with open('data.csv', 'r', newline='') as csvfile:
		arr=[]
		spamreader = csv.reader(csvfile, delimiter=',', quotechar="'",quoting= csv.QUOTE_NONNUMERIC)
		for i in spamreader:
			arr.append(i)
		
		tempBorders = arr[0]

		temp = fcc.temperature

	#sunset = fc.sunsetTime

	if temp < tempBorders[0]:
		out.append('error too cold go get you nobel prize')
	elif temp < tempBorders[1]:
		out.append('Wear a winter coat, scarf, hat, gloves, and boots')
	elif temp < tempBorders[2]:
		out.append("Wear a light coat or jacket")
	elif temp < tempBorders[3]:
		out.append('Wear a jacket or long sleeved shirt')
	elif temp >= tempBorders[3]:
		out.append('Wear a T-shirt or tanktop')
	else:
		out.append("error too hot this computer shouldn't be working")

	#if(fcc.precipType == "rain"):
	#	out.append("It's raining, you should bring an umbrella or a rainjacket")

	#if(fcc.uvIndex >= 3):
	#T	out.append("You should wear sunscreen when going outside")

	#if((fcc.humidity <= .5 and temp >70) or temp >80):
		#out.append("It is hot outside, you should bring a waterbottle")
		
	#if(fcc.visibility == 0):
		#out.append("Be careful while driving")

	#out.append("{}F {}MPH {}% {}".format(fcc.temperature,fcc.windSpeed,fcc.humidity*100,wt.time.ctime(fcc.time)))
		
	with open('data.csv', 'a', newline='') as csvfile2:		
		writer = csv.writer(csvfile2, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
		writer.writerow([g.lat,g.lng,time])
		writer.writerows(fcc._data.items())
	return out

if __name__ == "__main__":
	cityname = input("What is the (city, state) you're in? ")
	g = wt.getloc(cityname)
	time = int(wt.time.time())
	fcc = wt.fcur(g,time)
	fc = wt.fall(g,time)