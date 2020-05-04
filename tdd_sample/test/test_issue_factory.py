#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

from src.issue_factory import IssueFactory

#python -m unittest
#python -m unittest test.test_issue_factory.TestIssueFactory


class TestIssueFactory(unittest.TestCase):
    def setUp(self):
        self.issue_factory = IssueFactory()

    def test_create_single_line(self):
        result = self.issue_factory.create("質問", "回答")
        expect_result = "### Question\n質問" + "\n\n### Answer\n回答"
        self.assertEqual(result, expect_result)

    def test_create_multiline_line(self):
        result = self.issue_factory.create("質問\n2行目", "回答")
        expect_result = "### Question\n質問\n2行目" + "\n\n### Answer\n回答"
        self.assertEqual(result, expect_result)


if __name__ == '__main__':
    unittest.main()

