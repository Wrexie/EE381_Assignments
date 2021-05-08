import numpy as np
import math


# main
def main():
    # number of bearings
    N = 1500000
    # mean
    mu = 55
    # standard deviation
    sigma = 5
    # array of sample sizes to test
    sampleSizes = [5, 40, 120]
    # generate N bearings using given mean and standard deviation
    populationDist = np.random.normal(mu, sigma, N)
    # amount ot times to do experiment
    M = 10000

    confidenceIntervalType = [95, 99]

    # iterate through each sample size in array
    for n in sampleSizes:
        # instantiate success counter for both normal and t distribution
        normalDistributionSuccess = 0.0
        tDistributionSuccess = 0.0

        # if sample size is 5 then...
        if(n == 5):
            print("Sample size %d" % n)
            # iterate through confidence interval array
            for interval in confidenceIntervalType:
                # if interval is 95% then...
                if interval == 95:
                    # run experiment M times
                    for i in range(M):
                        # select n random bearings as sample
                        sample = np.random.choice(populationDist, n)
                        # calculate mean of sample
                        sampleMean = sample.mean()
                        # calculate standard deviation of sample
                        std = sigma / math.sqrt(n)
                        # calculate normal distribution confidence interval
                        upperConfidenceNormal = mu + 1.96 * std
                        lowerConfidenceNormal = mu - 1.96 * std

                        # calculate t distribution confidence interval
                        upperConfidenceT = mu + 2.78 * std
                        lowerCondidenceT = mu - 2.78 * std

                        # if mean is in the interval then experiment was a success
                        if upperConfidenceNormal >= sampleMean >= lowerConfidenceNormal:
                            normalDistributionSuccess += 1
                        if upperConfidenceT >= sampleMean >= lowerCondidenceT:
                            tDistributionSuccess += 1

                    print("95% Confidence Interval test:")
                    print("    Number of successes of normal distribution of sample size %d: %d" % (n, normalDistributionSuccess))
                    print("    Success percentage of normal distribution: %.2f" % ((normalDistributionSuccess/M) * 100))
                    print("    Number of successes of t distribution of sample size %d: %d" % (n, tDistributionSuccess))
                    print("    Success percentage of t distribution: %.2f" % ((tDistributionSuccess/M) * 100))

                # if interval is 99% then...
                if interval == 99:
                    # run experiment M times
                    for i in range(M):
                        # select n random bearings as sample
                        sample = np.random.choice(populationDist, n)
                        # calculate mean of sample
                        sampleMean = sample.mean()
                        # calculatea standard deviation of sample
                        std = sigma / math.sqrt(n)
                        # calculate normal distribution confidence interval
                        upperConfidenceNormal = mu + 2.58 * std
                        lowerConfidenceNormal = mu - 2.58 * std

                        # calculate t distribution confidence interval
                        upperConfidenceT = mu + 4.60 * std
                        lowerCondidenceT = mu - 4.60 * std

                        # if mean is in the interval then experiment was a success
                        if upperConfidenceNormal >= sampleMean >= lowerConfidenceNormal:
                            normalDistributionSuccess += 1
                        if upperConfidenceT >= sampleMean >= lowerCondidenceT:
                            tDistributionSuccess += 1

                    print("99% Confidence Interval test:")
                    print("    Number of successes of normal distribution of sample size %d: %d" % (n, normalDistributionSuccess))
                    print("    Success percentage of normal distribution: %.2f" % ((normalDistributionSuccess/M) * 100))
                    print("    Number of successes of t distribution of sample size %d: %d" % (n, tDistributionSuccess))
                    print("    Success percentage of t distribution: %.2f" % ((tDistributionSuccess/M) * 100))

                # reset success counters for each interval
                normalDistributionSuccess = 0.0
                tDistributionSuccess = 0.0

        # exact same process as for sample 5 but with sample size 40
        if (n == 40):
            print("Sample size %d" % n)
            for interval in confidenceIntervalType:
                if interval == 95:
                    for i in range(M):
                        sample = np.random.choice(populationDist, n)
                        sampleMean = sample.mean()
                        std = sigma / math.sqrt(n)
                        upperConfidenceNormal = mu + 1.96 * std
                        lowerConfidenceNormal = mu - 1.96 * std

                        upperConfidenceT = mu + 2.02 * std
                        lowerCondidenceT = mu - 2.02 * std

                        if upperConfidenceNormal >= sampleMean >= lowerConfidenceNormal:
                            normalDistributionSuccess += 1
                        if upperConfidenceT >= sampleMean >= lowerCondidenceT:
                            tDistributionSuccess += 1

                    print("95% Confidence Interval test:")
                    print("    Number of successes of normal distribution of sample size %d: %d" % (n, normalDistributionSuccess))
                    print("    Success percentage of normal distribution: %.2f" % ((normalDistributionSuccess / M) * 100))
                    print("    Number of successes of t distribution of sample size %d: %d" % (n, tDistributionSuccess))
                    print("    Success percentage of t distribution: %.2f" % ((tDistributionSuccess / M) * 100))

                if interval == 99:
                    for i in range(M):
                        sample = np.random.choice(populationDist, n)
                        sampleMean = sample.mean()
                        std = sigma / math.sqrt(n)
                        upperConfidenceNormal = mu + 2.58 * std
                        lowerConfidenceNormal = mu - 2.58 * std

                        upperConfidenceT = mu + 2.704 * std
                        lowerCondidenceT = mu - 2.704 * std

                        if upperConfidenceNormal >= sampleMean >= lowerConfidenceNormal:
                            normalDistributionSuccess += 1
                        if upperConfidenceT >= sampleMean >= lowerCondidenceT:
                            tDistributionSuccess += 1

                    print("99% Confidence Interval test:")
                    print("    Number of successes of normal distribution of sample size %d: %d" % (n, normalDistributionSuccess))
                    print("    Success percentage of normal distribution: %.2f" % ((normalDistributionSuccess / M) * 100))
                    print("    Number of successes of t distribution of sample size %d: %d" % (n, tDistributionSuccess))
                    print("    Success percentage of t distribution: %.2f" % ((tDistributionSuccess / M) * 100))

                normalDistributionSuccess = 0.0
                tDistributionSuccess = 0.0

        # exact same process but with sample size 120
        if (n == 120):
            print("Sample size %d" % n)
            for interval in confidenceIntervalType:
                if interval == 95:
                    for i in range(M):
                        sample = np.random.choice(populationDist, n)
                        sampleMean = sample.mean()
                        std = sigma / math.sqrt(n)
                        upperConfidenceNormal = mu + 1.96 * std
                        lowerConfidenceNormal = mu - 1.96 * std

                        upperConfidenceT = mu + 1.98 * std
                        lowerCondidenceT = mu - 1.98 * std

                        if upperConfidenceNormal >= sampleMean >= lowerConfidenceNormal:
                            normalDistributionSuccess += 1
                        if upperConfidenceT >= sampleMean >= lowerCondidenceT:
                            tDistributionSuccess += 1

                    print("95% Confidence Interval test:")
                    print("    Number of successes of normal distribution of sample size %d: %d" % (n, normalDistributionSuccess))
                    print("    Success percentage of normal distribution: %.2f" % ((normalDistributionSuccess / M) * 100))
                    print("    Number of successes of t distribution of sample size %d: %d" % (n, tDistributionSuccess))
                    print("    Success percentage of t distribution: %.2f" % ((tDistributionSuccess / M) * 100))

                if interval == 99:
                    for i in range(M):
                        sample = np.random.choice(populationDist, n)
                        sampleMean = sample.mean()
                        std = sigma / math.sqrt(n)
                        upperConfidenceNormal = mu + 2.58 * std
                        lowerConfidenceNormal = mu - 2.58 * std

                        upperConfidenceT = mu + 2.617 * std
                        lowerCondidenceT = mu - 2.617 * std

                        if upperConfidenceNormal >= sampleMean >= lowerConfidenceNormal:
                            normalDistributionSuccess += 1
                        if upperConfidenceT >= sampleMean >= lowerCondidenceT:
                            tDistributionSuccess += 1

                    print("99% Confidence Interval test:")
                    print("    Number of successes of normal distribution of sample size %d: %d" % (n, normalDistributionSuccess))
                    print("    Success percentage of normal distribution: %.2f" % ((normalDistributionSuccess / M) * 100))
                    print("    Number of successes of t distribution of sample size %d: %d" % (n, tDistributionSuccess))
                    print("    Success percentage of t distribution: %.2f" % ((tDistributionSuccess / M) * 100))

                normalDistributionSuccess = 0.0
                tDistributionSuccess = 0.0

        print()


main()

