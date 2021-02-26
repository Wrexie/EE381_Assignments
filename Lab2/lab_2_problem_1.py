import numpy as np

def createMessageBit(bitProbability):
    cs = np.cumsum(bitProbability)
    cp = np.append(0, cs)
    n = len(bitProbability)
    bit = 0
    m = np.random.rand()

    for i in range(n):
        if m <= cp[i]:
            bit = 0
        elif m > cp[i]:
            bit = 1

    return bit


def main():
    pArr = [.6, .4]
    print(createMessageBit(pArr))
    return 0

main()