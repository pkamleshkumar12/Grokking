import quandl


def main():
    quandl.ApiConfig.api_key = 'ZCLG2HRqUFhBZxgfbrmj'
    table_data = quandl.get("EIA/PET_RWTC_D")

    # create series called data_series here 'Value' is the series name
    data_series= table_data['Value']
    print(data_series.describe())
    print(data_series.iloc[1])
    print(data_series['2017-2':'2017-4'])
    print('---head(N)---')
    print(data_series.head(2))
    print('---tail(N)---')
    print(data_series.tail(4))

    # Resampling
    # series.resample(freq) is a class called 'DatetimeIndexResampler' which groups data in Series object
    # into regular time intervals
    # series.resample.mean() is a complete statement that groups data into intervals, and then compute the mean
    # of each interval
    print('Aggregate the daily data into monthly data by mean:')
    by_month = data_series.resample('M').mean()
    print(by_month)
    print('Aggregate the daily data into weekly data by mean:')
    by_week = data_series.resample('W').mean()
    print(by_week)
    print(by_week.head())

    # any frequency by using the format 'nf', where 'n' is an integer and 'f' is M for month, W for week and D for day
    three_day = data_series.resample('3D').mean()
    two_week = data_series.resample('2W').mean()
    two_month = data_series.resample('2M').mean()

    std = data_series.resample('W').std()       # standard deviation
    max = data_series.resample('W').max()       # maximum value
    min = data_series.resample('W').min()       # minimum value
    print('---Weekly minimum---')
    print(min)

    # series.resample.agg() method which accepts labmdas
    last_day = data_series.resample('M').agg( lambda x: x[-1])
    print(last_day)
    # directly calculate the monthly rates of return using the data for the first day and the last day:
    monthly_return = data_series.resample('M').agg(lambda x: x[-1] / x[1] - 1)
    print('---monthly return---')
    print(monthly_return)
    print(monthly_return.mean())
    print(monthly_return.std())
    print(monthly_return.max())

    # .diff calculates the difference between consecutive elements and .pct_change calculate the percentage change
    print('---diff()---')
    print(last_day.diff())
    print('---pct_change()---')
    print(last_day.pct_change())

    # When dealing with NaN values, we usually either removing the data point or fill it with a specific value.
    # fillna(0), .fillna(method = 'bfill') or simply use .dropna() on series to remove data point
if __name__ == '__main__':
    main()


# ZCLG2HRqUFhBZxgfbrmj