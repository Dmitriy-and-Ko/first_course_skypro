import json


from src.utils import get_welcome_of_time
from src.views import get_data_for_json_about_currency, PATH_TO_JSON, get_data_for_json_about_stocks
from pathlib import Path

PATH_TO_OUT_DIR = Path(__file__).parent
PATH_TO_OUT_JSON = Path(PATH_TO_OUT_DIR, 'out_json.json')

def get_main_dictionary() -> dict:
    """Функция, формирует итоговый словарь"""
    main_dictionary ={
        "greeting": get_welcome_of_time(),
        "currency_rates": get_data_for_json_about_currency(PATH_TO_JSON),
        "stock_prices": get_data_for_json_about_stocks(PATH_TO_JSON)
    }
    return main_dictionary

def save_to_file(data_dict: dict, path_to_file) -> None:
    try:
        with open(path_to_file, 'w', encoding="utf-8") as data_file:
            json.dump(data_dict, data_file)
    except Exception as ex:
        return f"Произошла ошибка {ex}"

if __name__ == "__main__":

    save_to_file(get_main_dictionary(), PATH_TO_OUT_JSON)