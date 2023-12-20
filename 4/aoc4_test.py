# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:33:17 2023

@author: PBERGS14
"""

import aoc4
import unittest
testLines="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
def isSameSet(a,b):
    return len(set(a)^set(b)) == 0

class TestAoc4(unittest.TestCase):
    
    
    def testReadRow(self):
        l = aoc4.Lottery()
        card1 = l.readRow("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
        self.assertEqual(card1.ownNumbers, [41,48,83,86,17] )
        self.assertEqual(card1.winningNumbers, [83,86,6,31,17,9,48,53] )
    
    def testWinningNUmbers(self):
        l = aoc4.Lottery()
        card2 = l.readRow("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
        self.assertTrue(isSameSet(l.findWinningNumbers(card2),[48, 83, 17, 86]))
        card3 = l.readRow("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19")
        self.assertTrue(isSameSet(l.findWinningNumbers(card3),[32,61]))
        card4 = l.readRow("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1")
        self.assertTrue(isSameSet(l.findWinningNumbers(card4),[1,21]))
        
        
    def testScore(self):
        lottery = aoc4.Lottery()
        lines = testLines.splitlines()
        self.assertEqual(lottery.calculateScore(lottery.findWinningNumbers(lottery.readRow(lines[0]))), 8)
        self.assertEqual(lottery.calculateScore(lottery.findWinningNumbers(lottery.readRow(lines[1]))), 2)    
        self.assertEqual(lottery.calculateScore(lottery.findWinningNumbers(lottery.readRow(lines[2]))), 2)
        self.assertEqual(lottery.calculateScore(lottery.findWinningNumbers(lottery.readRow(lines[3]))), 1)
        self.assertEqual(lottery.calculateScore(lottery.findWinningNumbers(lottery.readRow(lines[4]))), 0)
        self.assertEqual(lottery.calculateScore(lottery.findWinningNumbers(lottery.readRow(lines[5]))), 0)
    
    def testCopies(self):
        lottery = aoc4.Lottery()
        self.assertEqual(lottery.getCopiesOfCards(testLines), [1,2,4,8,14,1])
    
if __name__ == '__main__':
    unittest.main()     