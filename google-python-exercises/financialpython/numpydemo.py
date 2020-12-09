import numpy as np
import pandas as pd


def main():
    price_list = [143.73, 145.83, 143.68, 144.02, 143.5, 142.62]
    price_array = np.array(price_list)
    print(price_array)
    print(type(price_array))

    Ar = np.array([[1, 3], [2, 4]])
    print((Ar))
    print(type(Ar))
    print(Ar.shape)
    print(Ar[0])
    print(Ar[1])
    print(Ar[:, 0])  # to print (first column
    print(Ar[:, 1])  # to print (second column
    # to apply natural algorithm
    print(np.log(price_array))
    # to get mean
    print(np.mean(price_array))
    # to get standard deviation
    print(np.std(price_array))
    # to get sum
    print(np.sum(price_array))
    # to get max
    print(np.max(price_array))

    price = [143.73, 145.83, 143.68, 144.02, 143.5, 142.62]
    s = pd.Series(price)
    s = pd.Series(price, index=['a', 'b', 'c', 'd', 'e', 'f'])
    s.index = [6,5,4,3,2,1]
    print(s)
    print(s[1:])
    print(s[:-2])

    s = pd.Series(price, name = 'Apple Prices')
    print(s.name)
    # statistical summaries
    print(s.describe())

    # Time Index
    time_index = pd.date_range('2017-01-01', periods= len(s), freq= 'D')
    print(time_index)
    s.index = time_index
    print(s)

    # iloc[] is used to access elements by integer index
    # loc[] is used to access the index of the series

    s.index = [6,5,4,3,2,1]
    print(s)
    print(s[1])
    print(s.iloc[1])
    # both of the above statements are same
    s.index = time_index
    print(s)
    print(s.loc['2017-01-05'])
    print(s[s < np.mean(s)])
    print(s[(s > np.mean(s)) & (s < np.mean(s) + 1.64 * np.std(s))])

if __name__ == '__main__':
    main()
