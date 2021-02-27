import numpy as np

# Generates a single bit of a message with given probabilities
def createMessageBit(bitProbability):
    cs = np.cumsum(bitProbability)
    cp = np.append(0, cs)
    n = len(bitProbability)
    m = np.random.rand()

    for i in range(n):
        if cp[i] < m <= cp[i + 1]:
            bit = i

    return bit

# Main function
def main():
    # Sent message bit probabilities
    p0 = [.6, .4]
    # Received message probabilities for S = 0
    e0 = [.95, .05]
    # Received message probabilities for S = 1
    e1 = [.03, .97]
    # Number of times to run experiment
    N = 100000
    # Holds amount of times experiment failed
    failureCount = 0

    # Sends 1 message and receives 1 in return comparing if
    # the sent message and the received message are the same
    for i in range(N):
        # Create message
        S = createMessageBit(p0)

        # Evaluate if sent message is equal to 1 or 0
        if S == 1:
            # Generate received message using probability e1 if
            # sent message = 1
            R = createMessageBit(e1)
        elif S == 0:
            # Generate received message using probability e0 if
            # sent message = 0
            R = createMessageBit(e0)

        # Compare if S and R are not equal to each other
        if S != R:
            # Keep track of how many times the experiment fails
            failureCount += 1

    # Print results
    print("Probability that message will be received incorrectly is:", failureCount / N)


main()
