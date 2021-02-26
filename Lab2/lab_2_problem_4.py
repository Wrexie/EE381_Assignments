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


def countReps(arr, x):
    xCount = 0
    if len(arr) == 0:
        return 0
    if x == arr[0]:
        xCount += 1

    return xCount + countReps(arr[1:], x)


def main():
    p0 = [.6, .4]
    e0 = [.95, .05]
    e1 = [.03, .97]
    N = 100000
    successCount = 0

    for i in range(N):
        S = createMessageBit(p0)
        if S == 1:
            R1 = createMessageBit(e1)
            R2 = createMessageBit(e1)
            R3 = createMessageBit(e1)
            rArr = [R1, R2, R3]
        elif S == 0:
            R1 = createMessageBit(e0)
            R2 = createMessageBit(e0)
            R3 = createMessageBit(e0)
            rArr = [R1, R2, R3]

        if countReps(rArr, 0) >= 2 and S == 0:
            successCount += 1
        if countReps(rArr, 1) >= 2 and S == 1:
            successCount += 1

    failureCount = N - successCount

    print("Probability that S will be received and decoded incorrectly is: ", failureCount / N)


main()
