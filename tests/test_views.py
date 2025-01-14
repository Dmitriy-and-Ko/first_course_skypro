import json
import os

import requests
from pathlib import Path
from unittest.mock import patch
from src.views import get_price_of_stock
from dotenv import load_dotenv

@patch('requests.get')
def test_get_price_of_stock(mock_get):
    mock_get.return_value.text = "{'stock': 'AAPL', 'price': '1'}"
    assert get_price_of_stock('AAPL') == get_price_of_stock('AAPL')