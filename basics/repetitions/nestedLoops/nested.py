print("How many rows should I have?")
rows = int(input())

print("\nHow many columns should I have?")
columns = int(input())

for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(":-)", end="")
    print()