import pandas as pd
FILENAME = "simple_data_1.csv"
if __name__ == '__main__':
    df = pd.read_csv(FILENAME)
    print(df.shape)
    print(df.head())
