import random

from input import Input


class RandomInput(Input):
    def __init__(self):
        super().__init__()

    def listen(self):
        value = 200 if random.random() < .999 else 3000
        return value
