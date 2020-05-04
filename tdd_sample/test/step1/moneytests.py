#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from src.step1 import dollar

#python -m unittest test.step1.moneytests.MoneyTest

class MoneyTest(unittest.TestCase):
    """Moneyクラスのテスト"""
    def test_multiplication(self):
        """テスト"""
        five = dollar.Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount, "amount expected 10")
