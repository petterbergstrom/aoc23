# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:23:21 2023

@author: PBERGS14
"""

import unittest
import prog

class TestConversions(unittest.TestCase):
    
    def testMapLitteralToDigit(self):
        self.assertEqual(prog.mapLitteralToDigit("one"), "1")
        self.assertEqual(prog.mapLitteralToDigit("two"), "2")
        self.assertEqual(prog.mapLitteralToDigit("three"), "3")
        self.assertEqual(prog.mapLitteralToDigit("four"), "4")
        self.assertEqual(prog.mapLitteralToDigit("five"), "5")
        self.assertEqual(prog.mapLitteralToDigit("six"), "6")
        self.assertEqual(prog.mapLitteralToDigit("seven"), "7")
        self.assertEqual(prog.mapLitteralToDigit("eight"), "8")
        self.assertEqual(prog.mapLitteralToDigit("nine"), "9")
        self.assertEqual(prog.mapLitteralToDigit("onetwothreefourfivesixseveneightnine"), "123456789")
    
    def testCalVals(self):
        for calVal in prog.calVals:
            self.assertLessEqual(calVal, 99)
            self.assertGreaterEqual(calVal, 10)
            
            
    def testGetCalVals(self):
   
        self.assertEqual(prog.getCalVal("1abc2"), 12)
        self.assertEqual(prog.getCalVal("pqr3stu8vwx"), 38)
        self.assertEqual(prog.getCalVal("a1b2c3d4e5f"), 15)
        self.assertEqual(prog.getCalVal("treb7uchet"), 77)    
        
        self.assertEqual(prog.getCalVal("two1nine"), 29)
        self.assertEqual(prog.getCalVal("eightwothree"), 83)
        self.assertEqual(prog.getCalVal("abcone2threexyz"), 13)
        self.assertEqual(prog.getCalVal("xtwone3four"), 24)
        self.assertEqual(prog.getCalVal("4nineeightseven2"), 42)
        self.assertEqual(prog.getCalVal("zoneight234"), 14)
        self.assertEqual(prog.getCalVal("7pqrstsixteen"), 76)
        
if __name__ == '__main__':
    unittest.main()        