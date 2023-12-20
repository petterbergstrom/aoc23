# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:22:26 2023

@author: PBERGS14
"""

import unittest
import aoc3

testRows = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


class TestAoc3(unittest.TestCase):
    
    def testIsAdjacentVertcally(self):
        reader = aoc3.SchematicReader(10)
        self.assertTrue(reader.isAdjacentVertcally(0, 2, reader.emptyRow(), "...*......"))
        self.assertFalse(reader.isAdjacentVertcally(5, 7, reader.emptyRow(), "...*......"))
        self.assertFalse(reader.isAdjacentVertcally(7, 9, reader.emptyRow(), "...*......"))
        self.assertTrue(reader.isAdjacentVertcally(7, 9, reader.emptyRow(), ".........u"))
    
        self.assertTrue(reader.isAdjacentVertcally(7, 9, reader.emptyRow(), ".........u"))
    
    def testIsAdjacentHorizontally(self):
        reader = aoc3.SchematicReader(10)
        self.assertFalse(reader.isAdjacentHorizontally("467..114..", 0, 2))
        self.assertFalse(reader.isAdjacentHorizontally("467..114..", 5, 7))
        self.assertTrue(reader.isAdjacentHorizontally("617*......", 0, 2))
        
    def testFaults(self):
        reader = aoc3.SchematicReader(141)
        prevRow = "..............124..*........49......*..........200.........162....+.....................914..........461......./....%.................=.....\n"
        currRow = "..808.......=......363........*......27....397.........107...*.......739+....232....+........68*395.................322..166+...=.......471.\n"
        nextRow = "...........465..............893..355..........*....70......963................*..133..........................................419.499.......\n"
        self.assertFalse(reader.isAdjacentHorizontally(currRow, 138, 140));
        self.assertFalse(reader.isAdjacentVertcally(138,140,prevRow,nextRow))
        
    def testGetRowMaches(self):
        reader = aoc3.SchematicReader(10)
        
        row = "467..114.."
        matches = reader.getRowMaches(row)
        self.assertIn((467,0,2), matches)
        self.assertIn((114,5,7), matches)
        
        row = "...*......"
        matches = reader.getRowMaches(row)
        self.assertEqual(len(matches),0)
        
        row = "..35..633.."
        matches = reader.getRowMaches(row)
        self.assertIn((35,2,3), matches)
        self.assertIn((633,6,8), matches)
     
    # def testTestRows(self):
    #     reader = aoc3.SchematicReader(10)
    #     lines = testRows.split('\n')
    #     for l in lines:
    #         reader.parse(l)
    #     reader.parse(reader.emptyRow())
    #     self.assertEqual(reader.checksum,4361)
            
    # def testFindGears(self):
        
    #     cogginator = aoc3.Cogginator(testRows)
    #     gears= cogginator.findGears()
    #     print(gears)
    #     self.assertEqual(len(gears), 2)
        
    def testGetRatios(self):
        cogginator = aoc3.Cogginator(testRows)
        
        self.assertEqual(cogginator.getRatios(), 467835)
        
    
if __name__ == '__main__':
    unittest.main()       
    
    
    

