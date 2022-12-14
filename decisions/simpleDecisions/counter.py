print("Please enter the first whole number.")
a = int(input())
print("Please enter the second whole number.")
b = int(input())
print("Please enter the third whole number.")
c = int(input())

evenNumbers = 0
oddNumbers = 0


if (a % 2 == 0):
    evenNumbers = evenNumbers + 1
else:
    oddNumbers = oddNumbers + 1

if (b % 2 == 0):
    evenNumbers = evenNumbers + 1
else:
    oddNumbers = oddNumbers + 1

if (c % 2 == 0):
    evenNumbers = evenNumbers + 1
else:
    oddNumbers = oddNumbers + 1


print("There were {} even and {} odd numbers.".format(evenNumbers, oddNumbers))