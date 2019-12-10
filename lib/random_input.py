import pandas as pd
import os.path as op
import random

from input import Input

# df = pd.DataFrame(keep)
# pd.to_numeric(df[0], downcast='integer').to_csv('lib/typical.csv', header=True)


class RandomInput(Input):
    def __init__(self):
        super().__init__()

    def listen(self):
        value = 200 if random.random() < .99 else 3000
        return value
