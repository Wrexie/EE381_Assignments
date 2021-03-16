import numpy as np
import scipy.stats as sc
import matplotlib.pyplot as plt


# Main function
def main():
    # Probability of rolling a 1 on the first die, a 2 on the second die
    # and a 3 on the third die. In other words, the probability of the experiment
    # being a success
    p = .003
    # Number of times to roll the 3 dice
    n = 1000

    # Hi Professor, so rather than making my own function for the Binomial formula, I used
    # a pre-existing library that contains the formula. I hope that is ok.

    # Binomial formula and plotting code
    fig, ax = plt.subplots(1, 1)
    mean, var, skew, kurt = sc.binom.stats(n, p, moments='mvsk')
    x = np.arange(sc.binom.ppf(0.01, n, p),
                  sc.binom.ppf(0.99, n, p))
    ax.plot(x, sc.binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
    ax.vlines(x, 0, sc.binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
    plt.title('Bernoulli Trials: PMF – Binomial Formula')
    plt.xlabel('Number of successes per 1000 rolls')
    plt.ylabel('Probability')

    plt.show()


main()

