import requests

import reports
# API = '5htfHBhDQYiqsM56kk4PJLQqhMvsarPe'


# API_KEY = '75a46huIPgb1GKGD4PBdu30EgI35nUs5OkiY60JKi2Wtpp'
API_KEY = '75arNXvyQMWahLeyGEvOVUYuM2LoXcoss6oL5iufAYMi5H'

twelve_API_KEY = 'f767e53cb99645f9931e63a3f18b3100'



stocks_list = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
for stock in stocks_list:
    response_element = requests.get(f"https://api.twelvedata.com/price?symbol={stock}&apikey=f767e53cb99645f9931e63a3f18b3100")
    print(response_element)
    print(response_element.text)