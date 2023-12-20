# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:07:07 2023

@author: PBERGS14
"""
import numpy as np
from enum import Enum
import functools

denominations = "AKQJT98765432"

def compareCards(a:str, b:str)->int:
    return np.sign(denominations.find(a) - denominations.find(b))

def cardsKey(a:str)->int:
    return denominations.find(a)

def compareCardsInHand(a:str,b:str)->int:
    firsta = a[0]
    a = a[1:]
    firstb = b[0]
    b = b[1:]
    comparation = compareCards(firsta,firstb)
    if(comparation == 0):
        return compareCardsInHand(a,b)
    return comparation

@functools.total_ordering
class HandType(Enum):
    FIVEOFAKIND = 7
    FOUROFAKIND = 6
    FULLHOUSE = 5
    THREEOFAKIND = 4
    TWOPAIR = 3
    ONEPAIR = 2
    HIGHCARD = 1
    UNKNOWN = -1
    
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    
    
    @classmethod
    def findType(cls,cards:str)->'HandType':
        sortedCards = sorted(cards,key=cardsKey)
        
        matchesInHand = []
        lastCard = "Joker"
        ofSame = 1
        for card in sortedCards:
            if(card == lastCard):
                ofSame += 1
            else:
                matchesInHand.append(ofSame)
                ofSame = 1
            lastCard = card
        matchesInHand.append(ofSame)
        matchesInHand.pop(0) #first element compares to "joker"
            
        if(5 in matchesInHand):
            return HandType.FIVEOFAKIND
        if(4 in matchesInHand):
            return HandType.FOUROFAKIND
        if(3 in matchesInHand and 2 in matchesInHand):
            return HandType.FULLHOUSE
        if(3 in matchesInHand):
            return HandType.THREEOFAKIND
        if(matchesInHand.count(2) == 2):
            return HandType.TWOPAIR
        if(matchesInHand.count(2) == 1):
            return HandType.ONEPAIR
        return HandType.HIGHCARD
    
@functools.total_ordering
class Hand:
    
    cards = ""
    handType:HandType = HandType.UNKNOWN
    bet = 0
    
    def __init__(self,cards:str, bet:int):
        self.cards = cards
        self.handType = HandType.findType(cards)
        self.bet = bet
    
    def _is_valid_operand(self, other):
        return (hasattr(other, "cards"))
      
    def __str__(self):
        return "Cards: '{cards}' {bet} type:{t}".format(cards=self.cards, bet=self.bet, t=self.handType)
    
    def __repr__(self):
        return "Cards: '{cards}' {bet} type:{t}".format(cards=self.cards, bet=self.bet, t=self.handType)
    
    
    def __eq__(self,other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.cards == other.cards
    
    def __lt__(self,other):
        if(self.handType == other.handType):
            return compareCardsInHand(self.cards, other.cards) > 0
        else:
            return self.handType < other.handType
    
with open('input', mode='r') as file:
    lines = file.read().splitlines()
    hands = list(map(lambda hand: Hand(hand.split()[0],int(hand.split()[1])), lines))
    hands = sorted(hands)
    winnings = 0
    for i in range(len(hands)):
        winnings += (i+1) * hands[i].bet
        
    print(str(hands))
    print("Uppgift 1:"+str(winnings))
        