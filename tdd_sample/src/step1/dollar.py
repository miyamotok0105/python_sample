#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Dollar:
    def __init__(self, amount: int):
        """初期化"""
        self.amount = amount

    def times(self, multiplier: int):
        """通貨変換"""
        self.amount *= multiplier
