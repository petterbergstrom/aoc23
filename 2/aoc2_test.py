# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:22:54 2023

@author: PBERGS14
"""

import unittest
import aoc2

class TestAoc2(unittest.TestCase):
    
    def testnrOfColor(self):
        "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        self.assertEqual(aoc2.nrOfColor("3 blue, 4 red", "blue"), 3)
        self.assertEqual(aoc2.nrOfColor("3 blue, 4 red", "red"), 4)
        self.assertEqual(aoc2.nrOfColor("3 blue, 4 red", "green"), 0)
 
        self.assertEqual(aoc2.nrOfColor("1 red, 2 green, 6 blue", "blue"), 6)
        self.assertEqual(aoc2.nrOfColor("1 red, 2 green, 6 blue", "red"), 1)
        self.assertEqual(aoc2.nrOfColor("1 red, 2 green, 6 blue", "green"), 2)

        self.assertEqual(aoc2.nrOfColor("2 green", "blue"), 0)
        self.assertEqual(aoc2.nrOfColor("2 green", "red"), 0)
        self.assertEqual(aoc2.nrOfColor("2 green", "green"), 2)
        
        self.assertNotEqual(aoc2.nrOfColor("2 green", "blue"), 1)
        self.assertNotEqual(aoc2.nrOfColor("2 green", "red"), 1)
        self.assertNotEqual(aoc2.nrOfColor("2 green", "green"), 1)


    def testMakePossibleDraw(self):
        game = aoc2.Sample(0,0,0)
        self.assertEqual(game.green,0)
        self.assertEqual(game.blue,0)
        self.assertEqual(game.red,0)
        game.makePossibleDraw(aoc2.Sample(2,3,4))
        self.assertEqual(game.green,2)
        self.assertEqual(game.blue,3)
        self.assertEqual(game.red,4)
        game.makePossibleDraw(aoc2.Sample(3,4,5))
        self.assertEqual(game.green,3)
        self.assertEqual(game.blue,4)
        self.assertEqual(game.red,5)
        game.makePossibleDraw(aoc2.Sample(1,1,1))
        self.assertEqual(game.green,3)
        self.assertEqual(game.blue,4)
        self.assertEqual(game.red,5)
        
    def testPowerOfGame(self):
        self.assertEqual(aoc2.makePossibleGame("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green").powerOfGame(), 48)
        self.assertEqual(aoc2.makePossibleGame("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue").powerOfGame(), 12)
        self.assertEqual(aoc2.makePossibleGame("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red").powerOfGame(), 1560)
        self.assertEqual(aoc2.makePossibleGame("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red").powerOfGame(), 630)
        self.assertEqual(aoc2.makePossibleGame("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green").powerOfGame(), 36)

    def testIsPossibleGame(self):
        self.assertTrue(aoc2.isOkGame("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", aoc2.theBag))
        self.assertTrue(aoc2.isOkGame("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", aoc2.theBag))
        self.assertFalse(aoc2.isOkGame("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", aoc2.theBag))
        self.assertFalse(aoc2.isOkGame("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", aoc2.theBag))
        self.assertTrue(aoc2.isOkGame("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", aoc2.theBag))
        
    
if __name__ == '__main__':
    unittest.main()        