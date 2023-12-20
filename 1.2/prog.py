# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:27:22 2023

@author: PBERGS14
"""

def isDigit(char):
    return char.isdigit()

conversions = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
    }

def mapLitteralToDigit(row):
    if len(row) <= 0:
        return row
    for key in conversions:
        if row.startswith(key):
            remainder = row[1:]
            return conversions[key]+mapLitteralToDigit(remainder)
    return row[0]+mapLitteralToDigit(row[1:])

   

def getCalVal(row):
    rowPrime = mapLitteralToDigit(row)
    result = list(filter(isDigit, rowPrime))
    return int(result[0] + result[-1])


with open('input.txt.txt', mode='r') as file:
    lines = file.readlines()
    calVals = list(map(getCalVal,lines))
    sumofCalVals =sum(calVals)
    print(sumofCalVals)
