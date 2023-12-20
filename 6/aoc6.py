# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:14:58 2023

@author: PBERGS14
"""
import math
import re
from functools import reduce

class Race():
    
    totalRaceTime:int = 0
    
    def __init__(self,totalRaceTime:int):
        self.totalRaceTime = totalRaceTime
    
    def getDistance(self,time:int):
        return (self.totalRaceTime - time)*time
    
    def getOptimalChargetTime(self)->int:
        return math.floor(self.totalRaceTime / 2)
    
    def getChargeTimes(self, distance:int)->(float,float):
        base = self.totalRaceTime / 2
        diff = math.sqrt(self.totalRaceTime*self.totalRaceTime - 4 * distance)/2
        return ((base-diff), (base+diff))
    
    def getBetterChargeTimes(self, distance:int)->[int]:
        chargeTimes = self.getChargeTimes(distance)
        betterChargeTimes = []
        for i in range(math.ceil(chargeTimes[0])-1,math.floor(chargeTimes[1])+1):
            if(self.getDistance(i)>distance):
                betterChargeTimes.append(i)
        return betterChargeTimes

pc = re.compile("(\d+)")

def getNumbers(numberString)->[int]:
    numbers:[int] = []
    for m in pc.findall(numberString):
        numbers.append(int(m))
    return numbers

with open('input', mode='r') as file:
    lines = file.read().splitlines()
    times= getNumbers(lines[0].split(':')[1])
    distances= getNumbers(lines[1].split(':')[1])
    
    numberOfBetterTimes:int = []
    for pos in range (len(times)):
        race = Race(times[pos])
        betterTimes = race.getBetterChargeTimes(distances[pos])
        print(str(distances[pos]) +":"+ str(times[pos]))
        print(str(betterTimes)+"="+str(len(betterTimes)))
        print(str(list(map(lambda x: race.getDistance(x),betterTimes))))
        numberOfBetterTimes.append(len(betterTimes))
        
    print("uppgift 1 " + str(reduce(lambda x,y: x*y, numberOfBetterTimes )))
        
    times2= int(lines[0].split(':')[1].replace(" ", ""))
    distances2=  int(lines[1].split(':')[1].replace(" ", ""))
   
    numberOfBetterTimes:int = []
    race = Race(times2)
    betterTimes = race.getBetterChargeTimes(distances2)
    print("uppgift 2 " + str(len(betterTimes))  
    