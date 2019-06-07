# simple visual test
import pandas as pd

# template to load time series
column_names = ['utc_string', 'voltaje']
df = pd.read_csv('2019-01-24_L1.txt', names=column_names,
                 header=None, delim_whitespace=True)

# single call for datetime conversion
year = '2019'
month = '01'
day = '24'
date = year + '-' + month + '-' + day
df['utc_string'] = [date + ' ' + item for item in df['utc_string']]
format_datetime_string = "%Y-%m-%d %H:%M:%S.%f"
df['utc_datetime'] = pd.to_datetime(df['utc_string'],
                                    format=format_datetime_string)
print(df)
print(df.dtypes)
