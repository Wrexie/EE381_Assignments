import numpy as np
import math


def main():
    N = 1500000
    mu = 55
    sigma = 5
    n = 5
    sampleSizes = [5, 40, 120]
    populationDist = np.random.normal(mu, sigma, N)
    M = 10000
    normalDistributionSuccess = 0
    tDistributionSuccess = 0
    confidenceIntervalType = [95, 99]

    for n in sampleSizes:
        normalDistributionSuccess = 0
        if(n == 5):
            for interval in confidenceIntervalType:
                if interval == 95:
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
                        if upperConfidenceT >= sampleMean >= lowerCondidenceT:
                            tDistributionSuccess += 1
            print("95% Confidence Interval test:")
            print("    Number of successes of normal distribution of sample size %d: %d" % (n, normalDistributionSuccess))
            print("    Success percentage of normal distribution: %d" % ((normalDistributionSuccess/M) * 100))
            print("    Number of successes of t distribution of sample size %d: %d" % (n, tDistributionSuccess))
            print("    Success percentage of t distribution: %d" % ((tDistributionSuccess/M) * 100))

    return 0


main()

