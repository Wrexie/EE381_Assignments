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
    # Received message bit probabilities for S = 0
    e0 = [.95, .05]
    # Received message bit probabilities for S = 1
    e1 = [.03, .97]
    # Number of times to run experiment
    N = 100000
    # Keeps track of how many times the experiment was a success
    successCount = 0
    # Keeps track of how many times S = 1
    sOneCount = 0

    # Experiment loop that runs N times
    for i in range(N):
        # Create message being sent using p0
        S = createMessageBit(p0)
        # Evaluate if sent message = 1
        if S == 1:
            # Keep track of how many times message being sent = 1
            sOneCount += 1
            # If message sent = 1 then generate a received message using e1
            R = createMessageBit(e1)
            # If S = R then the experiment was a success
            if S == R:
                successCount += 1

    # Print results
    print("Probability that message will be received correctly if S = 1 is:",
          successCount / sOneCount)


main()
