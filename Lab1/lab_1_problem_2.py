import numpy as np
import matplotlib.pyplot as plt


# Sums 2 dice and counts how many rolls it takes to get a sum of 7
# Does this N times
def sum2dice(N):
    rollCount = 0
    s = 0
    results = []

    for i in range(N):
        rollCount = 0
        while s != 7:
            d1 = np.random.randint(1, 7)
            d2 = np.random.randint(1, 7)
            s = d1 + d2
            rollCount += 1
        s = 0
        results.append(rollCount)

    return results


# Main function
def main():
    N = 10000
    results = sum2dice(N)

    # Stem plot code
    b = range(1, 22)
    sb = np.size(b)
    h1, bin_edges = np.histogram(results, bins=b)
    b1 = bin_edges[0: sb - 1]
    plt.close('all')

    plt.stem(b1, h1 / 10000)
    plt.title('Stem plot - Probability of Rolling a 7 from 2 Dice')
    plt.xlabel('Number of Rolls Needed for 7')
    plt.ylabel('Probability')
    plt.show()

main()