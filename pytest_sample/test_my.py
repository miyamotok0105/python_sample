# -*- coding: utf-8 -*-
#http://okamuuu.hatenablog.com/entry/2015/06/15/114757
#===========================
#sがあると結果が見れる
#py.test -s test_my.py
# collected 3 items                                                                                                                                              
# test_my.py [test_101]
# .[create_fixture]
# [test_102]
# .[test_103]
# .
#===========================
#sがないと結果があまり見れない
#py.test test_my.py

import pytest

# @pytest.fixture()
# @pytest.fixture(autouse=True)
#@pytest.fixture(autouse=True)にすると全部動く
@pytest.fixture(autouse=True, scope='module')
# @pytest.fixture(autouse=True, scope='class')
# @pytest.fixture(autouse=True, scope='session')
def create_fixture():
    print('[create_fixture]')

class TestMy(object):
    
    def test_101(self):
        print('[test_101]')
    #create_fixtureを引数に入れてるので動く
    def test_102(self, create_fixture):
        print('[test_102]')
    
    def test_103(self):
        print('[test_103]')


class TestMy200(object):
        
    def test_201(self):
        print('[test_201]')
        
    def test_202(self):
        print('[test_202]')
        
    def test_203(self):
        print('[test_203]')

