import quandl
import pandas as pd
import numpy as np


def main():
    apple_table = quandl.get("EOD/AAPL", authtoken="ZCLG2HRqUFhBZxgfbrmj")
    # print(apple_table)
    aapl = apple_table.loc['2017-03', ['Open', 'Close']]
    aapl['log_price'] = np.log(aapl.Close)
    aapl['log_return'] = aapl['log_price'].diff()  # current log_price - previous log_price
    print(aapl)

    print('--monthly return--')
    month_return = aapl.log_return.sum()
    print(month_return)

    print('--Arithmetic Mean---')
    print(np.mean(aapl.log_price))

    # Variance is a measure of dispersion. In finance, most of the time variance is a synonym for risk.
    # The higher the variance of an asset price is, the higher risk the asset bears.
    print('---Variance---')
    print(np.var(aapl.log_price))

    # The most commonly used measure of dispersion in finance is standard deviation.
    print('---Standard Deviation ---')
    print(np.std(aapl.log_price))


if __name__ == '__main__':
    main()
