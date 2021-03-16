import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc


# Main function
def main():
    # Probability of experiment being a success based on the vector
    # for our unfair die
    p = .003
    # Number of times to roll our dice
    n = 1000
    # Mu variable calculated by multiplying n and p
    mu = p * n

    # Hi Professor, again I used a pre-existing library that contains the
    # Poisson distribution formula rather than making my own function.

    # Poisson distribution formula and plotting code
    fig, ax = plt.subplots(1, 1)
    mean, var, skew, kurt = sc.poisson.stats(mu, moments='mvsk')
    x = np.arange(sc.poisson.ppf(0.01, mu),
                  sc.poisson.ppf(0.99, mu))
    ax.plot(x, sc.poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
    ax.vlines(x, 0, sc.poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)
    rv = sc.poisson(mu)
    ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
              label='frozen pmf')
    ax.legend(loc='best', frameon=False)
    plt.title('Bernoulli Trials: PMF – Poisson Approximation')
    plt.xlabel('Number of successes per 1000 rolls')
    plt.ylabel('Probability')

    plt.show()


main()

