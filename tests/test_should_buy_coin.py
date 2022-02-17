from unittest.mock import patch, Mock

import pytest

from django_like import CoinModel
from main import get_difference_between_api_and_db, should_buy_coin


class TestShouldBuyCoin:

    def test_getting_data_without_patching(self):
        difference = get_difference_between_api_and_db()
        assert difference != 0

    @pytest.mark.parametrize(
        "coin_value,willing_price,expected_result",
        [
            (100, 100, True),
            (1, 100, True),
            (100, 1, False),
            (0, 0, True),
        ]
    )
    @patch.object(CoinModel, 'get_value')
    def test_getting_data_with_patching(self, get_value_patch, coin_value, willing_price, expected_result):
        get_value_patch.return_value = coin_value

        coin_model = CoinModel("some_id", 1, "name")

        assert should_buy_coin(coin_model, willing_price) == expected_result

    @pytest.mark.parametrize(
        "coin_value,willing_price,expected_result",
        [
            (100, 100, True),
             (1, 100, True),
             (100, 1, False),
             (0, 0, True),
        ]
    )
    def test_getting_data_with_mock(self, coin_value, willing_price, expected_result):
        coin_model = Mock(spec=CoinModel)
        coin_model.get_value.return_value = coin_value

        assert should_buy_coin(coin_model, willing_price) == expected_result
        coin_model.get_value.assert_called()
