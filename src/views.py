import json
import os

import requests
from pathlib import Path

from dotenv import load_dotenv


PATH_TO_DIR = Path(__file__).parent.parent
PATH_TO_ENV = Path(PATH_TO_DIR, '.env')
PATH_TO_JSON = Path(PATH_TO_DIR, "user_settings.json")

# twelve_API_KEY = 'f767e53cb99645f9931e63a3f18b3100'
# currency_API_KEY = "JB6myZtJ89nwLwUpzo0LoDWOqKD26TaZ"
load_dotenv(PATH_TO_ENV)
STOCK_API_KEY = os.getenv("STOCK_API-KEY")
CURRENCY_API_KEY = os.getenv('CURRENCY_API-KEY')


def get_price_of_stock(stock_name : str) -> str:
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


def get_data_for_json_about_currency(path_json: str) -> dict:
    """Функция принимает на вход путь к файлу JSON с указанными валютами, по которым необходимо узнать курс.
    Ответ выдаёт в виде словаря."""
    with open(PATH_TO_JSON, 'r', encoding='utf-8') as file_json:
        json_dict = json.load(file_json)
    list_currencies = json_dict.get('user_currencies')
    list_of_currencies_price = []
    for element in list_currencies:
        currency_price = get_currency_rate(element)
        list_of_currencies_price.append({"currency": element,
                                         "rate": currency_price})
    return list_of_currencies_price


def get_data_for_json_about_stocks(path_json: str) -> dict:
    """Функция принимает на вход путь к файлу JSON с указанными акциями, по которым необходимо узнать
    цену. Ответ выдаёт в виде словаря."""
    with open(PATH_TO_JSON, 'r', encoding='utf-8') as file_json:
        json_dict = json.load(file_json)
    list_stocks = json_dict.get('user_stocks')
    list_of_stocks_price = []
    for element in list_stocks:
        stock_price = get_price_of_stock(element)
        list_of_stocks_price.append({"stock": element,
                                     "price": stock_price})
    return list_of_stocks_price


if __name__ == "__main__":
    # print(get_price_list_of_stocks('googl'))
    # print(get_currency_rate('USD'))
    print(PATH_TO_DIR)
    print(get_data_for_json_about_currency(PATH_TO_JSON))
    print(get_data_for_json_about_stocks(PATH_TO_JSON))

