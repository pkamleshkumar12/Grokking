import quandl
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


def main():
    spy_table = quandl.get("EOD/AAPL", authtoken="ZCLG2HRqUFhBZxgfbrmj")
    # Normal Distribution
    # As stated, probability desity function (PDF) to model the probability that our value is taken
    # out of specific range
    # if a normal distribution has a 0 mean and 1 standard deviation, we called it standard normal distribution
    # print(spy_table)
    spy = spy_table.loc['2015':'2017', ['Open', 'Close']]
    spy['log_return'] = np.log(spy.Close).diff()
    spy = spy.dropna()
    plt.figure(figsize=(20, 10))
    # spy.log_return.plot()
    spy.log_return.plot.density()
    # plt.show()

    # μ denotes the mean of the normal distribution
    # σ denotes the standard deviation

    de_2 = pd.Series(np.random.normal(0, 2, 10000), name='μ = 0, σ = 2')
    de_3 = pd.Series(np.random.normal(0, 3, 10000), name='μ = 0, σ = 3')
    de_0 = pd.Series(np.random.normal(0, 0.5, 10000), name='μ = 0, σ = 0.5')
    mu_1 = pd.Series(np.random.normal(-2, 1, 10000), name='μ = -2, σ = 1')
    df = pd.concat([de_2, de_3, de_0, mu_1], axis=1)
    plt.figure(figsize=(20, 10))
    df.plot.density()
    plt.show()


if __name__ == '__main__':
    main()
