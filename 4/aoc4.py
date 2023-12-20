# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:18:21 2023

@author: PBERGS14
"""

import re
class Card:
    ownNumbers: [int] = []
    winningNumbers: [int] = []
    def __init__(self, ownNumbers:[int],winningNumbers:[int]):
        self.ownNumbers = ownNumbers;
        self.winningNumbers = winningNumbers

class Lottery:
    

    
    rowPattern = re.compile("Card\s+\d+\: ([\d\s]*)\|([\d\s]*)")
    numnberPattern = re.compile("(\d+)")
    def readRow(self, row:str)->Card:
        rowMatch = self.rowPattern.match(row)
        own = rowMatch.group(1)
        winning  = rowMatch.group(2)
        card =  Card([],[])
        for n in self.numnberPattern.findall(own):
           card.ownNumbers.append(int(n))
        for n in self.numnberPattern.findall(winning):
           card.winningNumbers.append(int(n))
        return card

    def findWinningNumbers(self,card:Card)->[int]:
        return list( set(card.ownNumbers) & set(card.winningNumbers) )
    
    def calculateScore(self,winningNumbers:[int]):
        if len(winningNumbers) == 0:
            return 0
        if len(winningNumbers) == 1:
            return 1
        return pow(2, len(winningNumbers)-1)
    
    def getCopiesOfCards(self, data:str)->[int]:
        lines = data.splitlines()
        cardCopies = [0]*len(lines)
        lines = data.splitlines()
        for i in range(len(lines)):
            line = lines[i]
            cardCopies[i] += 1
            matchesForCard = len(self.findWinningNumbers(self.readRow(line)))
           # print("Processing: %d m: %d r:%s " % (i+1, matchesForCard,range(min(len(lines)-1,i+1),max(len(lines)-1,i+matchesForCard+1))))
            for j in range(i+1,matchesForCard+i+1):
                cardCopies[j] += cardCopies[i]
           # for k in range(len(lines)):
                #print("[ %d ][ %d ]: %d" % (i+1, k+1, cardCopies[k]))
        return cardCopies
            
    
    def getTotalScore(self,data:str)->int:
        lines = data.splitlines()
        totalScore = 0 
        for i in range(len(lines)):
            totalScore += self.calculateScore(self.findWinningNumbers(self.readRow(lines[i])))
        return totalScore
        
with open('input', mode='r') as file:
    lines = file.read()
    lottery = Lottery()
    print("Upg1: %d" % lottery.getTotalScore(lines))
    print("Upg2: %d" % sum(lottery.getCopiesOfCards(lines)))