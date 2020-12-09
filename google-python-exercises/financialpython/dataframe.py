import quandl
import pandas as pd
import numpy as np

# A Dataframe  is a collection of Series Objects, each of which may contain different data types
# A DataFrame can be created from various data types: dictionary, 2-D numpy.ndarray, a Series or another DataFrames
def main():
    dict = {'AAPL': [143.5, 144.09, 142.73, 144.18, 143.77],
            'GOOG': [898.7, 911.71, 906.69, 918.59, 926.99],
            'IBM': [155.58, 153.67, 152.36, 152.94, 153.49]}
    dates = pd.date_range('2017-07-03', periods=5, freq='D')
    df = pd.DataFrame(dict, index=dates)
    # print(df)

    apple_table = quandl.get("EOD/AAPL", authtoken="ZCLG2HRqUFhBZxgfbrmj")
    # create series called data_series here 'Value' is the series name
    df = apple_table
    # print(df.describe())
    # print(df.Close.tail(5))
    # print(df['Adj_Volume'].tail(5))
    apple_2016 = df['2016']
    apple_month = apple_2016.resample('M').agg(lambda x: x[-1])
    print(apple_month)
    columns = apple_month.columns
    for col in columns:
        print(col)

    aapl_bar = apple_month[['Open', 'High', 'Low', 'Close']]
    print(aapl_bar)
    print(apple_month.loc['2016-03':'2016-06', ['Open', 'Close', 'High', 'Low']])
    print()
    print('---- above mean close ----')
    above = aapl_bar[aapl_bar.Close > np.mean(aapl_bar.Close)]
    print(above)

    aapl_bar['rate_return'] = df.Close.pct_change()
    print(aapl_bar)
if __name__ == '__main__':
    main()
