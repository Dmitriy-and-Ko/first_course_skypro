
from datetime import datetime



def get_time_period(date: str) -> list:
    """Функция принимает на вход дату в виде строки, в формате YYYY-MM-DD HH:MM:SS и возвращает времени в виде списка
    с двумя датами в виде строки в формате DD.MM.YYYY HH:MM:SS. За начало периода берётся начало месяца, по принятую
    функцией дату. Если дата — 20.05.2020, то функция вернёт [01.05.2020-20.05.2020]"""
    try:
        date_format = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y %H:%M:%S')
    except Exception as ex:
        return f"Ошибка {ex}"
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
    return [str_date_lower, str_date_upper]

def get_welcome_of_time() -> str:
    """Функция возвращает приветствие в формате "???" , где ???— «Доброе утро» / «Добрый день» / «Добрыйвечер» /
     «Доброй ночи» в зависимости от текущего времени."""
    now_time = datetime.now()
    hour_now = now_time.hour
    if 4 <= hour_now <= 10:
        return 'Good morning'
    elif 11 <= hour_now <= 16:
        return 'Good afternoon'
    elif 17 <= hour_now <= 22:
        return 'Good evening'
    else:
        return 'Good night'

if __name__ == '__main__':
    print(get_time_period('2020-03-18 14:32:15'))
    print(get_time_period('2020-03-18'))
    print(get_time_period('2020-18-03 14:15:15'))
    print(get_time_period('08.08.2020 12:00:00'))
    print(type(get_time_period('2020-03-18 14:32:15')[0]))
    print(get_welcome_of_time())
    print(type(get_welcome_of_time()))