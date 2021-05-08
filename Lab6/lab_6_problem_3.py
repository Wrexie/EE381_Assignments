import numpy as np
import matplotlib.pyplot as plt


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
         [0, 1/2, 0, 1/2, 0],
         [0, 0, .6, 0, .4],
         [0, 0, 0, 0, 1]]

    # initial state probability vector
    initialProbability = [.2, .2, .2, .2, .2]
    # list of states
    stateNameList = [0, 1, 2, 3, 4]

    # number of steps
    steps = 15
    # will hold single simulated 5 state markov chain
    fiveStateResult = [0]

    # list of numbers representing number of steps
    stepNumberList = np.arange(0, steps + 1, 1)

    # simulate new 5-state chain until one that is absorbed by state 4 is generated
    while True:
        fiveStateResult = markovSimulation(steps, stateNameList, P, initialProbability)
        if fiveStateResult[15] == 4 and fiveStateResult[0] != 4:
            plot = plt.figure(1)
            plt.plot(stepNumberList, fiveStateResult, 'go--', linestyle='solid', color='black')
            plt.xticks(np.arange(0, steps + 1, 1.0))
            plt.title("Single 15 Step Absorbing Markov Chain Simulation")
            plt.xlabel("Step Number")
            plt.ylabel("State")
            plt.yticks(np.arange(0, 5, 1))
            plt.show()
            break

    # simulate new 5-state chain until one that is absorbed by state 0 is generated
    while True:
        fiveStateResult = markovSimulation(steps, stateNameList, P, initialProbability)
        if fiveStateResult[15] == 0 and fiveStateResult[0] != 0:
            plot = plt.figure(1)
            plt.plot(stepNumberList, fiveStateResult, 'go--', linestyle='solid', color='black')
            plt.xticks(np.arange(0, steps + 1, 1.0))
            plt.title("Single 15 Absorbing Step Markov Chain Simulation")
            plt.xlabel("Step Number")
            plt.ylabel("State")
            plt.yticks(np.arange(0, 5, 1))
            plt.show()
            break


main()
