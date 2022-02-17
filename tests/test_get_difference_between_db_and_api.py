from unittest.mock import patch, Mock

import pytest

from django_like import CoinModel
from main import get_difference_between_api_and_db


class TestGetCoinNames:

    def test_getting_data_without_patching(self):
        difference = get_difference_between_api_and_db()
        assert difference != 0

    @patch('main.requests.get')
    @patch.object(CoinModel.objects, 'filter')
    def test_getting_data_with_patching(self, filter_patch, get_patch):
        object_returned_from_get = Mock(status_code=200)
        object_returned_from_get.json.return_value = [
            {"name": "bitcoin"}
        ]
        get_patch.return_value = object_returned_from_get

        filter_patch.return_value = []

        difference = get_difference_between_api_and_db()

        assert difference == 1
