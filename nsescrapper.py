from bs4 import BeautifulSoup   # Importing BS4 which will be needed for web scrapping
import requests                 # Requests will be required to do a GET request to the NSE website
import json                     # importing json module to convert a string of json data into python dict

def get_info(stock_list):
    # Necessary Headers for the GET request
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

    res = []    # Result list, which will be returned. It will have a dictionary for each stock.

    for stock in stock_list:
        d = {}      # Initializing a dictionary to store data about the particular stock

        # getting the html page
        html_content = requests.get(f'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol={stock}', headers=headers).text

        soup = BeautifulSoup(html_content, 'lxml')      # Creating a BeautifulSoup instance with lxml parser

        # scrapping the json data from the website and converting it into a python dict
        stock_data = json.loads(soup.find('div', id='responseDiv').text.strip())["data"][0]

        # storing the needed fetched values
        d['stock'] = stock
        d['open'] = stock_data['open']
        d['dayHigh'] = stock_data['dayHigh']
        d['dayLow'] = stock_data['dayLow']
        d['closePrice'] = stock_data['closePrice']
        d['totalTradedVolume'] = stock_data['totalTradedVolume']
        d['deliveryToTradedQuantity'] = stock_data['deliveryToTradedQuantity']

        # Appending the dictionary object for the particular stock in the result list
        res.append(d)
    return res  # return a list of dictionary objects

if __name__ == '__main__':
    db = get_info(['RELIANCE', 'HDFCBANK', 'ADANIPORTS', 'ITC', 'SBIN', 'IOC', 'RBLBANK'])  # function call, params will be list of stocks
    print(json.dumps(db, indent=2))     # Converting the dictionary object into a json readable string