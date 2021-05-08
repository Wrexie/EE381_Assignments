import numpy as np
import matplotlib.pyplot as plt
import math


# main
def main():
    # number of bearings
    N = 1500000
    # mean
    mu = 55
    # standard deviation
    sigma = 5
    # samples
    n = 200
    # array to record sample sizes
    x = np.ones(n)

    # arrays for confidence intervals
    deviationSamplesPlusA = np.ones(n)
    deviationSamplesMinusA = np.ones(n)
    deviationSamplesPlusB = np.ones(n)
    deviationSamplesMinusB = np.ones(n)
    # array to hold mean of samples
    meanSamples = np.ones(n)
    # create N bearings with given mean and standard deviation
    populationDist = np.random.normal(mu, sigma, N)

    # iterate from n = 1... 200
    for i in range(1, n):
        # select n random bearings from the N bearings
        populationSample = np.random.choice(populationDist, i)
        # calculate mean of sample
        x_bar = populationSample.mean()
        # record mean
        meanSamples[i] = x_bar

        # calculate standard deviation
        std = sigma / math.sqrt(i)
        # calculate 95% confidence interval
        plusConfidenceA = mu + 1.96 * std
        deviationSamplesPlusA[i] = plusConfidenceA
        minusConfidenceA = mu - 1.96 * std
        deviationSamplesMinusA[i] = minusConfidenceA

        # calculate 99% confidence interval
        plusConfidenceB = mu + 2.58 * std
        deviationSamplesPlusB[i] = plusConfidenceB
        minusConfidenceB = mu - 2.58 * std
        deviationSamplesMinusB[i] = minusConfidenceB
        # record sample size
        x[i] = i

    # plot both graphs of sample means and confidence intervals
    plot1 = plt.figure(1)
    plt.scatter(x, meanSamples, marker="x", color="blue")
    plt.hlines(mu, 0, n, color="black")
    plt.xlim(1, 200)
    plt.ylim(45, 65)
    plt.xlabel("Sample size (n)")
    plt.ylabel("Mean of sample(X bar)")
    plt.plot(deviationSamplesPlusA, color="red")
    plt.plot(deviationSamplesMinusA, color="red")
    plt.title("Sample Means and 95% Confidence Interval")

    plot1 = plt.figure(2)
    plt.scatter(x, meanSamples, marker="x", color="blue")
    plt.hlines(mu, 0, n, color="black")
    plt.xlim(1, 200)
    plt.ylim(45, 65)
    plt.xlabel("Sample size (n)")
    plt.ylabel("Mean of sample(X bar)")
    plt.plot(deviationSamplesPlusB, color="red")
    plt.plot(deviationSamplesMinusB, color="red")
    plt.title("Sample Means and 99% Confidence Interval")

    plt.show()


main()

