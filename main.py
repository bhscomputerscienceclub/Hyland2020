import algorithm as al
import weathertest as wt
import csv

cityname = raw_input("What is the (city, state) you're in? ")
g = wt.getloc(cityname)
fcc = wt.fcur(g,int(wt.time.time()))
print("{}{}{}{}".format(fcc.temperature,fcc.windSpeed,fcc.humidity,wt.time.ctime(fcc.time)))


with open('data.csv', 'w', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	tempBorders = np.array([spamreader[0])
	lowCounterBoi = spamreader[1][0]
	medCounterBoi = spamreader[1][1]
	highCounterBoi = spamreader[1][2]
	tempOfTheDay = fcc.temperature
		
	out = algo(tempBorders,lowCounterBoi,medCounterBoi,highCounterBoi,tempOfTheDay)
	
	
	writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	
	tempBorders = out[0]
	lowCounterBoi=out[1]
	medCounterBoi=out[2]
	highCounterBoi=out[3]
	
	writer.writerow([tempBorders])
	writer.writerow([lowCounterBoi,medCounterBoi,highCounterBoi])
