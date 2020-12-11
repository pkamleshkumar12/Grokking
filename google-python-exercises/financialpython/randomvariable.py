import quandl
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


def main():
    apple_table = quandl.get("EOD/AAPL", authtoken="ZCLG2HRqUFhBZxgfbrmj")
    # print(apple_table)

    # Point estimation means using sample data to calculate a single value which is serve as a 'best estimation' of an
    # unknown population

    # Random Variables
    # If we roll the dice N times and record the number of each roll, a collection of those numbers is called
    # discrete random variable. The other type is called continuous random variable can any value in a given range.

    # Distribution
    # Each random variable follows a probability distribution
    # Probability density function (PDF) function to describe the probability that a value is in a specific range.
    # For each PDF, we have cumulative distribution function (CDF), it is defined as P(X<=x), which models the probality

    series = np.array([dice() for x in range(1000)])
    print(series)
    plt.figure(figsize=(20, 10))
    plt.hist(series, bins=11, align='mid')
    plt.xlabel('Dice Number')
    plt.ylabel('Occurrences')
    plt.grid()
    # plt.show()

    # calculating P(X<=3)
    print(len([x for x in series if x <= 3]) / float(len(series)))
    print(np.mean(series))

    # Binomial distribution
    # A binomial distribution is a discrete probability distribution of the number of successes in a sequence of
    # n independent experiments.
    res = [trial() for x in range(10)]
    print(sum(res))

    # The number printed below is simulated probability that we success 8 times if experiment 10 times
    print('--> Binomial <--')
    print(binomial(8))

    prob = []
    for i in range(1, 11):
        prob.append(binomial(i))

    prob_s = pd.Series(prob, index=range(1, 11))
    print(prob_s)
    plt.figure(figsize=(20, 10))
    plt.bar(range(1, 11), prob)
    plt.grid()
    # plt.show()


def dice():
    # Uniform Distribution
    # A discrete uniform distribution has equal weight assigned to all outcomes.
    number = [1, 2, 3, 4, 5, 6]
    return random.choice(number)


def binomial(number):
    l = []
    for i in range(10000):
        res = [trial() for x in range(10)]
        l.append(sum(res))

    return len([x for x in l if x == number]) / float(len(l))


def trial():
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a = random.choice(number)
    if a <= 7:
        return 1
    else:
        return 0


if __name__ == '__main__':
    main()
