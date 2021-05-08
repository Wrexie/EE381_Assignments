import numpy as np
import matplotlib.pyplot as plt
import collections


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
    P = np.array([[.5, .25, .25],
                  [.5, 0, .5],
                  [.25, .25, .5]
                  ])

    # copy of state transition matrix
    exp = np.array([[.5, .25, .25],
                  [.5, 0, .5],
                  [.25, .25, .5]
                  ])

    # initial state probability vector
    initialProbability = [.25, 0, .75]
    # list of states
    stateNameList = ['R', 'N', 'S']

    # number of steps to simulate
    steps = 15
    # number of times to simulate experiment
    N = 10000

    # list of numbers representing the steps
    stepNumberList = np.arange(0, steps + 1, 1)

    # used record how many times each state occurs each step
    countR = np.zeros(steps + 1)
    countN = np.zeros(steps + 1)
    countS = np.zeros(steps + 1)


    # single weather forecast for 15 days
    weatherForecast = markovSimulation(steps, stateNameList, P, initialProbability)

    # plotting code for single simulation run of 3 state markov chain
    plot = plt.figure(1)
    plt.plot(stepNumberList, weatherForecast, 'go--', linestyle = 'solid', color = 'black')
    plt.xticks(np.arange(0, steps + 1, 1.0))
    plt.title("Single 15 Step Markov Chain Simulation")
    plt.xlabel("Step Number")
    plt.ylabel("State")

    # 10000 15 day weather forecasts
    for i in range(N):
        # generate new chain each iteration
        weatherForecast = markovSimulation(steps, stateNameList, P, initialProbability)

        # increment state counters
        for j in range(steps + 1):
            if weatherForecast[j] == 'R':
                countR[j] += 1
            elif weatherForecast[j] == 'S':
                countS[j] += 1
            elif weatherForecast[j] == 'N':
                countN[j] += 1

    # calculate probability vector of each state
    probR = countR / N
    probN = countN / N
    probS = countS / N

    # plotting code for simulated 3 state markov chain
    plot = plt.figure(2)
    plt.plot(stepNumberList, probR, 'go--', linestyle = 'solid', color = 'red')
    # plt.legend(['Probability of R'])
    plt.plot(stepNumberList, probN, 'go--', linestyle = 'solid', color = 'blue')
    # plt.legend(['Probability of N'])
    plt.plot(stepNumberList, probS, 'go--', linestyle = 'solid', color = 'green')
    plt.legend(['Probability of R', 'Probability of N', 'Probability of S'])
    plt.xticks(np.arange(0, steps + 1, 1.0))
    plt.yticks(np.arange(0, 1, .05))
    plt.title("Simulated 3-state Markov Chain")
    plt.xlabel("Step Number")
    plt.ylabel("Probability")

    # iterate through each step
    for i in range(steps + 1):
        # if step is 0 then the probability for each state at that step is just their initial probability
        if i == 0:
            probR[i] = initialProbability[i]
            probN[i] = initialProbability[i + 1]
            probS[i] = initialProbability[i + 2]

        # if step is 1 then the probability for each state at that step is based on their initial probability
        elif i == 1:
            # calculate probability for R occurring at step 1
            probR[i] = (probR[i - 1] * P[0][0]) \
                       + (probN[i - 1] * P[1][0]) \
                       + (probS[i - 1] * P[2][0])

            # calculate probability for N occurring at step 1
            probN[i] = (probR[i - 1] * P[0][1]) \
                       + (probN[i - 1] * P[1][1]) \
                       + (probS[i - 1] * P[2][1])

            # calculate probability for S occurring at step 1
            probS[i] = (probR[i - 1] * P[0][2]) \
                       + (probN[i - 1] * P[1][2]) \
                       + (probS[i - 1] * P[2][2])

        # if step is not 0 or 1 then...
        else:
            # multiply the state transition matrix by itself each step to receive the state transition probabilities
            # for that step
            exp = np.matmul(P, exp)

            # calculate probabilty of each state
            probR[i] = (exp[0][0] + exp[1][0] + exp[2][0]) / 3
            probN[i] = (exp[0][1] + exp[1][1] + exp[2][1]) / 3
            probS[i] = (exp[0][2] + exp[1][2] + exp[2][2]) / 3

    # plotting code for calculated 3 state markov chain
    plot = plt.figure(3)
    plt.plot(stepNumberList, probR, 'go--', linestyle = 'solid', color = 'red')
    plt.plot(stepNumberList, probN, 'go--', linestyle = 'solid', color = 'blue')
    plt.plot(stepNumberList, probS, 'go--', linestyle = 'solid', color = 'green')
    plt.legend(['Probability of R', 'Probability of N', 'Probability of S'])
    plt.xticks(np.arange(0, steps + 1, 1.0))
    plt.yticks(np.arange(0, 1, .05))
    plt.title("Calculated 3-state Markov Chain")
    plt.xlabel("Step Number")
    plt.ylabel("Probability")
    plt.show()
    return 0


main()
