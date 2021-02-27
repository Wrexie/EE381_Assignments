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

# Counts the number of times a number 'x' is in an array 'arr' recursively
def countReps(arr, x):
    # Variable to keep track of how many times 'x' is in 'arr'
    xCount = 0
    # If array is empty then return 0
    if len(arr) == 0:
        return 0
    # If the first element in the array = x then increment xCount
    if x == arr[0]:
        xCount += 1

    # Function calls itself on the remaining portion of the array
    # and result is added to xCount which is returned once the
    # end of the array is reached
    return xCount + countReps(arr[1:], x)

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
    # Keeps track of how many times the experiment is a success
    successCount = 0

    # Experiment loop that runs N times
    for i in range(N):
        # Generate message to be sent using p0
        S = createMessageBit(p0)

        # Evaluate if S = 1 or S = 0
        if S == 1:
            # If S = 1 then generate 3 R messages using e1 and
            # add them to an array
            R1 = createMessageBit(e1)
            R2 = createMessageBit(e1)
            R3 = createMessageBit(e1)
            rArr = [R1, R2, R3]
        elif S == 0:
            # If S = 0 then generate 3 R messages using e0 and
            # add them to an array
            R1 = createMessageBit(e0)
            R2 = createMessageBit(e0)
            R3 = createMessageBit(e0)
            rArr = [R1, R2, R3]

        # Use voting and majority rule to decide what bit S was
        # originally transmitted.
        # Check if 0 shows up more than twice in our array of R's
        # and if S = 0
        if countReps(rArr, 0) >= 2 and S == 0:
            # If our array of R's contains mostly 0's and S = 0
            # then the experiment was a success
            successCount += 1
        # Check if 1 shows up more than twice in our array of R's
        # and if S = 1
        if countReps(rArr, 1) >= 2 and S == 1:
            # If our array of R's contains mostly 1's and S = 1
            # then the experiment was a success
            successCount += 1

    # Calculate failure count using N and the success count
    failureCount = N - successCount

    # Print results
    print("Probability that S will be received and decoded incorrectly is: ", failureCount / N)


main()
