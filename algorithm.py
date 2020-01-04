#ok this is the algorthm
import statistics
import random
import numpy as np
import weathertest as wt


def algo(tempBorders, lowCounterBoi, medCounterBoi, highCounterBoi, fcc):
    print("Hi! How was our advice to you today?")
    print("Was it 'Too Hot', 'Too Cold' or 'Just Right'?")
    tempFeeling = input()
    tempBorders = np.array(tempBorders)
    
    n = fcc.temperature+5*fcc.humidity**2-2*(fcc.windSpeed**(1/2))



    if(tempFeeling== "Too Cold"):
        nearestBorder = tempBorders[tempBorders < n].max()
        nearestIndex = np.where(tempBorders==nearestBorder)[0][0]
        if(nearestIndex == 1):
            tempBorders[nearestIndex] = (n - (nearestBorder))*(0.5**lowCounterBoi)+nearestBorder
            lowCounterBoi+=1
        elif(nearestIndex == 2):
            tempBorders[nearestIndex] = (n - (nearestBorder))*(0.5**medCounterBoi)+nearestBorder
            medCounterBoi+=1
        elif(nearestIndex == 3):
            tempBorders[nearestIndex] = (n - (nearestBorder))*(0.5**highCounterBoi)+nearestBorder
            highCounterBoi+=1
    elif(tempFeeling== "Too Hot"):
        nearestBorder = tempBorders[tempBorders > n].min()

        nearestIndex = np.where(tempBorders==nearestBorder)[0][0]

        if(nearestIndex == 1):
            tempBorders[nearestIndex] = nearestBorder - (nearestBorder - (n))*(0.5**lowCounterBoi)
            lowCounterBoi+=1
        elif(nearestIndex == 2):
            tempBorders[nearestIndex] = nearestBorder - (nearestBorder - (n))*(0.5**medCounterBoi)
            medCounterBoi+=1
        elif(nearestIndex == 3):
            tempBorders[nearestIndex] = nearestBorder- (nearestBorder - (n))*(0.5**highCounterBoi)
            highCounterBoi+=1
    elif(tempFeeling == "Just Right" and (tempFeeling >(tempBorders[1] and tempBorders[3]))):
        medCounterBoi+=1
        if(tempBorders[3] - n < n- tempBorders[1]):
            highCounterBoi+=1
        else:
            lowCounterBoi+=1
    else:
        print("invalid option")
    return [list(tempBorders),int(lowCounterBoi),int(medCounterBoi),int(highCounterBoi)]


if __name__ == "__main__":
    g = wt.getloc('Salt lake city, utah')
    fcc = wt.fcur(g,int(wt.time.time()))
    tempBorders = np.array([-450,15.00001,40.000001,70.000001,2000])
    lowCounterBoi = 0
    medCounterBoi = 0
    highCounterBoi = 0
    
    out = algo(tempBorders,lowCounterBoi,medCounterBoi,highCounterBoi,fcc)
    tempBorders = out[0]
    lowCounterBoi=out[1]
    medCounterBoi=out[2]
    highCounterBoi=out[3]

    print(fcc.temperature)
    print(fcc.temperature+5*fcc.humidity**2-2*(fcc.windSpeed**(1/2)))
    print(wt.time.ctime())
    print(lowCounterBoi+medCounterBoi+highCounterBoi)