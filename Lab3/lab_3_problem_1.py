import numpy as np
import matplotlib.pyplot as plt


def nSidedDie(p):
    cs = np.cumsum(p)
    cp = np.append(0, cs)
    n = len(p)
    d = 0
    r = np.random.random()
    for j in range(n):
        if r > cp[j] and r <= cp[j + 1]:
            d = j + 1

    return d


def main():
    p = [0.2, 0.1, 0.15, 0.3, 0.2, 0.05]
    N = 10000
    n = 1000
    s = np.zeros((N, 1))
    X = 0

    for i in range(N):
        X = 0
        for j in range(n):
            die1 = nSidedDie(p)
            die2 = nSidedDie(p)
            die3 = nSidedDie(p)

            if die1 == 1 and die2 == 2 and die3 == 3:
                X += 1

        s[i] = X

    b = range(1, len(p) + 2)
    sb = np.size(b)
    h1, bin_edges = np.histogram(s, bins=b)
    b1 = bin_edges[0:sb - 1]
    plt.close('all')
    prob = h1 / N
    plt.stem(b1, prob)
    # Graph labels
    plt.title('PMF for an unfair ' + str(len(p)) + '-sided die')
    plt.xlabel('Number on the face of the die')
    plt.ylabel('Probability')
    plt.xticks(b1)
    plt.show()


main()
