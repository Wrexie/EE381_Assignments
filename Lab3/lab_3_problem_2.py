import numpy as np
import scipy.stats as sc
import matplotlib.pyplot as plt


def main():
    p = [0.2, 0.1, 0.15, 0.3, 0.2, 0.05]
    N = 10000
    n = 1000


    fig, ax = plt.subplots(1, 1)
    mean, var, skew, kurt = sc.binom.stats(n, .003, moments='mvsk')
    x = np.arange(sc.binom.ppf(0.01, n, .003),
                  sc.binom.ppf(0.99, n, .003))
    ax.plot(x, sc.binom.pmf(x, n, .003), 'bo', ms=8, label='binom pmf')
    ax.vlines(x, 0, sc.binom.pmf(x, n, .003), colors='b', lw=5, alpha=0.5)
    plt.title('Bernoulli Trials PMF for 3 Unfair Die using Binomial Distribution')
    plt.xlabel('Number of successes per 1000 rolls')
    plt.ylabel('Probability')

    plt.show()

    print()

main()
