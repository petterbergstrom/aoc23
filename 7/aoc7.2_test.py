# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 08:25:31 2023

@author: PBERGS14
"""

import unittest
import aoc7_2
import functools
import enum

denominations = "AKQJT98765432"


testHands="""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

class TestAoc5(unittest.TestCase):
    
    
    def testCompareCards(self):
        self.assertEqual(aoc7_2.compareCards('A', 'K'), -1)
        self.assertEqual(aoc7_2.compareCards('A', '2'), -1)
        self.assertEqual(aoc7_2.compareCards('K', 'A'), 1)
        self.assertEqual(aoc7_2.compareCards('2', 'A'), 1)
        self.assertEqual(aoc7_2.compareCards('2', '2'), 0)
    
    def testSortHand(self):
        self.assertEqual(sorted("T55J5", key=functools.cmp_to_key(aoc7_2.compareCards)),list("T555J"))
        self.assertEqual(sorted("T55J5", key=aoc7_2.cardsKey),list("T555J"))
            
    def testHandTypes(self):
        self.assertEqual(aoc7_2.HandType.findType("AAAAA"),aoc7_2.HandType.FIVEOFAKIND )
        self.assertEqual(aoc7_2.HandType.findType("AA8AA"),aoc7_2.HandType.FOUROFAKIND )
        self.assertEqual(aoc7_2.HandType.findType("23332"),aoc7_2.HandType.FULLHOUSE )
        self.assertEqual(aoc7_2.HandType.findType("TTT98"),aoc7_2.HandType.THREEOFAKIND )
        self.assertEqual(aoc7_2.HandType.findType("23432"),aoc7_2.HandType.TWOPAIR )
        self.assertEqual(aoc7_2.HandType.findType("A23A4"),aoc7_2.HandType.ONEPAIR )
        self.assertEqual(aoc7_2.HandType.findType("23456"),aoc7_2.HandType.HIGHCARD )
        self.assertEqual(aoc7_2.HandType.findType("QJJQ2"),aoc7_2.HandType.FOUROFAKIND )
        self.assertEqual(aoc7_2.HandType.findType("JJJJJ"),aoc7_2.HandType.FIVEOFAKIND )
        
    def testHandComparation(self):
        lines = testHands.splitlines()
        hands = list(map(lambda hand: aoc7_2.Hand(hand.split()[0],int(hand.split()[1])), lines))
        self.assertLess(hands[1], hands[4])
        
        
        self.assertLess(hands[0], hands[1])
        self.assertLess(hands[0], hands[2])
        self.assertLess(hands[0], hands[3])
        self.assertLess(hands[0], hands[4])
        
        self.assertLess(aoc7_2.Hand("JKKK2", 0),aoc7_2.Hand("QQQQ2", 0))

        
        sortedHands = sorted(hands)
        print(sortedHands)
        self.assertEqual(hands[0], sortedHands[0])
        self.assertEqual(hands[2], sortedHands[1])
        self.assertEqual(hands[1], sortedHands[2])
        self.assertEqual(hands[4], sortedHands[3])
        self.assertEqual(hands[3], sortedHands[4])

   
     
if __name__ == '__main__':
   unittest.main()     