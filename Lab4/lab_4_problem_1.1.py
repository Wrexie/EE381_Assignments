import numpy as np
import matplotlib.pyplot as plt


def UnifPDF(a, b, x):
    f = (1/abs(b-a))*np.ones(np.size(x))
    return f


def main():
    a = 1
    b = 4
    n = 10000
    x = np.random.uniform(a, b, n)

    nbins = 30  # Number of bins
    edgecolor = 'w'  # Color separating bars in the bargraph
    #
    bins = [float(x) for x in np.linspace(a, b, nbins + 1)]
    h1, bin_edges = np.histogram(x, bins, density=True)
    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges) - 1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]  # Width of bars in the bargraph
    plt.close('all')
    # PLOT THE BAR GRAPH
    fig1 = plt.figure(1)
    plt.bar(b1, h1, width=barwidth, edgecolor=edgecolor)

    f = UnifPDF(a, b, b1)
    plt.plot(b1, f, 'r')

    plt.title('Experimental Values of X')
    plt.legend(['PDF of X'])
    plt.show()

    mu_x = np.mean(x)
    sig_x = np.std(x)

    print("Mean of X: ", mu_x)
    print("Standard Deviation of X: ", sig_x)

    return 0


main()

