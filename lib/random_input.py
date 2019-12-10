import pandas as pd
import os.path as op
import numpy as np

from input import Input

# df = pd.DataFrame(keep)
# pd.to_numeric(df[0], downcast='integer').to_csv('lib/typical.csv', header=True)


class RandomInput(Input):
    def __init__(self, chunk, rate):
        super().__init__()
        filepath = op.join(op.dirname(__file__), 'typical.csv')
        self.read = pd.read_csv(filepath, index_col=0)['0'].values
        self.i = 0

    def listen(self):
        value = 200 if np.random.rand() < .99 else 3000
        return value
