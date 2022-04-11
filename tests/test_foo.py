from unittest.mock import Mock

from examples.foo import Foo, DatabaseQueryMaker


class TestFoo:


    def test_given_foo_class_with_bar_then_returns_BAR(self):
        bar = Mock(spec=DatabaseQueryMaker)
        bar.make_query.return_value = [
        ]

        foo = Foo(bar)
        result = foo.foo()

        assert result == []

    def test_given_foo_class_with_bar_then_returns_BAR_1(self):
        bar = Mock(spec=DatabaseQueryMaker)
        bar.make_query.return_value = [
            {"a": 1}
        ]

        foo = Foo(bar)
        result = foo.foo()

        assert result == []

    def test_given_foo_class_with_bar_then_returns_BAR_2(self):
        bar = Mock(spec=DatabaseQueryMaker)
        bar.make_query.return_value = [
            {"a": 2}
        ]

        foo = Foo(bar)
        result = foo.foo()

        assert result == [{"a": 2}]



