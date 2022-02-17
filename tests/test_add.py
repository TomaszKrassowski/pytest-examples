import pytest

from main import add


class TestAddFunction:

    @pytest.mark.parametrize("first_number,second_number,expected_result", [
        (1, 1, 2),
        (100, 21, 121),
        (1, -1, 0),
        (1, -100, -99),
        (-100, 1, -99),

    ])
    def test_numbers(self, first_number, second_number, expected_result):
        result = add(first_number, second_number)
        assert result == expected_result

    @pytest.mark.parametrize("first_number,second_number", [
        ("string", 1),
        ({}, 1),
        ([], 1),
    ])
    def test_passing_non_numbers(self, first_number, second_number):
        with pytest.raises(TypeError):
            add(first_number, second_number)
