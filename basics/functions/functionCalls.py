def displayBox(word):
    numDashes = 4 + len(word)
    print("-" * numDashes)
    print("| {} |".format(word))
    print("-" * numDashes)

def displayLowerCase(word):
    print(word.lower())

def displayUpperCase(word):
    print(word.upper())

def displayMirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print("{} | {}".format(word, mirrored))

def displayRepeated(word):
    print("How many times should the word be displayed?")
    repetitions = int(input())

    for repetition in range(repetitions):
        if (repetition % 2 == 0):
            print(displayLowerCase(word))
        else:
            print(displayUpperCase(word))

def run():
    print("Please enter a word:")
    word = input()
    response = 0

    while (response != 6):
        print("What would you like to do with this word?")
        print("[1] Display in a box")
        print("[2] Display lower-case")
        print("[3] Display upper-case")
        print("[4] Display mirrored")
        print("[5] Display repeated")
        print("[6] Quit")

        response = int(input()) 
 
        if (response == 1):
            displayBox(word)
        elif (response == 2):
            displayLowerCase(word)
        elif (response == 3):
            displayUpperCase(word)
        elif (response == 4):
            displayMirrored(word)
        elif (response == 5):
            displayRepeated(word)
        elif (response == 6):
            break
        else:
            print("Unknown option.") 

run()