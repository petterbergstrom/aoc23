# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:27:22 2023

@author: PBERGS14
"""

def isDigit(char):
    return char.isdigit()


def getCalVal(row):
    result = list(filter(isDigit, row))
    return int(result[0] + result[-1])


with open('input.txt.txt', mode='r') as file:
    lines = file.readlines()
    calVals = list(map(getCalVal,lines))
    sumofCalVals =sum(calVals)
