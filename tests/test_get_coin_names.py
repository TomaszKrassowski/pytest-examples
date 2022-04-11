from unittest.mock import patch, Mock, MagicMock

import pytest

from examples.main import add, get_coins_names


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
        """
        This test case can fail and it takes a lot more time to execute than the ones that are mocking the requests library.
        """
        names = get_coins_names()
        assert "Bitcoin" in names

    @patch('examples.main.requests.get')
    def test_getting_data_with_patching(self, get_patch):
        """
        This test case mocks the object returned from "get" function.
        Patch argument is the method/class we want to control.
        Mocked object will be available as function argument
        More about patch: https://docs.python.org/3/library/unittest.mock.html#patch

        The flow of the function is as below:
        > obj = requests.get()
        > obj.json()

        requests.get() - will return Mock by default (this is controlled by patch decorator), and we need to control
         the return value of obj.json(), so we explicitly say that get_patch.return_value is a mock we created with speficic fields and return value of functions
        """
        object_returned_from_get = Mock(status_code=200)
        object_returned_from_get.json.return_value = [
            {"name": "bitcoin"}
        ]
        get_patch.return_value = object_returned_from_get

        names = get_coins_names()
        assert "bitcoin" in names
        assert len(names) == 1

    @patch('examples.main.requests.get')
    def test_correct_url_called(self, get_patch):
        """
        We can check if function was called with expected arguments
        """
        object_returned_from_get = MagicMock(status_code=200)
        get_patch.return_value = object_returned_from_get

        get_coins_names()

        get_patch.assert_called_with('https://api.coinpaprika.com/v1/coins', timeout=10)

    @patch('examples.main.requests.get')
    def test_getting_data_with_patching_and_fixture(self, get_patch, request_get_mock, bitcoin_data):
        """
        Patch argument comes before fixtures
        """
        request_get_mock.json.return_value = [
            bitcoin_data
        ]
        get_patch.return_value = request_get_mock

        names = get_coins_names()
        assert "Bitcoin" in names
        assert len(names) == 1

    @patch('examples.main.requests.get')
    def test_getting_data_with_more_return_values(self, get_patch, request_get_mock, bitcoin_data):
        """
        We can specify that different calls have different return values
        """
        # assigning iterable to side_effect will return elements of iterable per different call
        request_get_mock.json.side_effect = [
            [bitcoin_data],
            []
        ]
        get_patch.return_value = request_get_mock

        first_call_names = get_coins_names()
        second_call_names = get_coins_names()
        # third_call_names = get_coins_names() # this will fail, as we only specified two elements to return

        assert "Bitcoin" in first_call_names
        assert len(first_call_names) == 1
        assert len(second_call_names) == 0

