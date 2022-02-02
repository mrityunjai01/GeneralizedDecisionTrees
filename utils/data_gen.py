import pandas as pd
import numpy as np
from constants import NO_SAMPLES
FILENAME = "simple_data_1.csv"

if __name__ == '__main__':
    data = np.random.normal(size=(NO_SAMPLES, 2))

    labels = np.where(data[:, 0] * data[:, 1] < 0, 0, 1)

    data = np.concatenate([data, labels[:, None]], axis = 1)
    np.savetxt(FILENAME, data)
