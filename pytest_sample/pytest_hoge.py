# -*- coding: utf-8 -*-
from hoge import Hoge
import pytest

@pytest.fixture()
def create_hoge():
    return Hoge(1)

class TestHoge1(object):
    
    def test_101(self):
        print('[test_101]')

    def test_102(self, create_hoge):
        print('[test_102]')
    
    def test_type(self, create_hoge):
        assert isinstance(hoge, Hoge)


# class TestHoge1(object):

#     @pytest.fixture()
#     def create_hoge():
#         return Hoge(1)

#     def test_type(self, create_hoge):
#         assert isinstance(hoge, Hoge)

#     def test_val(self, create_hoge):

#         assert hoge.val == 1

#         hoge.update('hoge')
#         # assert hoge.val == 'hige'

# if __name__ == '__main__':
#     pytest.main()

