import pytest
from project import get_exchange_rate, convert_currency

def test_get_exchange_rate():
    assert get_exchange_rate('USD', 'EUR') == 0.91
    assert get_exchange_rate('EUR', 'USD') == 1.1
    assert get_exchange_rate('USD', 'KZT') == 450
    assert get_exchange_rate('KZT', 'USD') == 0.0022
    assert get_exchange_rate('EUR', 'KZT') == 490
    assert get_exchange_rate('KZT', 'EUR') == 0.0020
    assert get_exchange_rate('USD', 'GBP') is None

def test_convert_currency():
    assert convert_currency(100, 'USD', 'EUR') == 91.0
    assert convert_currency(50, 'EUR', 'USD') == 55.0
    assert convert_currency(200, 'USD', 'KZT') == 90000
    assert convert_currency(500, 'KZT', 'USD') == 1.1
    assert convert_currency(1000, 'EUR', 'KZT') == 490000
    assert convert_currency(1000, 'KZT', 'EUR') == 2.0
    assert convert_currency(100, 'USD', 'GBP') is None
