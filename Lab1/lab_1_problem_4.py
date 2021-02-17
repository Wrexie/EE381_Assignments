import numpy as np


# Generates a random password given a
# password length requirement and a character list
def generatePassword(length, characterList):
    password = ""
    for i in range(length):
        password += characterList[np.random.randint(len(characterList))]

    return password


# Generates a list of random passwords given a size of the list,
# a password length requirement, and a character list
def generateHackerList(listSize, passwordLength, characterList):
    list = []
    password = ""
    for i in range(listSize):
        for j in range(passwordLength):
            password += characterList[np.random.randint(len(characterList))]
        list.append(password)
        password = ""

    return list


# Main function
def main():
    # m = 80000 k = 7
    m = 80000
    k = 7
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    N = 1000
    successCount1 = 0

    print("This might take a second... \n")

    # Check list of size m
    hackerList = generateHackerList(m, 4, alphabet)
    for i in range(N):
        password = generatePassword(4, alphabet)

        if password in hackerList:
            successCount1 += 1

    print("Probability of password being in hacker list of size: m")
    print(successCount1 / N)

    # Check list of size k * m
    successCount2 = 0
    hackerList = generateHackerList(m * k, 4, alphabet)
    for i in range(N):
        password = generatePassword(4, alphabet)

        if password in hackerList:
            successCount2 += 1

    print("Probability of password being in a hacker list of size: m * k")
    print(successCount2 / N)
    print()

    # Find how many words for prob. of p = 0.5
    successCount3 = 0
    m = 20000
    prob = 0.0
    hackerList = generateHackerList(m, 4, alphabet)
    while prob < .5 - .05:
        hackerListAddition = generateHackerList(m, 4, alphabet)
        hackerList += hackerListAddition
        for i in range(N):
            password = generatePassword(4, alphabet)

            if password in hackerList:
                successCount3 += 1

        prob = successCount3 / N
        m += 20000
        print(prob)

    print("The number of words required for a probability of p = .5 is: ")
    print(len(hackerList))


main()
