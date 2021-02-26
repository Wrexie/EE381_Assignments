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
    e0 = [.95, .05]
    e1 = [.03, .97]
    N = 100000
    successCount = 0
    rOneCount = 0

    for i in range(N):
        S = createMessageBit(p0)
        if S == 1:
            R = createMessageBit(e1)
        elif S == 0:
            R = createMessageBit(e0)

        if R == 1:
            rOneCount += 1
            if S == R:
                successCount += 1

    print("Probability that if message received is 1, then the message sent was 1 originally is:",
          successCount / rOneCount)


main()
