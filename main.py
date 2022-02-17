import random

import requests

from django_like import CoinModel


def add(x, y):
    return x + y


def get_coins_names():
    url = 'https://api.coinpaprika.com/v1/coins'
    response = requests.get(url, timeout=10)
    assert response.status_code == 200
    coins_list = response.json()

    return [
        coin['name'] for coin in coins_list
    ]


def should_buy_coin(coin: CoinModel, max_price_willing_to_pay: int):
    """
    Checks if current coin price is lower than max price you are willing to pay
    """
    value = coin.get_value()
    return value <= max_price_willing_to_pay


def get_difference_between_api_and_db():
    names = get_coins_names()

    return len(names) - len(CoinModel.objects.filter(name__in=names))




