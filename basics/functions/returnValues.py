def sumWeights(beepWeight, bopWeight):
    totalWeight = beepWeight + bopWeight
    return totalWeight

def calcAvgWeight(beepWeight, bopWeight):
    avgWeight = (beepWeight + bopWeight) / 2
    return avgWeight

def run():
    print("What is the weight of Bop?")
    bopWeight = float(input())

    print("What is the weight of Beep?")
    beepWeight = float(input())

    print("What would you like to calculate (sum or average)?")
    action = input()

    if (action == "sum"):
        answer = sumWeights(beepWeight, bopWeight)
        print("The sum of Beep's and Bop's weight is {:.2f}".format(answer))
    elif (action == "average"):
        answer = calcAvgWeight(beepWeight, bopWeight)
        print("The average of Beep's and Bop's weight is {:.2f}".format(answer))
    else:
        print("I am not sure what you would like to do.")


run()