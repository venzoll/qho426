print("Program Started!\n")

print("Please enter an ASCII code:")
code = int(input())

if (code >= 32 and code <= 126):
    print("\nThe character represented by the ASCII value {} is: {}".format(code, chr(code)))
else:
    print("\nThe character cannot be displayed.")
print("Program Ended!")