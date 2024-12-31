import json
import os

import requests
from pathlib import Path

from dotenv import load_dotenv


PATH_TO_DIR = Path(__file__).parent.parent
PATH_TO_ENV = Path(PATH_TO_DIR, '.env')

twelve_API_KEY = 'f767e53cb99645f9931e63a3f18b3100'
load_dotenv(PATH_TO_ENV)
API_KEY = os.getenv("API-KEY")


def get_price_list_of_stocks() -> list:
    """Функция возвращает список актуальных цен на акции AAPL, AMZN, GOOGL, MSFT, TSLA"""
    stocks_list = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    price_of_stocks = []
    for stock in stocks_list:
        response_element = requests.get(f"https://api.twelvedata.com/price?symbol={stock}&apikey={API_KEY}")
        # print(response_element)
        json_str = response_element.text
        dict_result = json.loads(json_str)
        price_element = dict_result.get('price')
        price_of_stocks.append(price_element)
    return price_of_stocks

if __name__ == "__main__":
    print(get_price_list_of_stocks())
