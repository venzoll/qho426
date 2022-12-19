def displayLadder(steps):
    for step in range(steps):
        print("| |")
        print("***") 

    print("| |")

def createLadder():
    print("How many steps remain?")
    steps = int(input())
    displayLadder(steps)

createLadder()