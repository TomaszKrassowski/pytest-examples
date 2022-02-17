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
        """
        This example shows how to parametrize test function.
        First parameter of decorator are names of the arguments that will be later on replaced with different values.
        Second argument is a list of tuples, which represent values that will be tested.
        More about parametrize: https://docs.pytest.org/en/6.2.x/reference.html?highlight=parametrize#pytest.python.Metafunc.parametrize
        """
        result = add(first_number, second_number)
        assert result == expected_result

    @pytest.mark.parametrize("first_number,second_number", [
        ("string", 1),
        ({}, 1),
        ([], 1),
    ])
    def test_passing_non_numbers(self, first_number, second_number):
        """
        This example shows how to check if code raises error when we expect it.
        More about raises: https://docs.pytest.org/en/6.2.x/reference.html?highlight=parametrize#pytest-raises
        """
        with pytest.raises(TypeError):
            add(first_number, second_number)
