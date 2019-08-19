#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:59:24 2019

@author: igor
"""

import unittest

import knight as k

class TestNavigator(unittest.TestCase):
    def test_get_best_path(self):
        b = k.Board()
        n = k.Navigator(b, k.Knight(b))
        self.assertEqual(n.get_best_path('A1', 'H8'), 'A1 C2 E3 G4 E5 G6 H8')
        self.assertEqual(n.get_best_path('A11', 'H8'), '')
        self.assertEqual(n.get_best_path('A1', ''), '')
        self.assertEqual(n.get_best_path('A1', 'Q2'), '')

    def test_validate_input(self):
        b = k.Board()
        n = k.Navigator(b, k.Knight(b))
        self.assertEqual(n.validate_input('A1'), True)
        self.assertEqual(n.validate_input('A11'), False)
        self.assertEqual(n.validate_input('Z1'), False)
        self.assertEqual(n.validate_input(''), False)
        self.assertEqual(n.validate_input('c3'), True)


class TestBoard(unittest.TestCase):
    def test_is_inside(self):
        b = k.Board()
        self.assertEqual(b.is_inside(1,3), True)
        self.assertEqual(b.is_inside(1,9), False)
        self.assertEqual(b.is_inside(0,5), False)
        
if __name__ == '__main__':
    unittest.main()