import numpy as np
import matplotlib.pyplot as plt
import math


# Function that calculates normal PDF
def NormPDF(m, s, x):
    f = np.ones(np.size(x))
    for i in range(np.size(x)):
        f[i] = (1/(s*math.sqrt(2*math.pi)))*math.exp(-((x[i]-m)**2)/(2*s**2))
    return f


# main
def main():
    mu = 2.5
    sig = .75
    n = 10000
    # Array of random normal variables
    x = np.random.normal(mu, sig, n)

    # Plotting code
    nbins = 30  # Number of bins
    edgecolor = 'w'  # Color separating bars in the bargraph
    #
    bins = [float(x) for x in np.linspace(sig, mu, nbins + 1)]
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

    f = NormPDF(mu,sig, b1)
    plt.plot(b1, f, 'r')
    plt.title("Experimental Values of X")
    plt.legend(['PDF of X'])
    plt.show()

    # Mu and sigma of X
    mu_x = np.mean(x)
    sig_x = np.std(x)

    print("Mean of x: ", mu_x)
    print("Standard Deviation of x: ", sig_x)

    return 0

main()

