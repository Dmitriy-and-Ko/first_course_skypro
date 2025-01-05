import json

import pandas as pd
from typing import Optional
from pathlib import Path
import csv
from datetime import date
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from numpy.ma.core import shape

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
    # for row in csv_to_iterator(PATH_TO_FILE_CSV):
    #     print(row)
    # df_with_index_category = pd.read_excel(PATH_TO_FILE, sheet_name="Отчет по операциям", index_col=9)
    date = '2020-03-18 9:43:51'
    date_format = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y %H:%M:%S')
    obj_date_upper = datetime.strptime(date_format, '%d.%m.%Y %H:%M:%S')
    year_upper_date = obj_date_upper.year
    month_upper_date = obj_date_upper.month
    day_upper_date = obj_date_upper.day
    hour_upper_date = obj_date_upper.hour
    minute_upper_date = obj_date_upper.minute
    second_upper_date = obj_date_upper.second
    obj_date_lower = datetime(year_upper_date, month_upper_date, 1, hour_upper_date, minute_upper_date,
                                       second_upper_date)
    str_date_lower = datetime.strftime(obj_date_lower, '%d.%m.%Y %H:%M:%S')
    str_date_upper = datetime.strftime(obj_date_upper, '%d.%m.%Y %H:%M:%S')
    print([str_date_lower, str_date_upper])

    print(obj_date_lower)
    print(type(obj_date_lower))
    print(obj_date_upper)
    print(type(obj_date_upper))


    df = pd.read_excel(PATH_TO_FILE, sheet_name="Отчет по операциям")



    df_category = df.groupby('Категория')
    print(df_category['Сумма платежа'].mean())
    group_df_category = df_category['Сумма платежа'].mean()
    list_dict = group_df_category.to_dict()
    print(list_dict)

    # df_with_index_card_number = pd.read_excel(PATH_TO_FILE, sheet_name="Отчет по операциям", index_col=2)
    # group_df_index_card_number = df_with_index_card_number['Сумма платежа'].mean()
    # print(group_df_index_card_number)


    # df_group_card_number_sum_pay_cash_back = df.groupby(['Номер карты', 'Сумма платежа', 'Кэшбэк']).sum()
    # print(df_group_card_number_sum_pay_cash_back)



    df_card_number = df.groupby('Номер карты')
    df_card_number_sum_pay = df_card_number.agg({'Сумма платежа': 'mean', 'Кэшбэк': 'mean'})
    shape_card_number_sum_pay = df_card_number_sum_pay.shape
    list_dict_card_number = []
    # for i in range(shape_card_number_sum_pay[0]):
    #     list_dict_card_number.append(df_card_number_sum_pay.iloc[i].to_dict())
    # print(list_dict_card_number)
    # for i in range(shape_card_number_sum_pay[0]):
    #     list_dict_card_number.append
    #     {df_card_number_sum_pay.iloc[i, 0]: df_card_number_sum_pay.iloc[i, 1]}
    # print(list_dict_card_number)

    # for i in range(shape_card_number_sum_pay[0]):
    #     list_dict_card_number.append
    #     {df_card_number('Номер карты')}
    # print(list_dict_card_number)

    # print(df_card_number_sum_pay)
    # print(shape_card_number_sum_pay)
    # list_card_dict = df_card_number_sum_pay.to_dict()
    # print(list_card_dict)





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