import numpy as np
import matplotlib.pyplot as plt
import math


def ExpPDF(B, x):
    f = np.ones(np.size(x))
    for i in range(np.size(x)):
        f[i] = (1/B * math.exp(-(1/B) * x[i]))
    return f


def main():
    B = 40
    n = 10000
    T = np.random.exponential(B, n)

    nbins = 30  # Number of bins
    edgecolor = 'w'  # Color separating bars in the bargraph
    #
    bins = [float(x) for x in np.linspace(0, B, nbins + 1)]
    h1, bin_edges = np.histogram(T, bins, density=True)
    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges) - 1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]  # Width of bars in the bargraph
    plt.close('all')
    # PLOT THE BAR GRAPH
    fig1 = plt.figure(1)
    plt.bar(b1, h1, width=barwidth, edgecolor=edgecolor)

    f = ExpPDF(B, b1)
    plt.plot(b1, f, 'r')
    plt.show()

    mu_t = np.mean(T)
    sig_t = np.std(T)

    print("Mean of T: ", mu_t)
    print("Standard Deviation of T: ", sig_t)

    return 0


main()

