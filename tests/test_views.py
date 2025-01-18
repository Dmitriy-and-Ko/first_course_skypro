import json
import os

import requests
from pathlib import Path
from unittest.mock import patch
from src.views import get_price_of_stock
from dotenv import load_dotenv


@patch('requests.get')
def test_get_price_of_stock(mock_get):
  mock_get.return_value.text = '{"stock": "AAPL", "price": "1"}'
  assert get_price_of_stock("AAPL") == "1"
  stock_name = "AAPL"
  STOCK_API_KEY = os.getenv("STOCK_API-KEY")
  mock_get.assert_called_once_with(f"https://api.twelvedata.com/price?symbol={stock_name}&apikey={STOCK_API_KEY}")