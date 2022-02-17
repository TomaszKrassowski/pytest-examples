from unittest.mock import patch, Mock

import pytest

from django_like import CoinModel
from main import add, get_coins_names


@pytest.fixture()
def coin_model():
    return CoinModel(id="id", rank=1, name="name")


class TestCoinModel:
    """
    This examples show how to use a fixture.
    When using some kind of object or value in different test cases, the repeating code can be put into fixture,
    which will be automatically inserted into test function, if it is passed as an argument.
    This allows to have repeatable and consistent test cases.
    More about fixtures: https://docs.pytest.org/en/6.2.x/fixture.html
    """

    def test_get_value_should_return_between_1_and_100(self, coin_model):
        value = coin_model.get_value()
        assert 1 <= value <= 100

    def test_str_should_return_id_joined_with_name(self, coin_model):
        model_string = str(coin_model)

        assert f"{coin_model.id} {coin_model.name}" == model_string
