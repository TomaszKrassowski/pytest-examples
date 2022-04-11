import time


class DatabaseQueryMaker:

    def __init__(self, n: int):
        self.n = n

    def make_query(self):
        return [{
            "a": 1
        }, {
            "a": 2
        }]


class Foo:

    def __init__(self, some_class: DatabaseQueryMaker):
        self.class_to_call = some_class

    def foo(self):
        result = self.class_to_call.make_query()

        return [row for row in result if row["a"] % 2 == 0]



