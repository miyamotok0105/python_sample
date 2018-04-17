# -*- coding: utf-8 -*-
from hoge import Hoge
import unittest

class TestHoge1(unittest.TestCase):

    def setUp(self):
        self.hoge = Hoge(1)

    def test_type(self):
        self.assertIsInstance(self.hoge, Hoge)

    def test_val(self):
        self.assertEqual(self.hoge.val, 1)

        self.hoge.update('hoge')
        self.assertEqual(self.hoge.val, 'hige')

if __name__ == '__main__':
    unittest.main()

