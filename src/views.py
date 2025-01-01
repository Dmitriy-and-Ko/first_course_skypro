import json
import os

import requests
from pathlib import Path

from dotenv import load_dotenv


PATH_TO_DIR = Path(__file__).parent.parent
PATH_TO_ENV = Path(PATH_TO_DIR, '.env')

# twelve_API_KEY = 'f767e53cb99645f9931e63a3f18b3100'
# currency_API_KEY = "JB6myZtJ89nwLwUpzo0LoDWOqKD26TaZ"
load_dotenv(PATH_TO_ENV)
STOCK_API_KEY = os.getenv("STOCK_API-KEY")
CURRENCY_API_KEY = os.getenv('CURRENCY_API-KEY')


def get_price_list_of_stocks(stock_name : str) -> str:
    """Функция принимает на вход название одной из 5 акций: AAPL, AMZN, GOOGL, MSFT, TSLA и возвращает её
    действительную цену"""
    response = requests.get(f"https://api.twelvedata.com/price?symbol={stock_name}&apikey={STOCK_API_KEY}")
    if response.status_code == 200:
        json_str = response.text
        dict_result = json.loads(json_str)
        price_stock = dict_result.get('price')
        return price_stock

def get_currency_rate(current_string: str) -> float:
    """Функция принимает на вход название валюты в виде USD или EUR и возвращает её курс по отношению к рублю"""

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={current_string}&amount=1"

    'apikey: YOUR API KEY'

    payload = {}
    headers = {
        "apikey": CURRENCY_API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    # print(status_code)
    result = response.text
    dict_result = json.loads(result)
    currency_price = dict_result.get('result')
    return float(currency_price)

if __name__ == "__main__":
    print(get_price_list_of_stocks('googl'))
    print(get_currency_rate('USD'))

