# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:44:11 2023

@author: PBERGS14
"""
import re

class SchematicReader:
    
    rowMinusTwo =""
    rowMinusOne =""
    rowLength = 10
    
    def emptyRow(self)->str:
        return "".ljust(self.rowLength,'.')
    
    def __init__(self, rowLenght:int):
        self.rowMinusTwo = "".ljust(rowLenght-1,'.')+'\n'
        self.rowMinusOne = "".ljust(rowLenght-1,'.')+'\n'
        self.rowLength = rowLenght
    
    def isSymbol(self, char:chr)->bool:
        return not char.isdigit() and char != '.' and char != '\n'
    
    def isAdjacentHorizontally(self,row:str,start:int, end:int)->bool:
        isPreceded = False
        isSuperceded = False
        isPreceded = self.isSymbol(row[max(0,start-1)])
        isSuperceded = self.isSymbol(row[min(self.rowLength-1, end+1)])
        return isPreceded or isSuperceded
    
    def isAdjacentVertcally(self,start:int, end:int,previousRow:str, nextRow:str)->bool:
        isOnPreviousRow = False
        #print('0123456789')
        #print("previous:\n"+previousRow)
        for i in range(max(0,start-1),min(self.rowLength,end+2)):
            isOnPreviousRow = isOnPreviousRow or self.isSymbol(previousRow[i])
            #print(str(i)+":"+str(self.isSymbol(previousRow[i])))
        isOnNextRow = False
        #print("next:\n"+'0123456789')
        #print(nextRow)
        for i in range(max(0,start-1),min(self.rowLength,end+2)):
            isOnNextRow = isOnNextRow or self.isSymbol(nextRow[i])  
            #print(str(i)+":"+str(self.isSymbol(nextRow[i])))
        return isOnNextRow or isOnPreviousRow
        
    p = re.compile("(\d+)")
    
    def getRowMaches(self,row:str):
        numbersInRow = []
        for m in self.p.finditer(row):
            numbersInRow.append((int(m.group()),m.start(),m.end()-1))
        return numbersInRow
    

    
    checksum = 0
    rowNumber = 0

    def parse(self, row)->str:
        self.rowNumber+=1
        #print("row("+str(len(row))+"):"+row)
        assert(len(row) == self.rowLength)
        #print("rowMinusOne("+str(len(self.rowMinusOne))+"):"+self.rowMinusOne)
        
        debugStr = self.rowMinusOne
        matches = self.getRowMaches(self.rowMinusOne)
        matches.append(matches)
        for match in matches:
            #print("testing: "+ str(match))
            if(self.isAdjacentHorizontally(self.rowMinusOne, match[1], match[2]) or 
               self.isAdjacentVertcally(match[1], match[2], self.rowMinusTwo, row)):
                self.checksum += match[0]
                for i in range(match[1],match[2]):
                    debugStr = debugStr[:i] + 'T' + debugStr[i + 1:]
            else:
                for i in range(match[1],match[2]):
                    debugStr = debugStr[:i] + 'F' + debugStr[i + 1:]
        
        # Shift for comming calculations
        self.rowMinusTwo = self.rowMinusOne
        self.rowMinusOne = row
        return debugStr
    
class Cogginator:
    
    cogs = []
    allNumbers = []
    
    pc = re.compile("(\*)")
        
    def getCogs(self,row:str,rowNumber:int):
        rowCogs = []
        for m in self.pc.finditer(row):
            rowCogs.append((rowNumber,m.start()))
        return rowCogs
    
    def __init__(self, data: str):
        reader = SchematicReader(140)
        lines = data.splitlines()
        for i in range(len(lines)):
            line = lines[i]
            self.allNumbers.append(reader.getRowMaches(line))
            self.cogs.extend(self.getCogs(line, i))

    def findGears(self)->[((int,int,int),(int,int,int))]:
        gears = []
        
        for cog in self.cogs:
            numbers = []
            previousRowNumber = cog[0] - 1
            currentRowNumber = cog[0]
            nextRowNumber = cog[0] + 1
            col = cog[1]
            if(previousRowNumber>=0):
                numbers += filter(lambda number: (col>=number[1]-1) and (col<=number[2]+1), self.allNumbers[previousRowNumber])
            numbers += filter(lambda number: (col>=number[1]-1) and (col<=number[2]+1), self.allNumbers[currentRowNumber])
            if(nextRowNumber<len(self.allNumbers)):
                numbers += filter(lambda number: (col>=number[1]-1) and (col<=number[2]+1), self.allNumbers[nextRowNumber])
            if(len(numbers)==2):
                gears.append((numbers[0],numbers[1]))
                
        return gears
    
    def sumRationsOfGears(self,gears:[((int,int,int),(int,int,int))])->int:
        sumOfRatios = 0
        for gear in gears:
            sumOfRatios += gear[0][0]*gear[1][0]
        return sumOfRatios

    def getRatios(self)->int:
        return self.sumRationsOfGears(self.findGears())           
       
# with open('input', mode='r') as file:
#     with open('output', mode="w") as output:
#         lines = file.read().splitlines()
#         reader = SchematicReader(140)
#         for line in lines:
#             debug = reader.parse(line)
#             output.write(debug)
#         reader.parse(reader.emptyRow())
#         print('part1:'+str(reader.checksum))
#         file.close()

# with open('input', mode='r') as file:
#     with open('output', mode="r") as output:
#         lines = file.readlines()
#         print(output.readline())
#         for line in lines:
#             print(line)
#             print(output.readline())
#             input()
            

with open('input', mode='r') as file:
    lines = file.read()
    cogginator = Cogginator(lines)
    print(cogginator.getRatios())
