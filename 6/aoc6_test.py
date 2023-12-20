# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:35:22 2023

@author: PBERGS14
"""

import unittest
import aoc6

class TestAoc6(unittest.TestCase):
    
    def testGetDistance(self):
        race = aoc6.Race(7)
        self.assertEqual(race.getDistance(0), 0)
        self.assertEqual(race.getDistance(1), 6)
        self.assertEqual(race.getDistance(2), 10)
        self.assertEqual(race.getDistance(3), 12)
        self.assertEqual(race.getDistance(4), 12)
        self.assertEqual(race.getDistance(5), 10)
        self.assertEqual(race.getDistance(6), 6)
        self.assertEqual(race.getDistance(7), 0)
        
    def testGetBetterChargeTimes(self):
        race = aoc6.Race(7)
        self.assertEqual(race.getBetterChargeTimes(9), [2,3,4,5])
        race = aoc6.Race(15)
        self.assertEqual(len(race.getBetterChargeTimes(40)), 8)
        race = aoc6.Race(30)
        betterTimes:[int] = race.getBetterChargeTimes(200)
        self.assertEqual(len(betterTimes), 9)
    
if __name__ == '__main__':
    unittest.main()     