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
    # Keeps track of how many times experiment was a success
    successCount = 0
    # Keeps track of how many times R = 1
    rOneCount = 0

    # Experiment loop that runs N times
    for i in range(N):
        # Create message to be sent using p0
        S = createMessageBit(p0)

        # Evaluate if S = 1 or if S = 0
        if S == 1:
            # If S = 1 then generate a received message using e1
            R = createMessageBit(e1)
        elif S == 0:
            # If S = 0 then generate a received message using e0
            R = createMessageBit(e0)

        # Check if R = 1 since these are the messages we are focusing on for
        # this experiment
        if R == 1:
            # Keep track of how many times R = 1
            rOneCount += 1
            # Evaluate if S = R, if they do then add 1 to our successCount variable
            if S == R:
                successCount += 1

    # Print results
    print("Probability that if message received is 1, then the message sent was 1 originally is:",
          successCount / rOneCount)


main()
