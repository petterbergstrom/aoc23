# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:19:37 2023

@author: PBERGS14
"""

import re
from typing import List

class Sample:

    
    def __init__(self,green,blue,red):
        self.green = green
        self.blue = blue
        self.red = red
    
    def isPossibleDraw(self, green, blue, red)->bool:
        return self.green >= green and self.blue >= blue and self.red >= red
    
    def isPossibleGame(self,draws:List['Sample'])->bool:
        for draw in draws:
            if(not self.isPossibleDraw(draw.green, draw.blue, draw.red)):
                return False
        return True
    
    def makePossibleDraw(self, draw : 'Sample'):
        if self.green < draw.green:
            self.green = draw.green
        if self.blue < draw.blue:
            self.blue = draw.blue
        if self.red < draw.red:
            self.red = draw.red
            
    def powerOfGame(self)->int:
        return self.green*self.blue*self.red
    
    def __str__(self):
        return "[r:{red},g:{green},b:{blue}]".format(red=self.red,green=self.green,blue=self.blue)
    

def nrOfColor(draw,color):
    match = re.search("(\d*) "+color,draw)
    if match == None:
            return 0
        
    return int(match.group(1))
            
    
def isOkGame(row, game):
    match = re.search("Game (\d*):(.*)",row)
    drawsString = match.group(2)
    listofDraws = list(re.split(";", drawsString))
    draws = list()
    for drawString in listofDraws:
        blue = nrOfColor(drawString, "blue")
        red = nrOfColor(drawString, "red")
        green = nrOfColor(drawString, "green")
        draws.append(Sample(green,blue,red))
        
    return game.isPossibleGame(draws)
    
def makePossibleGame(row)->Sample:
    match = re.search("Game (\d*):(.*)",row)
    drawsString = match.group(2)
    listofDraws = list(re.split(";", drawsString))
    game = Sample(0, 0, 0)
    for drawString in listofDraws:
        blue = nrOfColor(drawString, "blue")
        red = nrOfColor(drawString, "red")
        green = nrOfColor(drawString, "green")
        game.makePossibleDraw(Sample(green,blue,red))
    return game

theBag = Sample(13, 14, 12)

with open('input', mode='r') as file:
    lines = file.readlines()
    total = 0
    for i in range(len(lines)):
        line = lines[i]
        if(isOkGame(line, theBag)):
            """list is zeroindexed"""
            total = total + i + 1 
    print('part1:'+str(total))
    file.close()
    
with open('input', mode='r') as file:
    lines = file.readlines()
    totalPower = 0
    for line in lines:
        game = makePossibleGame(line)
        totalPower += game.powerOfGame()
    print('part2:'+str(totalPower))
    file.close()
    
