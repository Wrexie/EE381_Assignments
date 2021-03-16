import numpy as np
import matplotlib.pyplot as plt


# Function that rolls an n-sided die with a given probability vector
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


# Main function
def main():
    # Probability vector provided
    p = [0.2, 0.1, 0.15, 0.3, 0.2, 0.05]
    # N - number of times to repeat experiment
    N = 10000
    # n - number of times to roll the 3 dice
    n = 1000
    # Empty array to store results
    s = np.zeros((N, 1))
    # Keeps count of successful experiments
    successCount = 0

    print("This might take a few minutes since there are a lot of trials....")

    # For loop where experiment is ran for N times
    for i in range(N):
        # Reset success count to 0 after each experiment
        successCount = 0
        # Roll the 3 dice n times
        for j in range(n):
            die1 = nSidedDie(p)
            die2 = nSidedDie(p)
            die3 = nSidedDie(p)

            # Check if experiment was a success
            if die1 == 1 and die2 == 2 and die3 == 3:
                # Increment success count by 1
                successCount += 1

        # Store experiment result in array
        s[i] = successCount

    # Plotting code
    b = range(0, 12)
    sb = np.size(b)
    h1, bin_edges = np.histogram(s, bins=b)
    b1 = bin_edges[0:sb - 1]
    plt.close('all')
    prob = h1 / N
    plt.stem(b1, prob)
    # Graph labels
    plt.title('Bernoulli Trials: PMF - Experimental Results')
    plt.xlabel('Number of successes per 1000 rolls')
    plt.ylabel('Probability')
    plt.xticks(b1)

    plt.show()


main()
