print("Please enter a sequence:")
sequence = input()

print("Please enter the character for the marker:")
marker = input()

marker1Position = -1
marker2Position = -1

for position in range(0, len(sequence), 1):
    letter = sequence[position]

    if (letter == marker):
        if (marker1Position == -1):
            marker1Position = position
        else:
            marker2Position = position

print(f"The distance between the markers is {marker2Position - marker1Position - 1}.")