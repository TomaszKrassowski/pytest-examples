import pytest

from examples.maths import fibonacci


class TestFibonacci:

    @pytest.mark.parametrize("n,expected_result", [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
    ])
    def test_given_n_equals_0_when_calculating_fibonacci_then_expected_result_is_returned(
        self, n, expected_result
    ):
       result = fibonacci(n)

       assert result == expected_result

