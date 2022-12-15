print("How many live cables should I avoid?")
liveCables = int(input())
avoided = 0

print()

while(avoided < liveCables):
  print("Avoiding...", end="")
  avoided = avoided + 1
  print("Done!", avoided, "cables avoided." )

print()
print("All live cables have been avoided.")
