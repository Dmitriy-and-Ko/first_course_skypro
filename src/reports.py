
import pandas as pd
from datetime import datetime, timedelta
from pandas import DataFrame
from pathlib import Path
from src.utils import get_time_period

PATH_TO_DIR = Path(__file__).parent.parent
PATH_TO_FILE = Path(PATH_TO_DIR, 'data', 'operations.xlsx')

def get_df_for_period(path: str, period_list: list) -> DataFrame:
    starting_time = datetime.strptime(period_list[0], '%d.%m.%Y %H:%M:%S')
    finishing_time = datetime.strptime(period_list[1], '%d.%m.%Y %H:%M:%S')
    print(type(starting_time))
    print(starting_time)
    print(type(finishing_time))
    print(finishing_time)
    if path == PATH_TO_FILE:
        df = pd.read_excel(PATH_TO_FILE, sheet_name="Отчет по операциям")
        df['Дaтa операции'] = pd.to_datetime(df['Дaтa операции'], format='%d.%m.%Y %H:%M:%S')
        df['Дата oперации'] = pd.to_datetime(df['Дата oперации'], format='%d.%m.%Y %H:%M:%S')
        df_for_time = df[(df['Дaтa операции'] >= starting_time) & (df['Дата oперации'] <= finishing_time)]
        return df_for_time

if __name__ == '__main__':
    print(get_df_for_period(PATH_TO_FILE, get_time_period('20.05.2020 12:12:22')))



