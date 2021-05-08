import numpy as np
import matplotlib.pyplot as plt

def markovSimulation(steps, stateNameList, transitionMatrix, initialProbability):
    currentState = np.random.choice(stateNameList, replace = True, p = initialProbability)
    stateList = [currentState]

    for i in range(steps):
        if currentState == 'R':
            nextState = np.random.choice(stateNameList, replace = True, p = transitionMatrix[0])
            currentState = nextState
            stateList.append(nextState)

        elif currentState == 'N':
            nextState = np.random.choice(stateNameList, replace = True, p = transitionMatrix[1])
            currentState = nextState
            stateList.append(nextState)

        elif currentState == 'S':
            nextState = np.random.choice(stateNameList, replace = True, p = transitionMatrix[2])
            currentState = nextState
            stateList.append(nextState)

    return stateList

def main():
    P = np.array([[.5, .25, .25],
                  [.5, 0, .5],
                  [.25, .25, .5]
                  ])

    initialProbability = [.25, 0, .75]
    stateNameList = ['R', 'N', 'S']

    steps = 15
    N = 10000

    weatherForecastList = []
    countR = np.zeros(steps + 1)
    countN = np.zeros(steps + 1)
    countS = np.zeros(steps + 1)

    # single weather forecast for 15 days
    weatherForecast = markovSimulation(steps, stateNameList, P, initialProbability)
    stepNumberList = np.arange(0, steps + 1, 1)

    plot = plt.figure(1)
    plt.plot(stepNumberList, weatherForecast, 'go--', linestyle = 'solid', color = 'black')
    plt.xticks(np.arange(0, steps + 1, 1.0))
    plt.title("Single 15 Step Markov Chain Simulation")
    plt.xlabel("Step Number")
    plt.ylabel("State")

    # 10000 15 day weather forecasts
    for i in range(N):
        weatherForecast = markovSimulation(steps, stateNameList, P, initialProbability)
        for j in range(steps + 1):
            if weatherForecast[j] == 'R':
                countR[j] += 1
            elif weatherForecast[j] == 'S':
                countS[j] += 1
            elif weatherForecast[j] == 'N':
                countN[j] += 1
        # weatherForecastList.append(weatherForecast)

    probR = countR / N
    probN = countN / N
    probS = countS / N

    plot = plt.figure(2)
    plt.plot(stepNumberList, probR, 'go--', linestyle = 'solid', color = 'black')
    plt.plot(stepNumberList, probN, 'go--', linestyle = 'solid', color = 'black')
    plt.plot(stepNumberList, probS, 'go--', linestyle = 'solid', color = 'black')
    plt.yticks(np.arange(0, 1, .25))
    plt.title("Simulated 3-state Markov Chain")
    plt.xlabel("Step Number")
    plt.ylabel("Probability")

    for k in range(steps):
        print(P)
        for i in range(len(P)):
            for j in range(len(P[i])):
                P[i][j] *= P[i][j]
    print(P)

    plt.show()
    return 0


main()
