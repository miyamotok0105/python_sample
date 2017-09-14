#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simple_delete import rm

import mock
import unittest

class RmTestCase(unittest.TestCase):
    
    @mock.patch('simple_delete.os')
    def test_rm(self, mock_os):
        rm("any path")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")

if __name__ == '__main__':
    rt = RmTestCase()
    rt.test_rm()
    