import numpy as np


# Function that tosses a given number of coins
def tossCoins(N):
    heads, tails = 0, 0
    coin = np.random.randint(0, 2, N)
    heads = sum(coin)
    tails = N - heads

    results = [heads, tails]
    return results


# Main function
def main():
    # Will keep track of the number of times the
    # experiment is a success
    successCount = 0
    # Repetitions of experiment
    N = 100000
    for i in range(N):
        result = tossCoins(100)
        if result[0] == 50:
            successCount += 1

    print("Probability of getting 50 heads: ")
    print(successCount / N)


main()
