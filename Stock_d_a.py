import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'R76SKXZKMHY0WXK3'


ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(
    symbol='TD.TO', interval='1min', outputsize='full')
print(data)

