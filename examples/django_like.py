import random
import time


class CoinManager:

    def filter(self, *args, **kwargs):
        time.sleep(1 + random.randint(0, 3))
        result = list(self.__entities)
        for name, value in kwargs.items():
            if name.endswith("__in"):
                filtered_name = name.replace("__in", "")
                for single_value in value:
                    result = [
                        entity for entity in result if getattr(entity, filtered_name) == single_value
                    ]
            else:
                result = [
                    entity for entity in result if getattr(entity, name) == value
                ]
        return result

    @property
    def __entities(self):
        return [
            CoinModel('btc-bitcoin', 1, 'Bitcoin'),
            CoinModel('eth-ethereum', 1, 'Ethereum'),
        ]


class CoinModel:
    objects = CoinManager()

    def __init__(self, id: str, rank: int, name: str):
        self.id = id
        self.rank = rank
        self.name = name

    def get_value(self):
        return random.randint(1, 100)

    def __str__(self):
        return f"{self.id} {self.name}"
