import requests
 
def get_resp(url):
 
    resp = requests.get(url)
    if resp.status_code != 200:
        print('Get Data Failed...(error code : {})'.format(resp.status_code))
        raise
 
    return resp.json()
 
def main():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
 
    actual = get_resp(url)
    print(actual)
 
if __name__ == '__main__':
    main()
    
