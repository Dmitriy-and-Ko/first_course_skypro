import pandas as pd
from typing import Optional
from pathlib import Path
from src.utils import get_time_period
from datetime import date
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from numpy.ma.core import shape

PATH_TO_DIR = Path(__file__).parent.parent
PATH_TO_FILE = Path(PATH_TO_DIR, 'data', 'operations.xlsx')

if __name__ == '__main__':
    print(PATH_TO_FILE)
    df = pd.read_excel(PATH_TO_FILE, sheet_name="Отчет по операциям")
    period_list = get_time_period('2020-06-24 00:05:12')
    df_time_for_period = df.groupby('Дата платежа')
    df_time_for_period = df[(datetime.strptime(df.loc['Дата платежа'],'%d.%m.%Y %H:%M:%S')) <= datetime.strptime(period_list[1], '%d.%m.%Y %H:%M:%S')]
    print(period_list[0])
    print(period_list[1])
    print(df_time_for_period)