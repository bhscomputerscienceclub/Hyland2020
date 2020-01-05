import algorithm as al
import weathertest as wt
import numpy as np
import csv

#read values fcc 
class Struct(object):
	def __init__(self, adict):
		self.__dict__.update(adict)
		for k, v in adict.items():
			if isinstance(v, dict):
				self.__dict__[k] = Struct(v)

def get_object(adict):
	return Struct(adict)


#fcc = wt.fcur(g,int(wt.time.time()))

with open('data.csv', 'r', newline='') as csvfile:
	arr=[]
	spamreader = csv.reader(csvfile, delimiter=',', quotechar="'", quoting= csv.QUOTE_NONNUMERIC)
	j = 2
	for i in spamreader:
		arr.append(i)
		
		j-=1
		if j == 0:
			break
	tempBorders = arr[0]
	lowCounterBoi = int(arr[1][0])
	medCounterBoi = int(arr[1][1])
	highCounterBoi = int(arr[1][2])
	fcc = {}
	for rows in spamreader:
		fcc.update({rows[0]:rows[1]})
	fcc = get_object(fcc)
	out = al.algo(tempBorders,lowCounterBoi,medCounterBoi,highCounterBoi,fcc)
	

print("{}F {}MPH {}% {}".format(fcc.temperature,fcc.windSpeed,fcc.humidity*100,wt.time.ctime(fcc.time)))
	
with open('data.csv', 'w', newline='') as csvfile2:		
	writer = csv.writer(csvfile2, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
	tempBorders = out[0]
	lowCounterBoi=out[1]
	medCounterBoi=out[2]
	highCounterBoi=out[3]
	writer.writerow(tempBorders)
	writer.writerow([lowCounterBoi,medCounterBoi,highCounterBoi])
