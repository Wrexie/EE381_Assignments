import numpy as np
import matplotlib.pyplot as plt
import math


# Function to calculate normal PDF
def gaussian(mu, sig, z):
    f = np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
    return f


# Main
def main():
    # Beta
    B = 40
    # Experiment trials
    N = 10000
    # Empty array to store results of each carton
    T = np.ones(N)
    # Mu and sigma of c
    mu_c = 24 * B
    sig_c = B * math.sqrt(24)

    # Run experiment N times
    for i in range(N):
        # Create a carton with 24 batteries
        carton = np.random.exponential(B, 24)
        # Calculate C
        C = np.sum(carton)
        # Record results
        T[i] = C

    # Plotting code
    nbins = 30  # Number of bins
    edgecolor = 'w'  # Color separating bars in the bargraph
    #
    bins = [float(x) for x in np.linspace(300, 2000, nbins + 1)]
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

    # Plot PDF
    f = gaussian(mu_c, sig_c, b1)
    plt.plot(b1, f, 'r')
    plt.title('PDF of lifetime of a 24 battery carton')
    plt.xlabel('Lifetime of a 24 battery carton')
    plt.ylabel('Probability')

    # Plot CDF
    fig2 = plt.figure(2)
    h2 = np.cumsum(h1) * barwidth
    plt.bar(b1, h2, width=barwidth, edgecolor=edgecolor)
    plt.title('CDF of lifetime of a 24 battery carton')
    plt.xlabel('Lifetime of a 24 battery carton')
    plt.ylabel('CDF')

    plt.show()

    return 0


main()

