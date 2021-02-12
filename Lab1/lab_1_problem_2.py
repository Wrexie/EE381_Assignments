import numpy as np
import random
import matplotlib.pyplot as plt


def sum2dice(N):
    rollCount = 0
    s = 0

    for i in range(N):
        while s != 7:
            d1 = np.random.randint(1, 7)
            d2 = np.random.randint(1, 7)
            s = d1 + d2
            rollCount += 1

    '''
    b = range(1, 22)
    sb = np.size(b)
    h1, bin_edges = np.histogram(s, bins=b)
    b1 = bin_edges[0:sb - 1]
    plt.close('all')
    #
    fig1 = plt.figure(1)
    plt.stem(b1, h1)
    plt.title('Stem plot - Sum of two dice')
    plt.xlabel('Sum of two dice')
    plt.ylabel('Number of occurrences')
    fig1.savefig('1 EE381 Proj Stoch Exper-1.jpg')  #
    fig2 = plt.figure(2)
    p1 = h1 / N
    plt.stem(b1, p1)
    plt.title('Stem plot - Sum of two dice: Probability mass function')
    plt.xlabel('Sum of two dice')
    plt.ylabel('Probability')
    plt.show()
    '''



def main():
    N = 100000
    sum2dice(N)

main()
