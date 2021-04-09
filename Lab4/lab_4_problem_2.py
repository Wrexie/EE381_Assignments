import numpy as np
import matplotlib.pyplot as plt


def main():
    a = 1
    b = 4
    n = 10
    # mean thickness of a single book = 2.5, standard deviation = .86
    stacks = [1, 5, 10, 15]
    for stack in stacks:
        s = np.random.uniform(a, b, stack)

        mu_s = np.mean(s)
        sig_s = np.std(s)

        print("Mean of stack of books of size", stack, ":", mu_s)
        print("Standard deviation of stack of books of size", stack, ":", sig_s)
        print()


    return 0


main()

