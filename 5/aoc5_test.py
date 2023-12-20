# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:41:56 2023

@author: PBERGS14
"""


import aoc5
import unittest
testLines="""50 98 2
52 50 48
"""

testInput="""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


class TestAoc5(unittest.TestCase):
    
    
    def testReadSpans(self):
        lines = testLines.splitlines()
        self.assertEqual(aoc5.Span.getSpan(lines[0]),aoc5.Span(50,98,2))
        self.assertEqual(aoc5.Span.getSpan(lines[1]),aoc5.Span(52,50,48))    
    
    def testParseAlmanac(self):
        a = aoc5.Almanac()
        a.parse(testInput)
        self.assertEqual(a.getDestCategory("seed-to-soil map", 79),81)
        self.assertEqual(a.getDestCategory("seed-to-soil map", 14),14)
        self.assertEqual(a.getDestCategory("seed-to-soil map", 55),57)
        self.assertEqual(a.getDestCategory("seed-to-soil map", 13),13)
    
    def testGetLocation(self):
        a = aoc5.Almanac()
        a.parse(testInput)
        self.assertEqual(a.getLocation(79),82)
        self.assertEqual(a.getLocation(14),43)
        self.assertEqual(a.getLocation(55),86)
        self.assertEqual(a.getLocation(13),35)
    
    def testSeedRanges(self):
        a = aoc5.Almanac()
        a.parse(testInput)
        ranges = a.getSeedRanges()
        self.assertEqual(len(ranges), 2)
        self.assertEqual(ranges[0], (79,79+14-1))
        self.assertEqual(ranges[1], (55,55+13-1))
    
    def testIsInRangeFromSpan(self):
        span = aoc5.Span(10, 5, 15)
        self.assertTrue(span.isInRangeFromSpan(5, 20))
        self.assertTrue(span.isInRangeFromSpan(5, 30))
        self.assertTrue(span.isInRangeFromSpan(0, 30))
        self.assertTrue(span.isInRangeFromSpan(20, 30))
        self.assertFalse(span.isInRangeFromSpan(0, 4))
        self.assertFalse(span.isInRangeFromSpan(21, 100))
        
    def testSeedToSoil(self):
        a = aoc5.Almanac()
        a.parse(testInput)
        spans = a.categories["seed-to-soil map"]
        self.assertEqual(min(aoc5.Span.getDestCategoriesFromSpan(79, 92, spans)),84)
        self.assertEqual(min(aoc5.Span.getDestCategoriesFromSpan(55, 67, spans)),84)
            
        
    def testGetDestCategoryFromSpan(self):
        a = aoc5.Almanac()
        a.parse(testInput)
        spans = a.categories["seed-to-soil map"]
        seedRanges = a.getSeedRanges()
        
        spans =  a.categories["humidity-to-location map"]
        self.assertEqual(min(aoc5.Span.getDestCategoriesFromSpan(46, 46, spans)),46)
        spans =  a.categories["temperature-to-humidity map"]
        self.assertEqual(min(aoc5.Span.getDestCategoriesFromSpan(45, 45, spans)),46)
        spans =  a.categories["light-to-temperature map"]
        self.assertEqual(min(aoc5.Span.getDestCategoriesFromSpan(77, 77, spans)),45)
        spans =  a.categories["water-to-light map"]
        self.assertEqual(min(aoc5.Span.getDestCategoriesFromSpan(84, 84, spans)),77)
        spans =  a.categories["fertilizer-to-water map"]
        self.assertEqual(min(aoc5.Span.getDestCategoriesFromSpan(84, 84, spans)),84)
        spans =  a.categories["soil-to-fertilizer map"]
        self.assertEqual(min(aoc5.Span.getDestCategoriesFromSpan(84, 84, spans)),84)
        spans =  a.categories["seed-to-soil map"]
        self.assertEqual(min(aoc5.Span.getDestCategoriesFromSpan(82, 82, spans)),84)
        
        self.assertEqual(min(aoc5.Span.getDestCategoriesFromSpan(79, 92, spans)),84)
        self.assertEqual(min(aoc5.Span.getDestCategoriesFromSpan(55, 67, spans)),84)

        
    # def testGetLowestOptimalLocation(self):
    #       a = aoc5.Almanac()
    #       a.parse(testInput)
    #       self.assertEqual(a.getLowestOptimalLocation(), 46)

    
if __name__ == '__main__':
   unittest.main()     