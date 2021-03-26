from bs4 import BeautifulSoup   # Importing BS4 which will be needed for web scrapping
import requests                 # Requests will be required to do a GET request to the NSE website
from selenium import webdriver

def get_info(stock_list):
    # Necessary Headers for the GET request
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

    res = []    # Result list, which will be returned. It will have a dictionary for each stock.

    for stock in stock_list:
        d = {}      # Initializing a dictionary to store data about the particular stock
        # html_content = requests.get(f'https://www.nseindia.com/get-quotes/equity?symbol={stock}', headers=headers).text
        driver = webdriver.Firefox()
        driver.get(f'https://www.nseindia.com/get-quotes/equity?symbol={stock}')
        html_content = driver.execute_script("return document.documentElement.outerHTML")
        soup = BeautifulSoup(html_content, 'lxml')      # Creating a BeautifulSoup instance with lxml parser
        price_table = soup.find_all('table', class_='w-100')
        print(price_table)

if __name__ == '__main__':
    db = get_info(["RELIANCE"])

    https://www.nseindia.com/api/quote-equity?symbol=RELIANCE
    https://www.nseindia.com/api/quote-equity?symbol=RELIANCE&section=trade_info