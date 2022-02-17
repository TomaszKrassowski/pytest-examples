from unittest.mock import patch, Mock, MagicMock

import pytest

from main import add, get_coins_names


@pytest.fixture()
def bitcoin_data():
    return {
        "id": "btc-bitcoin",
        "is_active": True,
        "is_new": False,
        "name": "Bitcoin",
        "rank": 1,
        "symbol": "BTC",
        "type": "coin",
    }

@pytest.fixture()
def request_get_mock():
    response = Mock(status_code=200)
    response.json.return_value = []
    return response


class TestGetCoinNames:

    def test_getting_data_without_patching(self):
        names = get_coins_names()
        assert "Bitcoin" in names

    @patch('main.requests.get')
    def test_getting_data_with_patching(self, get_patch):
        object_returned_from_get = Mock(status_code=200)
        object_returned_from_get.json.return_value = [
            {"name": "bitcoin"}
        ]
        get_patch.return_value = object_returned_from_get

        names = get_coins_names()
        assert "bitcoin" in names
        assert len(names) == 1

    @patch('main.requests.get')
    def test_correct_url_called(self, get_patch):
        object_returned_from_get = MagicMock(status_code=200)
        get_patch.return_value = object_returned_from_get

        get_coins_names()

        get_patch.assert_called_with('https://api.coinpaprika.com/v1/coins', timeout=10)

    @patch('main.requests.get')
    def test_getting_data_with_patching_and_fixture(self, get_patch, request_get_mock, bitcoin_data):
        request_get_mock.json.return_value = [
            bitcoin_data
        ]
        get_patch.return_value = request_get_mock

        names = get_coins_names()
        assert "Bitcoin" in names
        assert len(names) == 1

    @patch('main.requests.get')
    def test_getting_data_with_more_return_values(self, get_patch, request_get_mock, bitcoin_data):
        request_get_mock.json.side_effect = [
            [bitcoin_data],
            []
        ]
        get_patch.return_value = request_get_mock

        first_call_names = get_coins_names()
        second_call_names = get_coins_names()

        assert "Bitcoin" in first_call_names
        assert len(first_call_names) == 1
        assert len(second_call_names) == 0

