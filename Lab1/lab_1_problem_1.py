import numpy
import random
import matplotlib.pyplot as plt


# Function that rolls an n-sided die with a given probability
# vector
def nSidedDie(p):
    cs = numpy.cumsum(p)
    cp = numpy.append(0, cs)
    n = len(p)
    d = 0
    r = random.random()
    for j in range(n):
        if r > cp[j] and r <= cp[j + 1]:
            d = j + 1

    return d


# Main function
def main():
    # Probability vector
    p = [0.10, 0.15, 0.20, 0.05, 0.30, 0.10, 0.10]
    # Repetitions of experiment
    N = 1000
    # Empty array to store results
    s = numpy.zeros((N, 1))
    for i in range(N):
        r = nSidedDie(p)
        s[i] = r

    # Plotting code
    b = range(1, len(p) + 2)
    sb = numpy.size(b)
    h1, bin_edges = numpy.histogram(s, bins=b)
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
