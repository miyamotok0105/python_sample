#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

from src.fizz_buss import FizzBuzz

#python -m unittest
#python -m unittest test.test_fizz_buss.TestFizzBuzz.test_normal



class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fb = FizzBuzz()

    def test_normal(self):
        self.assertEqual(self.fb.execute(1), "1")
        self.assertEqual(self.fb.execute(2), "2")
        self.assertEqual(self.fb.execute(3), "Fizz")
        self.assertEqual(self.fb.execute(4), "4")
        self.assertEqual(self.fb.execute(5), "Buzz")
        self.assertEqual(self.fb.execute(6), "Fizz")
        self.assertEqual(self.fb.execute(9), "Fizz")
        self.assertEqual(self.fb.execute(15), "FizzBuzz")
        self.assertEqual(self.fb.execute(30), "FizzBuzz")


    # def test_normal2(self):
    #     fb = FizzBuzz()
    #     self.assertEqual(fb.execute(2), 1)


if __name__ == '__main__':
    unittest.main()

