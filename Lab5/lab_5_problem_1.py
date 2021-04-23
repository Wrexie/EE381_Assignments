import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt
import math


def main():
    N = 1500000
    mu = 55
    sigma = 5
    n = 200
    x = np.ones(n)
    deviationSamplesPlusA = np.ones(n)
    deviationSamplesMinusA = np.ones(n)
    deviationSamplesPlusB = np.ones(n)
    deviationSamplesMinusB = np.ones(n)
    meanSamples = np.ones(n)
    populationDist = np.random.normal(mu, sigma, N)

    for i in range(1, n):
        populationSample = np.random.choice(populationDist, i)
        x_bar = populationSample.mean()
        meanSamples[i] = x_bar

        std = sigma / math.sqrt(i)
        plusConfidenceA = mu + 1.96 * std
        deviationSamplesPlusA[i] = plusConfidenceA
        minusConfidenceA = mu - 1.96 * std
        deviationSamplesMinusA[i] = minusConfidenceA

        plusConfidenceB = mu + 2.58 * std
        deviationSamplesPlusB[i] = plusConfidenceB
        minusConfidenceB = mu - 2.58 * std
        deviationSamplesMinusB[i] = minusConfidenceB
        x[i] = i

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

