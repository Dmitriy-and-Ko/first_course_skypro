import pandas as pd
from typing import Optional
from pathlib import Path
import csv
from datetime import date
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

PATH_TO_DIR = Path(__file__).parent.parent
PATH_TO_FILE = Path(PATH_TO_DIR, 'data', 'operations.xlsx')
PATH_TO_FILE_CSV = Path(PATH_TO_DIR, 'data', 'Отчет по операциям.csv')
# print(PATH_TO_DIR)
# print(PATH_TO_FILE)
# print(PATH_TO_FILE_CSV)
def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date: Optional[str] = None) -> pd.DataFrame:
    """Функция принимает на вход:
    датафрейм с транзакциями,
    название категории,
    опциональную дату.
Если дата не передана, то берется текущая дата.

Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    pass

def excel_reader(excel_path: str) ->pd.DataFrame:
    try:
        if excel_path == PATH_TO_FILE:
            excel_data = pd.read_excel(PATH_TO_FILE, sheet_name="Отчет по операциям" )
            shape_data = excel_data.shape
            list_of_dicts = [dict(excel_data.iloc[x]) for x in range(shape_data[0])]
            return list_of_dicts
        else:
            return "Неверно указан путь к файлу Excel transactions"
    except Exception as ex:
        return f"Ошибка {ex}"

def csv_reader(csv_path: str) -> list:
    """Функция считывает финансовые операции из CSV файла принимает путь к файлу CSV в качестве аргумента.
    Результат выводит в виде списка словарей"""
    try:
        if csv_path == PATH_TO_FILE_CSV:
            with open(PATH_TO_FILE_CSV, encoding="utf-8") as file:
                reader = csv.DictReader(file)
                result = list(reader)
                # for row in reader:
                #     print(row)
                return result
        return f"Неверно указан путь к файлу CSV transactions"
    except Exception as ex:
        return f"Ошибка {ex}"


def spending_by_category(transactions: list,
                         category: str,
                         date: Optional[str] = None) -> list:
    """Функция принимает на вход:
    список словарей с транзакциями,
    название категории,
    опциональную дату.
Если дата не передана, то берется текущая дата.

Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    if date is None:
        date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    else:
        date = datetime.strptime(date, '%d.%m.%Y %H:%M:%S').strftime('%d.%m.%Y %H:%M:%S')
    upper_date = datetime.strptime(date, '%d.%m.%Y %H:%M:%S') + relativedelta(months=-3)
    low_date = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
    print(type(low_date))
    print(type(upper_date))
    return [low_date, upper_date]

# def iteration_reader_csv():
#     file_name = PATH_TO_FILE_CSV
#     lines = (line for line in open(file_name))
#     return lines

# def iteration_reader_csv():
#     file_name = PATH_TO_FILE_CSV
#     file_read = open(file_name, 'r')
#     line = file_read.readline()
#     return line



# def iteration_reader_csv():
#     file = PATH_TO_FILE_CSV
#     with open(file,  'r', newline=" ") as reader_file:
#     line = file_read.readline()
#     return line



def csv_to_iterator(file_path):
    # if file_path == PATH_TO_FILE_CSV:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield row


if __name__ == '__main__':
    for row in csv_to_iterator(PATH_TO_FILE_CSV):
        print(row)
    # print(excel_reader(PATH_TO_FILE))
    # csv_reader(PATH_TO_FILE_CSV)
    # print(spending_by_category([], 'категория', '01.01.2018 11:34:02'))
    # file_name = PATH_TO_FILE_CSV
    # lines = (line for line in open(file_name))
    # list_line = (s.rstrip().split(",") for s in lines)
    # cols = next(list_line)
    # log_dicts = (dict(zip(cols, data)) for data in list_line)
    # e = iteration_reader_csv()
    # print(next(e))
    # print(iteration_reader_csv())