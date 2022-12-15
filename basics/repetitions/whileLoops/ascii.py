print("How many bars should be charged?")
shouldCharged = int(input())
barsCharged = 0

print()

while(barsCharged < shouldCharged):
  barsCharged = barsCharged + 1
  print("Charging:",  "\u2588 " * barsCharged )
  print()

print("The battery is fully charged.")

