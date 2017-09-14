#!/usr/bin/env python
# -*- coding: utf-8 -*-
from simple_delete import rm

import os.path
import tempfile
import unittest


class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp-testfile")
    # print(tmpfilepath)

    def setUp(self):
        with open(self.tmpfilepath, "a") as f:
            f.write("Delete me!")
        
    def test_rm(self):
        # remove the file
        rm(self.tmpfilepath)
        # test that it was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")

if __name__ == '__main__':
    rt = RmTestCase()
    rt.setUp()
    rt.test_rm()
    