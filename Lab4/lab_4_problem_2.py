import numpy as np
import matplotlib.pyplot as plt


def main():
    a = 1
    b = 4
    n = 10
    x = np.random.uniform(a, b, 10)

    mu_w = np.mean(x)
    sig_w = np.std(x)

    print(mu_w)
    print(sig_w)
    return 0


main()

