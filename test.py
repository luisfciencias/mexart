# simple visual test
import pandas as pd

# template to load time series
column_names = ['utc', 'voltaje']
df = pd.read_csv('2019-01-24_L1.txt', names=column_names,
                 header=None, delim_whitespace=True)
print(df.shape)
print(df.dtypes)
print(df.head())
