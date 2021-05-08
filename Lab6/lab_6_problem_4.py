import numpy as np


# Function to simulate markov chain
# Takes number of steps, a list of all the state, a transition matrix and an initial state probability vector
# as parameters
def markovSimulation(steps, stateNameList, transitionMatrix, initialProbability):
    # generates the first state using the initial state probability vector
    currentState = np.random.choice(stateNameList, replace = True, p = initialProbability)
    # instantiates a list to record all states in the chain
    stateList = [currentState]

    # iterate through each step
    for i in range(steps):
        # for each step, iterate through the list of states
        for j in range(len(stateNameList)):
            # if the current state equals the current state of the list of states then...
            if currentState == stateNameList[j]:
                # generate a new state using the list of states and appropriate state probability from the matrix
                nextState = np.random.choice(stateNameList, replace=True, p=transitionMatrix[j])
                # set the current state equal to the newly generated state
                currentState = nextState
                # append the new state to the state list
                stateList.append(nextState)
                break

    # return the state list
    return stateList


# main function
def main():
    # state transition matrix
    P = [[1, 0, 0, 0, 0],
         [.3, 0, .7, 0, 0],
         [0, 1 / 2, 0, 1 / 2, 0],
         [0, 0, .6, 0, .4],
         [0, 0, 0, 0, 1]]

    # initial state proability vector
    initialProbability = [0, 0, 1, 0, 0]

    # list of states
    stateNameList = [0, 1, 2, 3, 4]

    # number of steps
    steps = 15

    # will hold single simulated 5-state markov chain
    fiveStateResult = []

    # number of times to generate chain
    N = 10000

    # counters for absorption by state 0 and state 4
    counter0 = 0
    counter4 = 0

    # run experiment N times
    for i in range(N):
        # generate new chain
        fiveStateResult = markovSimulation(steps, stateNameList, P, initialProbability)

        # increment counters
        if fiveStateResult[15] == 0:
            counter0 += 1
        elif fiveStateResult[15] == 4:
            counter4 += 1

    # print results
    print('Probability of chain ending in a 0:', counter0 / N)
    print('Probability of chain ending in a 4: ', counter4 / N)


main()
