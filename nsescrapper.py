from bs4 import BeautifulSoup   # For web scraping
import requests                 # For GET request
import json                     # Working with json and dicts

def get_info(stock_list):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

    res = [] 

    for stock in stock_list:
        d = {}

        # getting the html page
        html_content = requests.get(f'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol={stock}', headers=headers).text

        # Creating a BeautifulSoup instance with lxml parser
        soup = BeautifulSoup(html_content, 'lxml')

        # converting json to python dict
        stock_data = json.loads(soup.find('div', id='responseDiv').text.strip())["data"][0]

        # storing the needed fetched values
        d['stock'] = stock
        d['open'] = stock_data['open']
        d['dayHigh'] = stock_data['dayHigh']
        d['dayLow'] = stock_data['dayLow']
        d['closePrice'] = stock_data['closePrice']
        d['totalTradedVolume'] = stock_data['totalTradedVolume']
        d['deliveryToTradedQuantity'] = stock_data['deliveryToTradedQuantity']

        res.append(d)
    
    return res

if __name__ == '__main__':
    # function call, params will be list of stocks
    db = get_info(['RELIANCE', 'HDFCBANK', 'ADANIPORTS', 'ITC', 'SBIN', 'IOC', 'RBLBANK'])

    # Converting the dictionary object into a json readable string
    print(json.dumps(db, indent=2))     