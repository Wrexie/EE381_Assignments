import numpy as np
import matplotlib.pyplot as plt
import math


def gaussian(mu, sig, z):
    f = np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
    return f


def main():
    a = 1
    b = 4
    n = 1
    N = 10000
    # mean thickness of a single book = 2.5, standard deviation = .86
    stacks = [1, 5, 10, 15]
    for stack in stacks:
        s = np.random.uniform(a, b, stack)

        mu_s = np.mean(s)
        sig_s = np.std(s)

        print("Mean of stack of books of size", stack, ":", mu_s)
        print("Standard deviation of stack of books of size", stack, ":", sig_s)
        print()


    for stack in stacks:
        mu_x = (a + b) / 2
        sig_x = np.sqrt((b - a) ** 2 / 12)
        X = np.zeros((N, 1))
        for k in range(0, N):
            x = np.random.uniform(a, b, stack)
            w = np.sum(x)
            X[k] = w
        # Create bins and histogram
        nbins = 30  # Number of bins
        edgecolor = 'w'  # Color separating bars in the bargraph
        #
        bins = [float(x) for x in np.linspace(stack * a, stack * b, nbins + 1)]
        h1, bin_edges = np.histogram(X, bins, density=True)
        # Define points on the horizontal axis
        be1 = bin_edges[0:np.size(bin_edges) - 1]
        be2 = bin_edges[1:np.size(bin_edges)]
        b1 = (be1 + be2) / 2
        barwidth = b1[1] - b1[0]  # Width of bars in the bargraph
        plt.close('all')
        # PLOT THE BAR GRAPH
        fig1 = plt.figure(1)
        plt.bar(b1, h1, width=barwidth, edgecolor=edgecolor)
        title = "Probability Hisogram of S = ", stack, "books"
        plt.title(title)
        f = gaussian(mu_x * stack, sig_x * np.sqrt(stack), b1)
        plt.plot(b1, f, 'r')
        plt.show()

    return 0


main()

