from unittest import mock
 
def hoge():
    return fuga()
 
def fuga():
    return 'Here is Fuga!'
 
# fuga() を patch(mock化)
@mock.patch('__main__.fuga')
def test_hoge(mock_fuga):
    # mock の戻り値を設定
    mock_fuga.return_value = 'Here is Mock!'
 
    res = hoge()
    print(res)
 
if __name__ == '__main__':
    test_hoge()
    
