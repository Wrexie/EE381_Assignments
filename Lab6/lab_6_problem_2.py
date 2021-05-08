import numpy as np
import matplotlib.pyplot as plt


# main function
def main():
    # initial state probability vector list
    initialProbabilities = [[.2, .2, .2, .2, .2], [0, 0, 0, 0, 1]]

    # calculated state transition vector
    P = [[0, 1, 0, 0, 0],
         [.5, 0, .5, 0, 0],
         [1/3, 1/3, 0, 0, 1/3],
         [1, 0, 0, 0, 0],
         [0, 1/3, 1/3, 1/3, 0]]

    # copy of state transition vector
    exp = [[0, 1, 0, 0, 0],
         [.5, 0, .5, 0, 0],
         [1/3, 1/3, 0, 0, 1/3],
         [1, 0, 0, 0, 0],
         [0, 1/3, 1/3, 1/3, 0]]

    # number of steps
    steps = 20

    # list of numbers representing steps
    stepNumberList = np.arange(0, steps + 1, 1)

    # instantiate lists to be used to represent probability vectors for each state
    probA = np.zeros(steps + 1)
    probB = np.zeros(steps + 1)
    probC = np.zeros(steps + 1)
    probD = np.zeros(steps + 1)
    probE = np.zeros(steps + 1)

    # list to hold probability vectors of each state
    probList = []

    # list to hold probability vector results of each initial state probability vector
    probListFinal = []

    # iterate through each initial state probability vector
    for elem in initialProbabilities:
        # iterate through each step
        for i in range(steps + 1):
            # if we are at step 0 then probability for each state at that state is just their initial state probability
            if i == 0:
                probA[i] = elem[i]
                probB[i] = elem[i + 1]
                probC[i] = elem[i + 2]
                probD[i] = elem[i + 3]
                probE[i] = elem[i + 4]

            # if we are at step 1 then the probability for each state is based on their initial probability
            elif i == 1:
                # calculate probability of A occurring at step 1
                probA[i] = (probA[i - 1] * P[0][0]) \
                           + (probB[i - 1] * P[1][0]) \
                           + (probC[i - 1] * P[2][0])  \
                           + (probD[i - 1] * P[3][0]) \
                           + (probE[i - 1] * P[4][0])
                # calculate probability of B occurring at step 1
                probB[i] = (probA[i - 1] * P[0][1]) \
                           + (probB[i - 1] * P[1][1]) \
                           + (probC[i - 1] * P[2][1])  \
                           + (probD[i - 1] * P[3][1]) \
                           + (probE[i - 1] * P[4][1])
                # calculate probability of C occurring at step 1
                probC[i] = (probA[i - 1] * P[0][2]) \
                           + (probB[i - 1] * P[1][2]) \
                           + (probC[i - 1] * P[2][2])  \
                           + (probD[i - 1] * P[3][2]) \
                           + (probE[i - 1] * P[4][2])
                # calculate probability of D occurring at step 1
                probD[i] = (probA[i - 1] * P[0][3]) \
                           + (probB[i - 1] * P[1][3]) \
                           + (probC[i - 1] * P[2][3])  \
                           + (probD[i - 1] * P[3][3]) \
                           + (probE[i - 1] * P[4][3])
                # calculate probability of E occurring at step 1
                probE[i] = (probA[i - 1] * P[0][4]) \
                           + (probB[i - 1] * P[1][4]) \
                           + (probC[i - 1] * P[2][4])  \
                           + (probD[i - 1] * P[3][4]) \
                           + (probE[i - 1] * P[4][4])

            # if we are not at step 0 or 1 then...
            else:
                # multiple the state transition matrix by itself each step to receive the state transition probabilities
                # for that step
                exp = np.matmul(P, exp)

                # calculate probability of each state at current step
                probA[i] = (exp[0][0] + exp[1][0] + exp[2][0] + exp[3][0] + exp[4][0]) / 5
                probB[i] = (exp[0][1] + exp[1][1] + exp[2][1] + exp[3][1] + exp[4][1]) / 5
                probC[i] = (exp[0][2] + exp[1][2] + exp[2][2] + exp[3][2] + exp[4][2]) / 5
                probD[i] = (exp[0][3] + exp[1][3] + exp[2][3] + exp[3][3] + exp[4][3]) / 5
                probE[i] = (exp[0][4] + exp[1][4] + exp[2][4] + exp[3][4] + exp[4][4]) / 5

        # record each state probability vector
        probList.append(probA)
        probList.append(probB)
        probList.append(probC)
        probList.append(probD)
        probList.append(probE)

        # record probability vectors for current initial state probability vector
        probListFinal.append(probList)

        # reset state probability vector list to empty
        probList = []

        # reset each state probability vector
        probA = np.zeros(steps + 1)
        probB = np.zeros(steps + 1)
        probC = np.zeros(steps + 1)
        probD = np.zeros(steps + 1)
        probE = np.zeros(steps + 1)

    # plotting code for state probability vectors calculated from intial state probability vector v1
    plot = plt.figure(1)
    plt.plot(stepNumberList, probListFinal[0][0], 'go--', linestyle = 'solid', color = 'red')
    plt.plot(stepNumberList, probListFinal[0][1], 'go--', linestyle = 'solid', color = 'blue')
    plt.plot(stepNumberList, probListFinal[0][2], 'go--', linestyle = 'solid', color = 'green')
    plt.plot(stepNumberList, probListFinal[0][3], 'go--', linestyle = 'solid', color = 'orange')
    plt.plot(stepNumberList, probListFinal[0][4], 'go--', linestyle = 'solid', color = 'purple')
    plt.xticks(np.arange(0, steps + 1, 1))
    plt.yticks(np.arange(0, 1.1, .1))
    plt.title("Calculated 5-page Markov Chain\n with Initial State Probability Distribution Vector v1")
    plt.xlabel("Step Number")
    plt.ylabel("Probability")
    plt.legend(['Probability of A', 'Probability of B', 'Probability of C', 'Probability of D', 'Probability of E'])

    # plotting code for state probability vectors calculated from intial state probability vector v2
    plot = plt.figure(2)
    plt.plot(stepNumberList, probListFinal[1][0], 'go--', linestyle='solid', color='red')
    plt.plot(stepNumberList, probListFinal[1][1], 'go--', linestyle='solid', color='blue')
    plt.plot(stepNumberList, probListFinal[1][2], 'go--', linestyle='solid', color='green')
    plt.plot(stepNumberList, probListFinal[1][3], 'go--', linestyle='solid', color='orange')
    plt.plot(stepNumberList, probListFinal[1][4], 'go--', linestyle='solid', color='purple')
    plt.xticks(np.arange(0, steps + 1, 1))
    plt.yticks(np.arange(0, 1.1, .1))
    plt.title("Calculated 5-page Markov Chain\n with Initial State Probability Distribution Vector v2")
    plt.xlabel("Step Number")
    plt.ylabel("Probability")
    plt.legend(['Probability of A', 'Probability of B', 'Probability of C', 'Probability of D', 'Probability of E'])

    plt.show()

    # used to store calculated probability of each page being visited
    finalProbA = 0
    finalProbB = 0
    finalProbC = 0
    finalProbD = 0
    finalProbE = 0

    # iterate through the results for each initial state probability vector
    for j in range(len(probListFinal)):
        for i in range(steps + 1):
            finalProbA += probListFinal[j][0][i]
            finalProbB += probListFinal[j][1][i]
            finalProbC += probListFinal[j][2][i]
            finalProbD += probListFinal[j][3][i]
            finalProbE += probListFinal[j][4][i]

        # calculate final probability for each page
        finalProbA = finalProbA / 20
        finalProbB = finalProbB / 20
        finalProbC = finalProbC / 20
        finalProbD = finalProbD / 20
        finalProbE = finalProbE / 20

        # print results of page probabilities
        if j == 0:
            print("Probability of pages using initial state probability distribution vector v1")
        elif j == 1:
            print("Probability of pages using initial state probability distribution vector v2")
        print("Probability of Page A: ", finalProbA)
        print("Probability of Page B: ", finalProbB)
        print("Probability of Page C: ", finalProbC)
        print("Probability of Page D: ", finalProbD)
        print("Probability of Page E: ", finalProbE)
        print()


main()
