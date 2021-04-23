import numpy as np
import math


def main():
    N = 1500000
    mu = 55
    sigma = 5
    n = 5
    sampleSizes = [5, 40, 120]
    tValues = []
    populationDist = np.random.normal(mu, sigma, N)
    M = 10000
    normalDistributionSuccess = 0
    tDistributionSuccess = 0

    for n in sampleSizes:

        for i in range(M):
            sample = np.random.choice(populationDist, n)
            sampleMean = sample.mean()
            std = sigma / math.sqrt(n)
            upperConfidenceNormal = mu + 1.96 * std
            lowerConfidenceNormal = mu - 1.96 * std

            upperConfidenceT = mu + 2.78 * std
            lowerCondidenceT = mu - 2.78 * std

            if upperConfidenceNormal >= sampleMean >= lowerConfidenceNormal:
                normalDistributionSuccess += 1



    print(M/normalDistributionSuccess)
    return 0


main()

