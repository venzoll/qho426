print("How many numbers should I sum up?")
numbersToSum = int(input())

position = 1
print()
total = 0

while (position <= numbersToSum):
    print("Please enter number", position, "of", numbersToSum, ":")
    number = int(input())
    total = total + number
    position = position + 1

print("The answer is", total)

