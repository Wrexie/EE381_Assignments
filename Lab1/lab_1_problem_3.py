import numpy as np

def tossCoins(N):
    heads, tails = 0, 0
    coin = np.random.randint(0, 2, N)
    heads = sum(coin)
    tails = N - heads

    results = [heads, tails]
    return results

def main():
    successCount = 0
    N = 100000
    for i in range(N):
        result = tossCoins(100)
        if result[0] == 50:
            successCount += 1

    print(successCount)

main()