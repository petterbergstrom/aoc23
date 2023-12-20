# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:35:16 2023

@author: PBERGS14
"""

class Span():
    destRangeStart:int = 0
    sourceRangeStart:int = 0
    rangeLenght:int = 0
    def __init__(self,destRangeStart:int, sourceRangeStart:int, rangeLenght:int):
        self.destRangeStart = int(destRangeStart)
        self.sourceRangeStart = int(sourceRangeStart)
        self.rangeLenght = int(rangeLenght)
        
    def __eq__(self, o):
        if(o==None):
            return False
        return  self.destRangeStart == o.destRangeStart and self.sourceRangeStart == o.sourceRangeStart and self.rangeLenght == o.rangeLenght
    
    def __str__(self):
        return "destRangeStart: {0} sourceRangeStart: {1} rangeLenght: {2}".format(self.destRangeStart,  self.sourceRangeStart, self.rangeLenght )

        
    def isInRange(self, sourceCategory:int)->bool:
        return sourceCategory >= self.sourceRangeStart  and sourceCategory <= self.sourceRangeStart + self.rangeLenght
    
    def isInRangeFromSpan(self, start: int, end:int):
        if(start < self.sourceRangeStart and end < self.sourceRangeStart ):
            return False
        if(start > self.sourceRangeStart + self.rangeLenght and end > self.sourceRangeStart + self.rangeLenght):
            return False
        return True
    
    def getOfSet(self, source:int)->int:
        return source-self.sourceRangeStart
        
    def getDestCategory(source:int, spans:['Span'])->int:
        for span in spans:    
            if(span.isInRange(source)):
                return span.destRangeStart + span.getOfSet(source)
        return source
    
    def getDestCategoriesFromSpan(start:int,end:int, spans:['Span'])->[int]:
        #relevantSpans:['Span'] = filter(lambda span: span.isInRangeFromSpan(start,end),spans)
        categories:[int]=[]
        for span in spans:
            # if(start < span.sourceRangeStart):
            #     categories.append(start)
            # if(end > span.sourceRangeStart + span.rangeLenght):
            #     #categories.append(span.sourceRangeStart + span.rangeLenght + 1)
            #     categories.append(end)
            # offset = span.getOfSet(start)
            # if offset > 0:
            #     categories.append(span.destRangeStart + offset)
            
            #if in range from span -> span.destRangeStart + offset
            if span.isInRangeFromSpan(start,end):
                if span.isInRange(start):
                    categories.append(span.destRangeStart + span.getOfSet(start))
                else:
                    categories.append(span.sourceRangeStart + span.rangeLenght)
        
        if(len(categories)==0):
            categories.append(start)
        return categories
        
    def getSpan(line:str)->'Span':
        segments= line.split()
        if(len(segments)!=3):
            return
        return Span(segments[0], segments[1], segments[2])
    
    
class Almanac():
    
    categories:dict[str, [Span]]= {}
    
    seeds:[int]=[]
    
    def parse(self,data:str):
        chunks = data.split('\n\n')
        for chunk in chunks:
            chunkParts = chunk.split(':')
            chunkName = chunkParts[0]
            chunkContent = chunkParts[1]
            if(chunkName=='seeds'):
                self.seeds = chunkContent.split()
            else:
                spans = []
                segmentLines = chunkContent.splitlines()
                for segmentLine in segmentLines:
                    span = Span.getSpan(segmentLine)
                    if span != None:
                        spans.append(Span.getSpan(segmentLine))
                self.categories[chunkName] = spans
    
    def getLocation(self,seed:int)->int:
        soil = self.getDestCategory("seed-to-soil map",seed)
        fertilizer = self.getDestCategory("soil-to-fertilizer map",soil)
        water = self.getDestCategory("fertilizer-to-water map",fertilizer)
        light = self.getDestCategory("water-to-light map",water)
        temperature = self.getDestCategory("light-to-temperature map",light)
        humidity = self.getDestCategory("temperature-to-humidity map",temperature)
        location = self.getDestCategory("humidity-to-location map",humidity)
        return location
    
    def getLocationFromSpan(self,start:int,end:int)->int:
        soils = self.getDestCategoryFromSpan("seed-to-soil map",start,end)
        locations  = []
        for soil in soils:
            fertilizer = self.getDestCategory("soil-to-fertilizer map",soil)
            water = self.getDestCategory("fertilizer-to-water map",fertilizer)
            light = self.getDestCategory("water-to-light map",water)
            temperature = self.getDestCategory("light-to-temperature map",light)
            humidity = self.getDestCategory("temperature-to-humidity map",temperature)
            locations.append(self.getDestCategory("humidity-to-location map",humidity))    
        print("getLocationFromSpan"+str(locations))
        return min(locations)
    
    def getDestCategory(self, categoryName:str, source:int)->int:
        return Span.getDestCategory(source, self.categories[categoryName])
    
    def getDestCategoryFromSpan(self, categoryName:str, start:int,end:int)->int:
        return Span.getDestCategoriesFromSpan(start, end, self.categories[categoryName])
    
    def getOptimalLocations(self)->int:
        locations:[int] = []
        for seed in self.seeds:
            locations.append(self.getLocation(int(seed)))
        return locations
    
    def getSeedRanges(self)->[(int,int)]:
        ranges = []
        for i in range(0,len(self.seeds),2):
            ranges.append((int(self.seeds[i]), int(self.seeds[i]) +int(self.seeds[i+1])-1 ))
        return ranges
    
    def getLowestOptimalLocation(self)->int:
        locations:[int] = []
        for seedRange in self.getSeedRanges():
            print(range(seedRange[0],seedRange[1]))
            locations.append(self.getLocationFromSpan(seedRange[0],seedRange[1]))
        print("getLowestOptimalLocation:"+ str(locations))
        return min(locations)
    
# with open('input', mode='r') as file:
#     lines = file.read()
#     a = Almanac()
#     a.parse(lines)
#     optimalLocations = a.getOptimalLocations()
#     print(min(optimalLocations))
#     print(a.getLowestOptimalLocation())
    
    #print("Upg1: %d" % lottery.getTotalScore(lines))
