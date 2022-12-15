print("Where should I look?")
where = input()
if (where == "In the bedroom"):
  print("Where in the bedroom should I look?")
  whereBedroom = input()
  if (whereBedroom == "under the bed"):
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery.")
elif (where == "in the bathroom"):
  print("Where in the bathroom should I look?")
  whereBathroom = input()
  if (whereBathroom == "in the bathtub"):
    print("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but no battery.")
elif (where == "in the lab"):
  print("Where in the lab should I look?")
  whereLab = input()
  if (whereLab == "on the table"):
   print("Yes! I found my battery!")
  else:
    print("Found some tools but no battery.")
else:
  print("I do not know where that is but I will keep looking.")