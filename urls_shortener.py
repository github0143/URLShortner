import requests
from selenium import webdriver
import time
class urlshorten:
    def __init__(self):
        self.query_params = {'access_token': '45f844d976acc00dce12c5220cbcfcb16356',
                                             'longUrl':input("Enter the url to Shorten:")}#use your access token of bitly
    def shortenUrl(self):
        api_address= 'https://api-ssl.bitly.com/v3/shorten'
        response = requests.get(api_address, params=self.query_params)
        x = response.json()
        result = x['data']['url']
        print('Short URL is:',result)
        driver = webdriver.Chrome()
        driver.get(result)
        while True:
            time.sleep(1)
        driver.close()
app = urlshorten()
app.shortenUrl()
