print("What level of brightness is required?")
brightnessDesired = int(input())


print("\nAdjusting brightness...\n")

for brightness in range(2, brightnessDesired + 1, 2):
    print("Beep's brightness level:", "*" * brightness)
    print("Bop's brightness level:", "*" * brightness)

print("\nAdjustments complete!")