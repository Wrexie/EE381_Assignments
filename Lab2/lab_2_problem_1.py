import numpy as np


def createMessageBit(bitProbability):
    cs = np.cumsum(bitProbability)
    cp = np.append(0, cs)
    n = len(bitProbability)
    m = np.random.rand()

    for i in range(n):
        if cp[i] < m <= cp[i + 1]:
            bit = i

    return bit


def main():
    p0 = [.6, .4]
    e0 = [.5, .5]
    e1 = [.3, .7]
    N = 100000
    failureCount = 0

    for i in range(N):
        S = createMessageBit(p0)
        if S == 1:
            R = createMessageBit(e1)
        elif S == 0:
            R = createMessageBit(e0)

        if S != R:
            failureCount += 1

    print("Probability that message will be received incorrectly is:", failureCount / N)


main()
